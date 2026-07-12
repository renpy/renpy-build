import Foundation
import UIKit
import DeclaredAgeRange

@objc(Age)
final class Age: NSObject {

    private static let stateLock = NSLock()

    private static var requestedStorage = false
    private static var inProgressStorage = false
    private static var validStorage = false
    private static var ageLowerStorage = -1
    private static var ageUpperStorage = 150

    @objc class var requested: Bool {
        stateLock.lock()
        defer { stateLock.unlock() }
        return requestedStorage
    }

    @objc class var inProgress: Bool {
        stateLock.lock()
        defer { stateLock.unlock() }
        return inProgressStorage
    }

    @objc class var valid: Bool {
        stateLock.lock()
        defer { stateLock.unlock() }
        return validStorage
    }

    @objc class var ageLower: Int {
        stateLock.lock()
        defer { stateLock.unlock() }
        return ageLowerStorage
    }

    @objc class var ageUpper: Int {
        stateLock.lock()
        defer { stateLock.unlock() }
        return ageUpperStorage
    }

    @objc class func update() {
        guard #available(iOS 26.0, *) else {
            return
        }

        stateLock.lock()
        if requestedStorage {
            stateLock.unlock()
            return
        }

        requestedStorage = true
        inProgressStorage = true
        validStorage = false
        stateLock.unlock()

        Task { @MainActor in
            await requestAgeRange()
        }
    }

    @available(iOS 26.0, *)
    @MainActor
    private class func requestAgeRange() async {
        guard let viewController = activeViewController() else {
            markFailure()
            return
        }

        do {
            let response = try await AgeRangeService.shared.requestAgeRange(ageGates: 13, 16, 18, in: viewController)

            guard case let .sharing(ageRange) = response else {
                markFailure()
                return
            }

            let lower = ageRange.lowerBound ?? 0
            let upper = ageRange.upperBound ?? 150
            markSuccess(lower: lower, upper: upper)
        } catch {
            markFailure()
        }
    }

    @MainActor
    private class func activeViewController() -> UIViewController? {
        let scenes = UIApplication.shared.connectedScenes
            .compactMap { $0 as? UIWindowScene }
            .filter { scene in
                scene.activationState == .foregroundActive || scene.activationState == .foregroundInactive
            }

        for scene in scenes {
            if let root = scene.windows.first(where: { $0.isKeyWindow })?.rootViewController {
                return topViewController(from: root)
            }
        }

        return nil
    }

    private class func topViewController(from root: UIViewController) -> UIViewController {
        if let presented = root.presentedViewController {
            return topViewController(from: presented)
        }

        if let navigationController = root as? UINavigationController,
           let visible = navigationController.visibleViewController {
            return topViewController(from: visible)
        }

        if let tabBarController = root as? UITabBarController,
           let selected = tabBarController.selectedViewController {
            return topViewController(from: selected)
        }

        return root
    }

    private class func markSuccess(lower: Int, upper: Int) {
        stateLock.lock()
        defer { stateLock.unlock() }
        ageLowerStorage = lower
        ageUpperStorage = upper
        validStorage = true
        inProgressStorage = false
    }

    private class func markFailure() {
        stateLock.lock()
        defer { stateLock.unlock() }
        validStorage = false
        inProgressStorage = false
    }
}
