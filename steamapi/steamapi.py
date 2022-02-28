from ctypes import (
    c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_long, c_ulong,
    c_longlong, c_ulonglong, c_char_p, c_void_p, c_bool, c_float, byref,
    c_double, c_size_t, Structure, POINTER, byref, cast, sizeof)

try:
    from typing import Any
except ImportError:
    pass

def not_ready(*args): # type: (...) -> Any
    raise RuntimeError("Please call steamapi.load() before this function.")

import platform
if platform.win32_ver()[0]:
    PACK = 8
else:
    PACK = 4



k_uAppIdInvalid = c_uint(0)
k_uDepotIdInvalid = c_uint(0)
k_uAPICallInvalid = c_ulonglong(0)
k_ulPartyBeaconIdInvalid = c_ulonglong(0)
k_HAuthTicketInvalid = c_uint(0)
k_unSteamAccountIDMask = c_uint(0xffffffff)
k_unSteamAccountInstanceMask = c_uint(0xfffff)
k_unSteamUserDefaultInstance = c_uint(0x1)
k_cchGameExtraInfoMax = c_int(0x40)
k_cchMaxFriendsGroupName = c_int(0x40)
k_cFriendsGroupLimit = c_int(0x64)
k_FriendsGroupID_Invalid = c_short(-1)
k_cEnumerateFollowersMax = c_int(0x32)
k_cubChatMetadataMax = c_uint(0x2000)
k_cbMaxGameServerGameDir = c_int(0x20)
k_cbMaxGameServerMapName = c_int(0x20)
k_cbMaxGameServerGameDescription = c_int(0x40)
k_cbMaxGameServerName = c_int(0x40)
k_cbMaxGameServerTags = c_int(0x80)
k_cbMaxGameServerGameData = c_int(0x800)
HSERVERQUERY_INVALID = c_int(0xffffffff)
k_unFavoriteFlagNone = c_uint(0)
k_unFavoriteFlagFavorite = c_uint(0x1)
k_unFavoriteFlagHistory = c_uint(0x2)
k_unMaxCloudFileChunkSize = c_uint(0x6400000)
k_PublishedFileIdInvalid = c_ulonglong(0)
k_UGCHandleInvalid = c_ulonglong(0xffffffffffffffff)
k_PublishedFileUpdateHandleInvalid = c_ulonglong(0xffffffffffffffff)
k_UGCFileStreamHandleInvalid = c_ulonglong(0xffffffffffffffff)
k_cchPublishedDocumentTitleMax = c_uint(0x81)
k_cchPublishedDocumentDescriptionMax = c_uint(0x1f40)
k_cchPublishedDocumentChangeDescriptionMax = c_uint(0x1f40)
k_unEnumeratePublishedFilesMaxResults = c_uint(0x32)
k_cchTagListMax = c_uint(0x401)
k_cchFilenameMax = c_uint(0x104)
k_cchPublishedFileURLMax = c_uint(0x100)
k_cubAppProofOfPurchaseKeyMax = c_int(0xf0)
k_nScreenshotMaxTaggedUsers = c_uint(0x20)
k_nScreenshotMaxTaggedPublishedFiles = c_uint(0x20)
k_cubUFSTagTypeMax = c_int(0xff)
k_cubUFSTagValueMax = c_int(0xff)
k_ScreenshotThumbWidth = c_int(0xc8)
k_UGCQueryHandleInvalid = c_ulonglong(0xffffffffffffffff)
k_UGCUpdateHandleInvalid = c_ulonglong(0xffffffffffffffff)
kNumUGCResultsPerPage = c_uint(0x32)
k_cchDeveloperMetadataMax = c_uint(0x1388)
INVALID_HTMLBROWSER = c_uint(0)
k_SteamItemInstanceIDInvalid = c_ulonglong(-1)
k_SteamInventoryResultInvalid = c_int(-1)
k_SteamInventoryUpdateHandleInvalid = c_ulonglong(0xffffffffffffffff)
k_HSteamNetConnection_Invalid = c_uint(0)
k_HSteamListenSocket_Invalid = c_uint(0)
k_HSteamNetPollGroup_Invalid = c_uint(0)
k_cchMaxSteamNetworkingErrMsg = c_int(0x400)
k_cchSteamNetworkingMaxConnectionCloseReason = c_int(0x80)
k_cchSteamNetworkingMaxConnectionDescription = c_int(0x80)
k_cchSteamNetworkingMaxConnectionAppName = c_int(0x20)
k_nSteamNetworkConnectionInfoFlags_Unauthenticated = c_int(0x1)
k_nSteamNetworkConnectionInfoFlags_Unencrypted = c_int(0x2)
k_nSteamNetworkConnectionInfoFlags_LoopbackBuffers = c_int(0x4)
k_nSteamNetworkConnectionInfoFlags_Fast = c_int(0x8)
k_nSteamNetworkConnectionInfoFlags_Relayed = c_int(0x10)
k_nSteamNetworkConnectionInfoFlags_DualWifi = c_int(0x20)
k_cbMaxSteamNetworkingSocketsMessageSizeSend = c_int(0x80000)
k_nSteamNetworkingSend_Unreliable = c_int(0)
k_nSteamNetworkingSend_NoNagle = c_int(0x1)
k_nSteamNetworkingSend_UnreliableNoNagle = c_int(0x1)
k_nSteamNetworkingSend_NoDelay = c_int(0x4)
k_nSteamNetworkingSend_UnreliableNoDelay = c_int(0x5)
k_nSteamNetworkingSend_Reliable = c_int(0x8)
k_nSteamNetworkingSend_ReliableNoNagle = c_int(0x9)
k_nSteamNetworkingSend_UseCurrentThread = c_int(0x10)
k_nSteamNetworkingSend_AutoRestartBrokenSession = c_int(0x20)
k_cchMaxSteamNetworkingPingLocationString = c_int(0x400)
k_nSteamNetworkingPing_Failed = c_int(-1)
k_nSteamNetworkingPing_Unknown = c_int(-2)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_Default = c_int(-1)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_Disable = c_int(0)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_Relay = c_int(0x1)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_Private = c_int(0x2)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_Public = c_int(0x4)
k_nSteamNetworkingConfig_P2P_Transport_ICE_Enable_All = c_int(0x7fffffff)
k_SteamDatagramPOPID_dev = c_uint(0x646576)
STEAMGAMESERVER_QUERY_PORT_SHARED = c_ushort(0xffff)
MASTERSERVERUPDATERPORT_USEGAMESOCKETSHARE = c_ushort(0xffff)
k_cbSteamDatagramMaxSerializedTicket = c_uint(0x200)
k_cbMaxSteamDatagramGameCoordinatorServerLoginAppData = c_uint(0x800)
k_cbMaxSteamDatagramGameCoordinatorServerLoginSerialized = c_uint(0x1000)
k_cbSteamNetworkingSocketsFakeUDPPortRecommendedMTU = c_int(0x4b0)
k_cbSteamNetworkingSocketsFakeUDPPortMaxMessageSize = c_int(0x1000)


# Enums

class ESteamIPType(c_int):
    pass

k_ESteamIPTypeIPv4 = ESteamIPType(0)
k_ESteamIPTypeIPv6 = ESteamIPType(1)

class EUniverse(c_int):
    pass

k_EUniverseInvalid = EUniverse(0)
k_EUniversePublic = EUniverse(1)
k_EUniverseBeta = EUniverse(2)
k_EUniverseInternal = EUniverse(3)
k_EUniverseDev = EUniverse(4)
k_EUniverseMax = EUniverse(5)

class EResult(c_int):
    pass

k_EResultNone = EResult(0)
k_EResultOK = EResult(1)
k_EResultFail = EResult(2)
k_EResultNoConnection = EResult(3)
k_EResultInvalidPassword = EResult(5)
k_EResultLoggedInElsewhere = EResult(6)
k_EResultInvalidProtocolVer = EResult(7)
k_EResultInvalidParam = EResult(8)
k_EResultFileNotFound = EResult(9)
k_EResultBusy = EResult(10)
k_EResultInvalidState = EResult(11)
k_EResultInvalidName = EResult(12)
k_EResultInvalidEmail = EResult(13)
k_EResultDuplicateName = EResult(14)
k_EResultAccessDenied = EResult(15)
k_EResultTimeout = EResult(16)
k_EResultBanned = EResult(17)
k_EResultAccountNotFound = EResult(18)
k_EResultInvalidSteamID = EResult(19)
k_EResultServiceUnavailable = EResult(20)
k_EResultNotLoggedOn = EResult(21)
k_EResultPending = EResult(22)
k_EResultEncryptionFailure = EResult(23)
k_EResultInsufficientPrivilege = EResult(24)
k_EResultLimitExceeded = EResult(25)
k_EResultRevoked = EResult(26)
k_EResultExpired = EResult(27)
k_EResultAlreadyRedeemed = EResult(28)
k_EResultDuplicateRequest = EResult(29)
k_EResultAlreadyOwned = EResult(30)
k_EResultIPNotFound = EResult(31)
k_EResultPersistFailed = EResult(32)
k_EResultLockingFailed = EResult(33)
k_EResultLogonSessionReplaced = EResult(34)
k_EResultConnectFailed = EResult(35)
k_EResultHandshakeFailed = EResult(36)
k_EResultIOFailure = EResult(37)
k_EResultRemoteDisconnect = EResult(38)
k_EResultShoppingCartNotFound = EResult(39)
k_EResultBlocked = EResult(40)
k_EResultIgnored = EResult(41)
k_EResultNoMatch = EResult(42)
k_EResultAccountDisabled = EResult(43)
k_EResultServiceReadOnly = EResult(44)
k_EResultAccountNotFeatured = EResult(45)
k_EResultAdministratorOK = EResult(46)
k_EResultContentVersion = EResult(47)
k_EResultTryAnotherCM = EResult(48)
k_EResultPasswordRequiredToKickSession = EResult(49)
k_EResultAlreadyLoggedInElsewhere = EResult(50)
k_EResultSuspended = EResult(51)
k_EResultCancelled = EResult(52)
k_EResultDataCorruption = EResult(53)
k_EResultDiskFull = EResult(54)
k_EResultRemoteCallFailed = EResult(55)
k_EResultPasswordUnset = EResult(56)
k_EResultExternalAccountUnlinked = EResult(57)
k_EResultPSNTicketInvalid = EResult(58)
k_EResultExternalAccountAlreadyLinked = EResult(59)
k_EResultRemoteFileConflict = EResult(60)
k_EResultIllegalPassword = EResult(61)
k_EResultSameAsPreviousValue = EResult(62)
k_EResultAccountLogonDenied = EResult(63)
k_EResultCannotUseOldPassword = EResult(64)
k_EResultInvalidLoginAuthCode = EResult(65)
k_EResultAccountLogonDeniedNoMail = EResult(66)
k_EResultHardwareNotCapableOfIPT = EResult(67)
k_EResultIPTInitError = EResult(68)
k_EResultParentalControlRestricted = EResult(69)
k_EResultFacebookQueryError = EResult(70)
k_EResultExpiredLoginAuthCode = EResult(71)
k_EResultIPLoginRestrictionFailed = EResult(72)
k_EResultAccountLockedDown = EResult(73)
k_EResultAccountLogonDeniedVerifiedEmailRequired = EResult(74)
k_EResultNoMatchingURL = EResult(75)
k_EResultBadResponse = EResult(76)
k_EResultRequirePasswordReEntry = EResult(77)
k_EResultValueOutOfRange = EResult(78)
k_EResultUnexpectedError = EResult(79)
k_EResultDisabled = EResult(80)
k_EResultInvalidCEGSubmission = EResult(81)
k_EResultRestrictedDevice = EResult(82)
k_EResultRegionLocked = EResult(83)
k_EResultRateLimitExceeded = EResult(84)
k_EResultAccountLoginDeniedNeedTwoFactor = EResult(85)
k_EResultItemDeleted = EResult(86)
k_EResultAccountLoginDeniedThrottle = EResult(87)
k_EResultTwoFactorCodeMismatch = EResult(88)
k_EResultTwoFactorActivationCodeMismatch = EResult(89)
k_EResultAccountAssociatedToMultiplePartners = EResult(90)
k_EResultNotModified = EResult(91)
k_EResultNoMobileDevice = EResult(92)
k_EResultTimeNotSynced = EResult(93)
k_EResultSmsCodeFailed = EResult(94)
k_EResultAccountLimitExceeded = EResult(95)
k_EResultAccountActivityLimitExceeded = EResult(96)
k_EResultPhoneActivityLimitExceeded = EResult(97)
k_EResultRefundToWallet = EResult(98)
k_EResultEmailSendFailure = EResult(99)
k_EResultNotSettled = EResult(100)
k_EResultNeedCaptcha = EResult(101)
k_EResultGSLTDenied = EResult(102)
k_EResultGSOwnerDenied = EResult(103)
k_EResultInvalidItemType = EResult(104)
k_EResultIPBanned = EResult(105)
k_EResultGSLTExpired = EResult(106)
k_EResultInsufficientFunds = EResult(107)
k_EResultTooManyPending = EResult(108)
k_EResultNoSiteLicensesFound = EResult(109)
k_EResultWGNetworkSendExceeded = EResult(110)
k_EResultAccountNotFriends = EResult(111)
k_EResultLimitedUserAccount = EResult(112)
k_EResultCantRemoveItem = EResult(113)
k_EResultAccountDeleted = EResult(114)
k_EResultExistingUserCancelledLicense = EResult(115)
k_EResultCommunityCooldown = EResult(116)
k_EResultNoLauncherSpecified = EResult(117)
k_EResultMustAgreeToSSA = EResult(118)
k_EResultLauncherMigrated = EResult(119)
k_EResultSteamRealmMismatch = EResult(120)
k_EResultInvalidSignature = EResult(121)
k_EResultParseFailure = EResult(122)
k_EResultNoVerifiedPhone = EResult(123)

class EVoiceResult(c_int):
    pass

k_EVoiceResultOK = EVoiceResult(0)
k_EVoiceResultNotInitialized = EVoiceResult(1)
k_EVoiceResultNotRecording = EVoiceResult(2)
k_EVoiceResultNoData = EVoiceResult(3)
k_EVoiceResultBufferTooSmall = EVoiceResult(4)
k_EVoiceResultDataCorrupted = EVoiceResult(5)
k_EVoiceResultRestricted = EVoiceResult(6)
k_EVoiceResultUnsupportedCodec = EVoiceResult(7)
k_EVoiceResultReceiverOutOfDate = EVoiceResult(8)
k_EVoiceResultReceiverDidNotAnswer = EVoiceResult(9)

class EDenyReason(c_int):
    pass

k_EDenyInvalid = EDenyReason(0)
k_EDenyInvalidVersion = EDenyReason(1)
k_EDenyGeneric = EDenyReason(2)
k_EDenyNotLoggedOn = EDenyReason(3)
k_EDenyNoLicense = EDenyReason(4)
k_EDenyCheater = EDenyReason(5)
k_EDenyLoggedInElseWhere = EDenyReason(6)
k_EDenyUnknownText = EDenyReason(7)
k_EDenyIncompatibleAnticheat = EDenyReason(8)
k_EDenyMemoryCorruption = EDenyReason(9)
k_EDenyIncompatibleSoftware = EDenyReason(10)
k_EDenySteamConnectionLost = EDenyReason(11)
k_EDenySteamConnectionError = EDenyReason(12)
k_EDenySteamResponseTimedOut = EDenyReason(13)
k_EDenySteamValidationStalled = EDenyReason(14)
k_EDenySteamOwnerLeftGuestUser = EDenyReason(15)

class EBeginAuthSessionResult(c_int):
    pass

k_EBeginAuthSessionResultOK = EBeginAuthSessionResult(0)
k_EBeginAuthSessionResultInvalidTicket = EBeginAuthSessionResult(1)
k_EBeginAuthSessionResultDuplicateRequest = EBeginAuthSessionResult(2)
k_EBeginAuthSessionResultInvalidVersion = EBeginAuthSessionResult(3)
k_EBeginAuthSessionResultGameMismatch = EBeginAuthSessionResult(4)
k_EBeginAuthSessionResultExpiredTicket = EBeginAuthSessionResult(5)

class EAuthSessionResponse(c_int):
    pass

k_EAuthSessionResponseOK = EAuthSessionResponse(0)
k_EAuthSessionResponseUserNotConnectedToSteam = EAuthSessionResponse(1)
k_EAuthSessionResponseNoLicenseOrExpired = EAuthSessionResponse(2)
k_EAuthSessionResponseVACBanned = EAuthSessionResponse(3)
k_EAuthSessionResponseLoggedInElseWhere = EAuthSessionResponse(4)
k_EAuthSessionResponseVACCheckTimedOut = EAuthSessionResponse(5)
k_EAuthSessionResponseAuthTicketCanceled = EAuthSessionResponse(6)
k_EAuthSessionResponseAuthTicketInvalidAlreadyUsed = EAuthSessionResponse(7)
k_EAuthSessionResponseAuthTicketInvalid = EAuthSessionResponse(8)
k_EAuthSessionResponsePublisherIssuedBan = EAuthSessionResponse(9)

class EUserHasLicenseForAppResult(c_int):
    pass

k_EUserHasLicenseResultHasLicense = EUserHasLicenseForAppResult(0)
k_EUserHasLicenseResultDoesNotHaveLicense = EUserHasLicenseForAppResult(1)
k_EUserHasLicenseResultNoAuth = EUserHasLicenseForAppResult(2)

class EAccountType(c_int):
    pass

k_EAccountTypeInvalid = EAccountType(0)
k_EAccountTypeIndividual = EAccountType(1)
k_EAccountTypeMultiseat = EAccountType(2)
k_EAccountTypeGameServer = EAccountType(3)
k_EAccountTypeAnonGameServer = EAccountType(4)
k_EAccountTypePending = EAccountType(5)
k_EAccountTypeContentServer = EAccountType(6)
k_EAccountTypeClan = EAccountType(7)
k_EAccountTypeChat = EAccountType(8)
k_EAccountTypeConsoleUser = EAccountType(9)
k_EAccountTypeAnonUser = EAccountType(10)
k_EAccountTypeMax = EAccountType(11)

class EChatEntryType(c_int):
    pass

k_EChatEntryTypeInvalid = EChatEntryType(0)
k_EChatEntryTypeChatMsg = EChatEntryType(1)
k_EChatEntryTypeTyping = EChatEntryType(2)
k_EChatEntryTypeInviteGame = EChatEntryType(3)
k_EChatEntryTypeEmote = EChatEntryType(4)
k_EChatEntryTypeLeftConversation = EChatEntryType(6)
k_EChatEntryTypeEntered = EChatEntryType(7)
k_EChatEntryTypeWasKicked = EChatEntryType(8)
k_EChatEntryTypeWasBanned = EChatEntryType(9)
k_EChatEntryTypeDisconnected = EChatEntryType(10)
k_EChatEntryTypeHistoricalChat = EChatEntryType(11)
k_EChatEntryTypeLinkBlocked = EChatEntryType(14)

class EChatRoomEnterResponse(c_int):
    pass

k_EChatRoomEnterResponseSuccess = EChatRoomEnterResponse(1)
k_EChatRoomEnterResponseDoesntExist = EChatRoomEnterResponse(2)
k_EChatRoomEnterResponseNotAllowed = EChatRoomEnterResponse(3)
k_EChatRoomEnterResponseFull = EChatRoomEnterResponse(4)
k_EChatRoomEnterResponseError = EChatRoomEnterResponse(5)
k_EChatRoomEnterResponseBanned = EChatRoomEnterResponse(6)
k_EChatRoomEnterResponseLimited = EChatRoomEnterResponse(7)
k_EChatRoomEnterResponseClanDisabled = EChatRoomEnterResponse(8)
k_EChatRoomEnterResponseCommunityBan = EChatRoomEnterResponse(9)
k_EChatRoomEnterResponseMemberBlockedYou = EChatRoomEnterResponse(10)
k_EChatRoomEnterResponseYouBlockedMember = EChatRoomEnterResponse(11)
k_EChatRoomEnterResponseRatelimitExceeded = EChatRoomEnterResponse(15)

class EChatSteamIDInstanceFlags(c_int):
    pass

k_EChatAccountInstanceMask = EChatSteamIDInstanceFlags(4095)
k_EChatInstanceFlagClan = EChatSteamIDInstanceFlags(524288)
k_EChatInstanceFlagLobby = EChatSteamIDInstanceFlags(262144)
k_EChatInstanceFlagMMSLobby = EChatSteamIDInstanceFlags(131072)

class ENotificationPosition(c_int):
    pass

k_EPositionTopLeft = ENotificationPosition(0)
k_EPositionTopRight = ENotificationPosition(1)
k_EPositionBottomLeft = ENotificationPosition(2)
k_EPositionBottomRight = ENotificationPosition(3)

class EBroadcastUploadResult(c_int):
    pass

k_EBroadcastUploadResultNone = EBroadcastUploadResult(0)
k_EBroadcastUploadResultOK = EBroadcastUploadResult(1)
k_EBroadcastUploadResultInitFailed = EBroadcastUploadResult(2)
k_EBroadcastUploadResultFrameFailed = EBroadcastUploadResult(3)
k_EBroadcastUploadResultTimeout = EBroadcastUploadResult(4)
k_EBroadcastUploadResultBandwidthExceeded = EBroadcastUploadResult(5)
k_EBroadcastUploadResultLowFPS = EBroadcastUploadResult(6)
k_EBroadcastUploadResultMissingKeyFrames = EBroadcastUploadResult(7)
k_EBroadcastUploadResultNoConnection = EBroadcastUploadResult(8)
k_EBroadcastUploadResultRelayFailed = EBroadcastUploadResult(9)
k_EBroadcastUploadResultSettingsChanged = EBroadcastUploadResult(10)
k_EBroadcastUploadResultMissingAudio = EBroadcastUploadResult(11)
k_EBroadcastUploadResultTooFarBehind = EBroadcastUploadResult(12)
k_EBroadcastUploadResultTranscodeBehind = EBroadcastUploadResult(13)
k_EBroadcastUploadResultNotAllowedToPlay = EBroadcastUploadResult(14)
k_EBroadcastUploadResultBusy = EBroadcastUploadResult(15)
k_EBroadcastUploadResultBanned = EBroadcastUploadResult(16)
k_EBroadcastUploadResultAlreadyActive = EBroadcastUploadResult(17)
k_EBroadcastUploadResultForcedOff = EBroadcastUploadResult(18)
k_EBroadcastUploadResultAudioBehind = EBroadcastUploadResult(19)
k_EBroadcastUploadResultShutdown = EBroadcastUploadResult(20)
k_EBroadcastUploadResultDisconnect = EBroadcastUploadResult(21)
k_EBroadcastUploadResultVideoInitFailed = EBroadcastUploadResult(22)
k_EBroadcastUploadResultAudioInitFailed = EBroadcastUploadResult(23)

class EMarketNotAllowedReasonFlags(c_int):
    pass

k_EMarketNotAllowedReason_None = EMarketNotAllowedReasonFlags(0)
k_EMarketNotAllowedReason_TemporaryFailure = EMarketNotAllowedReasonFlags(1)
k_EMarketNotAllowedReason_AccountDisabled = EMarketNotAllowedReasonFlags(2)
k_EMarketNotAllowedReason_AccountLockedDown = EMarketNotAllowedReasonFlags(4)
k_EMarketNotAllowedReason_AccountLimited = EMarketNotAllowedReasonFlags(8)
k_EMarketNotAllowedReason_TradeBanned = EMarketNotAllowedReasonFlags(16)
k_EMarketNotAllowedReason_AccountNotTrusted = EMarketNotAllowedReasonFlags(32)
k_EMarketNotAllowedReason_SteamGuardNotEnabled = EMarketNotAllowedReasonFlags(64)
k_EMarketNotAllowedReason_SteamGuardOnlyRecentlyEnabled = EMarketNotAllowedReasonFlags(128)
k_EMarketNotAllowedReason_RecentPasswordReset = EMarketNotAllowedReasonFlags(256)
k_EMarketNotAllowedReason_NewPaymentMethod = EMarketNotAllowedReasonFlags(512)
k_EMarketNotAllowedReason_InvalidCookie = EMarketNotAllowedReasonFlags(1024)
k_EMarketNotAllowedReason_UsingNewDevice = EMarketNotAllowedReasonFlags(2048)
k_EMarketNotAllowedReason_RecentSelfRefund = EMarketNotAllowedReasonFlags(4096)
k_EMarketNotAllowedReason_NewPaymentMethodCannotBeVerified = EMarketNotAllowedReasonFlags(8192)
k_EMarketNotAllowedReason_NoRecentPurchases = EMarketNotAllowedReasonFlags(16384)
k_EMarketNotAllowedReason_AcceptedWalletGift = EMarketNotAllowedReasonFlags(32768)

class EDurationControlProgress(c_int):
    pass

k_EDurationControlProgress_Full = EDurationControlProgress(0)
k_EDurationControlProgress_Half = EDurationControlProgress(1)
k_EDurationControlProgress_None = EDurationControlProgress(2)
k_EDurationControl_ExitSoon_3h = EDurationControlProgress(3)
k_EDurationControl_ExitSoon_5h = EDurationControlProgress(4)
k_EDurationControl_ExitSoon_Night = EDurationControlProgress(5)

class EDurationControlNotification(c_int):
    pass

k_EDurationControlNotification_None = EDurationControlNotification(0)
k_EDurationControlNotification_1Hour = EDurationControlNotification(1)
k_EDurationControlNotification_3Hours = EDurationControlNotification(2)
k_EDurationControlNotification_HalfProgress = EDurationControlNotification(3)
k_EDurationControlNotification_NoProgress = EDurationControlNotification(4)
k_EDurationControlNotification_ExitSoon_3h = EDurationControlNotification(5)
k_EDurationControlNotification_ExitSoon_5h = EDurationControlNotification(6)
k_EDurationControlNotification_ExitSoon_Night = EDurationControlNotification(7)

class EDurationControlOnlineState(c_int):
    pass

k_EDurationControlOnlineState_Invalid = EDurationControlOnlineState(0)
k_EDurationControlOnlineState_Offline = EDurationControlOnlineState(1)
k_EDurationControlOnlineState_Online = EDurationControlOnlineState(2)
k_EDurationControlOnlineState_OnlineHighPri = EDurationControlOnlineState(3)

class EGameSearchErrorCode_t(c_int):
    pass

k_EGameSearchErrorCode_OK = EGameSearchErrorCode_t(1)
k_EGameSearchErrorCode_Failed_Search_Already_In_Progress = EGameSearchErrorCode_t(2)
k_EGameSearchErrorCode_Failed_No_Search_In_Progress = EGameSearchErrorCode_t(3)
k_EGameSearchErrorCode_Failed_Not_Lobby_Leader = EGameSearchErrorCode_t(4)
k_EGameSearchErrorCode_Failed_No_Host_Available = EGameSearchErrorCode_t(5)
k_EGameSearchErrorCode_Failed_Search_Params_Invalid = EGameSearchErrorCode_t(6)
k_EGameSearchErrorCode_Failed_Offline = EGameSearchErrorCode_t(7)
k_EGameSearchErrorCode_Failed_NotAuthorized = EGameSearchErrorCode_t(8)
k_EGameSearchErrorCode_Failed_Unknown_Error = EGameSearchErrorCode_t(9)

class EPlayerResult_t(c_int):
    pass

k_EPlayerResultFailedToConnect = EPlayerResult_t(1)
k_EPlayerResultAbandoned = EPlayerResult_t(2)
k_EPlayerResultKicked = EPlayerResult_t(3)
k_EPlayerResultIncomplete = EPlayerResult_t(4)
k_EPlayerResultCompleted = EPlayerResult_t(5)

class ESteamIPv6ConnectivityProtocol(c_int):
    pass

k_ESteamIPv6ConnectivityProtocol_Invalid = ESteamIPv6ConnectivityProtocol(0)
k_ESteamIPv6ConnectivityProtocol_HTTP = ESteamIPv6ConnectivityProtocol(1)
k_ESteamIPv6ConnectivityProtocol_UDP = ESteamIPv6ConnectivityProtocol(2)

class ESteamIPv6ConnectivityState(c_int):
    pass

k_ESteamIPv6ConnectivityState_Unknown = ESteamIPv6ConnectivityState(0)
k_ESteamIPv6ConnectivityState_Good = ESteamIPv6ConnectivityState(1)
k_ESteamIPv6ConnectivityState_Bad = ESteamIPv6ConnectivityState(2)

class EFriendRelationship(c_int):
    pass

k_EFriendRelationshipNone = EFriendRelationship(0)
k_EFriendRelationshipBlocked = EFriendRelationship(1)
k_EFriendRelationshipRequestRecipient = EFriendRelationship(2)
k_EFriendRelationshipFriend = EFriendRelationship(3)
k_EFriendRelationshipRequestInitiator = EFriendRelationship(4)
k_EFriendRelationshipIgnored = EFriendRelationship(5)
k_EFriendRelationshipIgnoredFriend = EFriendRelationship(6)
k_EFriendRelationshipSuggested_DEPRECATED = EFriendRelationship(7)
k_EFriendRelationshipMax = EFriendRelationship(8)

class EPersonaState(c_int):
    pass

k_EPersonaStateOffline = EPersonaState(0)
k_EPersonaStateOnline = EPersonaState(1)
k_EPersonaStateBusy = EPersonaState(2)
k_EPersonaStateAway = EPersonaState(3)
k_EPersonaStateSnooze = EPersonaState(4)
k_EPersonaStateLookingToTrade = EPersonaState(5)
k_EPersonaStateLookingToPlay = EPersonaState(6)
k_EPersonaStateInvisible = EPersonaState(7)
k_EPersonaStateMax = EPersonaState(8)

class EFriendFlags(c_int):
    pass

k_EFriendFlagNone = EFriendFlags(0)
k_EFriendFlagBlocked = EFriendFlags(1)
k_EFriendFlagFriendshipRequested = EFriendFlags(2)
k_EFriendFlagImmediate = EFriendFlags(4)
k_EFriendFlagClanMember = EFriendFlags(8)
k_EFriendFlagOnGameServer = EFriendFlags(16)
k_EFriendFlagRequestingFriendship = EFriendFlags(128)
k_EFriendFlagRequestingInfo = EFriendFlags(256)
k_EFriendFlagIgnored = EFriendFlags(512)
k_EFriendFlagIgnoredFriend = EFriendFlags(1024)
k_EFriendFlagChatMember = EFriendFlags(4096)
k_EFriendFlagAll = EFriendFlags(65535)

class EUserRestriction(c_int):
    pass

k_nUserRestrictionNone = EUserRestriction(0)
k_nUserRestrictionUnknown = EUserRestriction(1)
k_nUserRestrictionAnyChat = EUserRestriction(2)
k_nUserRestrictionVoiceChat = EUserRestriction(4)
k_nUserRestrictionGroupChat = EUserRestriction(8)
k_nUserRestrictionRating = EUserRestriction(16)
k_nUserRestrictionGameInvites = EUserRestriction(32)
k_nUserRestrictionTrading = EUserRestriction(64)

class EOverlayToStoreFlag(c_int):
    pass

k_EOverlayToStoreFlag_None = EOverlayToStoreFlag(0)
k_EOverlayToStoreFlag_AddToCart = EOverlayToStoreFlag(1)
k_EOverlayToStoreFlag_AddToCartAndShow = EOverlayToStoreFlag(2)

class EActivateGameOverlayToWebPageMode(c_int):
    pass

k_EActivateGameOverlayToWebPageMode_Default = EActivateGameOverlayToWebPageMode(0)
k_EActivateGameOverlayToWebPageMode_Modal = EActivateGameOverlayToWebPageMode(1)

class EPersonaChange(c_int):
    pass

k_EPersonaChangeName = EPersonaChange(1)
k_EPersonaChangeStatus = EPersonaChange(2)
k_EPersonaChangeComeOnline = EPersonaChange(4)
k_EPersonaChangeGoneOffline = EPersonaChange(8)
k_EPersonaChangeGamePlayed = EPersonaChange(16)
k_EPersonaChangeGameServer = EPersonaChange(32)
k_EPersonaChangeAvatar = EPersonaChange(64)
k_EPersonaChangeJoinedSource = EPersonaChange(128)
k_EPersonaChangeLeftSource = EPersonaChange(256)
k_EPersonaChangeRelationshipChanged = EPersonaChange(512)
k_EPersonaChangeNameFirstSet = EPersonaChange(1024)
k_EPersonaChangeBroadcast = EPersonaChange(2048)
k_EPersonaChangeNickname = EPersonaChange(4096)
k_EPersonaChangeSteamLevel = EPersonaChange(8192)
k_EPersonaChangeRichPresence = EPersonaChange(16384)

class ESteamAPICallFailure(c_int):
    pass

k_ESteamAPICallFailureNone = ESteamAPICallFailure(-1)
k_ESteamAPICallFailureSteamGone = ESteamAPICallFailure(0)
k_ESteamAPICallFailureNetworkFailure = ESteamAPICallFailure(1)
k_ESteamAPICallFailureInvalidHandle = ESteamAPICallFailure(2)
k_ESteamAPICallFailureMismatchedCallback = ESteamAPICallFailure(3)

class EGamepadTextInputMode(c_int):
    pass

k_EGamepadTextInputModeNormal = EGamepadTextInputMode(0)
k_EGamepadTextInputModePassword = EGamepadTextInputMode(1)

class EGamepadTextInputLineMode(c_int):
    pass

k_EGamepadTextInputLineModeSingleLine = EGamepadTextInputLineMode(0)
k_EGamepadTextInputLineModeMultipleLines = EGamepadTextInputLineMode(1)

class EFloatingGamepadTextInputMode(c_int):
    pass

k_EFloatingGamepadTextInputModeModeSingleLine = EFloatingGamepadTextInputMode(0)
k_EFloatingGamepadTextInputModeModeMultipleLines = EFloatingGamepadTextInputMode(1)
k_EFloatingGamepadTextInputModeModeEmail = EFloatingGamepadTextInputMode(2)
k_EFloatingGamepadTextInputModeModeNumeric = EFloatingGamepadTextInputMode(3)

class ETextFilteringContext(c_int):
    pass

k_ETextFilteringContextUnknown = ETextFilteringContext(0)
k_ETextFilteringContextGameContent = ETextFilteringContext(1)
k_ETextFilteringContextChat = ETextFilteringContext(2)
k_ETextFilteringContextName = ETextFilteringContext(3)

class ECheckFileSignature(c_int):
    pass

k_ECheckFileSignatureInvalidSignature = ECheckFileSignature(0)
k_ECheckFileSignatureValidSignature = ECheckFileSignature(1)
k_ECheckFileSignatureFileNotFound = ECheckFileSignature(2)
k_ECheckFileSignatureNoSignaturesFoundForThisApp = ECheckFileSignature(3)
k_ECheckFileSignatureNoSignaturesFoundForThisFile = ECheckFileSignature(4)

class EMatchMakingServerResponse(c_int):
    pass

eServerResponded = EMatchMakingServerResponse(0)
eServerFailedToRespond = EMatchMakingServerResponse(1)
eNoServersListedOnMasterServer = EMatchMakingServerResponse(2)

class ELobbyType(c_int):
    pass

k_ELobbyTypePrivate = ELobbyType(0)
k_ELobbyTypeFriendsOnly = ELobbyType(1)
k_ELobbyTypePublic = ELobbyType(2)
k_ELobbyTypeInvisible = ELobbyType(3)
k_ELobbyTypePrivateUnique = ELobbyType(4)

class ELobbyComparison(c_int):
    pass

k_ELobbyComparisonEqualToOrLessThan = ELobbyComparison(-2)
k_ELobbyComparisonLessThan = ELobbyComparison(-1)
k_ELobbyComparisonEqual = ELobbyComparison(0)
k_ELobbyComparisonGreaterThan = ELobbyComparison(1)
k_ELobbyComparisonEqualToOrGreaterThan = ELobbyComparison(2)
k_ELobbyComparisonNotEqual = ELobbyComparison(3)

class ELobbyDistanceFilter(c_int):
    pass

k_ELobbyDistanceFilterClose = ELobbyDistanceFilter(0)
k_ELobbyDistanceFilterDefault = ELobbyDistanceFilter(1)
k_ELobbyDistanceFilterFar = ELobbyDistanceFilter(2)
k_ELobbyDistanceFilterWorldwide = ELobbyDistanceFilter(3)

class EChatMemberStateChange(c_int):
    pass

k_EChatMemberStateChangeEntered = EChatMemberStateChange(1)
k_EChatMemberStateChangeLeft = EChatMemberStateChange(2)
k_EChatMemberStateChangeDisconnected = EChatMemberStateChange(4)
k_EChatMemberStateChangeKicked = EChatMemberStateChange(8)
k_EChatMemberStateChangeBanned = EChatMemberStateChange(16)

class ESteamPartyBeaconLocationType(c_int):
    pass

k_ESteamPartyBeaconLocationType_Invalid = ESteamPartyBeaconLocationType(0)
k_ESteamPartyBeaconLocationType_ChatGroup = ESteamPartyBeaconLocationType(1)
k_ESteamPartyBeaconLocationType_Max = ESteamPartyBeaconLocationType(2)

class ESteamPartyBeaconLocationData(c_int):
    pass

k_ESteamPartyBeaconLocationDataInvalid = ESteamPartyBeaconLocationData(0)
k_ESteamPartyBeaconLocationDataName = ESteamPartyBeaconLocationData(1)
k_ESteamPartyBeaconLocationDataIconURLSmall = ESteamPartyBeaconLocationData(2)
k_ESteamPartyBeaconLocationDataIconURLMedium = ESteamPartyBeaconLocationData(3)
k_ESteamPartyBeaconLocationDataIconURLLarge = ESteamPartyBeaconLocationData(4)

class ERemoteStoragePlatform(c_int):
    pass

k_ERemoteStoragePlatformNone = ERemoteStoragePlatform(0)
k_ERemoteStoragePlatformWindows = ERemoteStoragePlatform(1)
k_ERemoteStoragePlatformOSX = ERemoteStoragePlatform(2)
k_ERemoteStoragePlatformPS3 = ERemoteStoragePlatform(4)
k_ERemoteStoragePlatformLinux = ERemoteStoragePlatform(8)
k_ERemoteStoragePlatformSwitch = ERemoteStoragePlatform(16)
k_ERemoteStoragePlatformAndroid = ERemoteStoragePlatform(32)
k_ERemoteStoragePlatformIOS = ERemoteStoragePlatform(64)
k_ERemoteStoragePlatformAll = ERemoteStoragePlatform(-1)

class ERemoteStoragePublishedFileVisibility(c_int):
    pass

k_ERemoteStoragePublishedFileVisibilityPublic = ERemoteStoragePublishedFileVisibility(0)
k_ERemoteStoragePublishedFileVisibilityFriendsOnly = ERemoteStoragePublishedFileVisibility(1)
k_ERemoteStoragePublishedFileVisibilityPrivate = ERemoteStoragePublishedFileVisibility(2)
k_ERemoteStoragePublishedFileVisibilityUnlisted = ERemoteStoragePublishedFileVisibility(3)

class EWorkshopFileType(c_int):
    pass

k_EWorkshopFileTypeFirst = EWorkshopFileType(0)
k_EWorkshopFileTypeCommunity = EWorkshopFileType(0)
k_EWorkshopFileTypeMicrotransaction = EWorkshopFileType(1)
k_EWorkshopFileTypeCollection = EWorkshopFileType(2)
k_EWorkshopFileTypeArt = EWorkshopFileType(3)
k_EWorkshopFileTypeVideo = EWorkshopFileType(4)
k_EWorkshopFileTypeScreenshot = EWorkshopFileType(5)
k_EWorkshopFileTypeGame = EWorkshopFileType(6)
k_EWorkshopFileTypeSoftware = EWorkshopFileType(7)
k_EWorkshopFileTypeConcept = EWorkshopFileType(8)
k_EWorkshopFileTypeWebGuide = EWorkshopFileType(9)
k_EWorkshopFileTypeIntegratedGuide = EWorkshopFileType(10)
k_EWorkshopFileTypeMerch = EWorkshopFileType(11)
k_EWorkshopFileTypeControllerBinding = EWorkshopFileType(12)
k_EWorkshopFileTypeSteamworksAccessInvite = EWorkshopFileType(13)
k_EWorkshopFileTypeSteamVideo = EWorkshopFileType(14)
k_EWorkshopFileTypeGameManagedItem = EWorkshopFileType(15)
k_EWorkshopFileTypeMax = EWorkshopFileType(16)

class EWorkshopVote(c_int):
    pass

k_EWorkshopVoteUnvoted = EWorkshopVote(0)
k_EWorkshopVoteFor = EWorkshopVote(1)
k_EWorkshopVoteAgainst = EWorkshopVote(2)
k_EWorkshopVoteLater = EWorkshopVote(3)

class EWorkshopFileAction(c_int):
    pass

k_EWorkshopFileActionPlayed = EWorkshopFileAction(0)
k_EWorkshopFileActionCompleted = EWorkshopFileAction(1)

class EWorkshopEnumerationType(c_int):
    pass

k_EWorkshopEnumerationTypeRankedByVote = EWorkshopEnumerationType(0)
k_EWorkshopEnumerationTypeRecent = EWorkshopEnumerationType(1)
k_EWorkshopEnumerationTypeTrending = EWorkshopEnumerationType(2)
k_EWorkshopEnumerationTypeFavoritesOfFriends = EWorkshopEnumerationType(3)
k_EWorkshopEnumerationTypeVotedByFriends = EWorkshopEnumerationType(4)
k_EWorkshopEnumerationTypeContentByFriends = EWorkshopEnumerationType(5)
k_EWorkshopEnumerationTypeRecentFromFollowedUsers = EWorkshopEnumerationType(6)

class EWorkshopVideoProvider(c_int):
    pass

k_EWorkshopVideoProviderNone = EWorkshopVideoProvider(0)
k_EWorkshopVideoProviderYoutube = EWorkshopVideoProvider(1)

class EUGCReadAction(c_int):
    pass

k_EUGCRead_ContinueReadingUntilFinished = EUGCReadAction(0)
k_EUGCRead_ContinueReading = EUGCReadAction(1)
k_EUGCRead_Close = EUGCReadAction(2)

class ERemoteStorageLocalFileChange(c_int):
    pass

k_ERemoteStorageLocalFileChange_Invalid = ERemoteStorageLocalFileChange(0)
k_ERemoteStorageLocalFileChange_FileUpdated = ERemoteStorageLocalFileChange(1)
k_ERemoteStorageLocalFileChange_FileDeleted = ERemoteStorageLocalFileChange(2)

class ERemoteStorageFilePathType(c_int):
    pass

k_ERemoteStorageFilePathType_Invalid = ERemoteStorageFilePathType(0)
k_ERemoteStorageFilePathType_Absolute = ERemoteStorageFilePathType(1)
k_ERemoteStorageFilePathType_APIFilename = ERemoteStorageFilePathType(2)

class ELeaderboardDataRequest(c_int):
    pass

k_ELeaderboardDataRequestGlobal = ELeaderboardDataRequest(0)
k_ELeaderboardDataRequestGlobalAroundUser = ELeaderboardDataRequest(1)
k_ELeaderboardDataRequestFriends = ELeaderboardDataRequest(2)
k_ELeaderboardDataRequestUsers = ELeaderboardDataRequest(3)

class ELeaderboardSortMethod(c_int):
    pass

k_ELeaderboardSortMethodNone = ELeaderboardSortMethod(0)
k_ELeaderboardSortMethodAscending = ELeaderboardSortMethod(1)
k_ELeaderboardSortMethodDescending = ELeaderboardSortMethod(2)

class ELeaderboardDisplayType(c_int):
    pass

k_ELeaderboardDisplayTypeNone = ELeaderboardDisplayType(0)
k_ELeaderboardDisplayTypeNumeric = ELeaderboardDisplayType(1)
k_ELeaderboardDisplayTypeTimeSeconds = ELeaderboardDisplayType(2)
k_ELeaderboardDisplayTypeTimeMilliSeconds = ELeaderboardDisplayType(3)

class ELeaderboardUploadScoreMethod(c_int):
    pass

k_ELeaderboardUploadScoreMethodNone = ELeaderboardUploadScoreMethod(0)
k_ELeaderboardUploadScoreMethodKeepBest = ELeaderboardUploadScoreMethod(1)
k_ELeaderboardUploadScoreMethodForceUpdate = ELeaderboardUploadScoreMethod(2)

class ERegisterActivationCodeResult(c_int):
    pass

k_ERegisterActivationCodeResultOK = ERegisterActivationCodeResult(0)
k_ERegisterActivationCodeResultFail = ERegisterActivationCodeResult(1)
k_ERegisterActivationCodeResultAlreadyRegistered = ERegisterActivationCodeResult(2)
k_ERegisterActivationCodeResultTimeout = ERegisterActivationCodeResult(3)
k_ERegisterActivationCodeAlreadyOwned = ERegisterActivationCodeResult(4)

class EP2PSessionError(c_int):
    pass

k_EP2PSessionErrorNone = EP2PSessionError(0)
k_EP2PSessionErrorNoRightsToApp = EP2PSessionError(2)
k_EP2PSessionErrorTimeout = EP2PSessionError(4)
k_EP2PSessionErrorNotRunningApp_DELETED = EP2PSessionError(1)
k_EP2PSessionErrorDestinationNotLoggedIn_DELETED = EP2PSessionError(3)
k_EP2PSessionErrorMax = EP2PSessionError(5)

class EP2PSend(c_int):
    pass

k_EP2PSendUnreliable = EP2PSend(0)
k_EP2PSendUnreliableNoDelay = EP2PSend(1)
k_EP2PSendReliable = EP2PSend(2)
k_EP2PSendReliableWithBuffering = EP2PSend(3)

class ESNetSocketState(c_int):
    pass

k_ESNetSocketStateInvalid = ESNetSocketState(0)
k_ESNetSocketStateConnected = ESNetSocketState(1)
k_ESNetSocketStateInitiated = ESNetSocketState(10)
k_ESNetSocketStateLocalCandidatesFound = ESNetSocketState(11)
k_ESNetSocketStateReceivedRemoteCandidates = ESNetSocketState(12)
k_ESNetSocketStateChallengeHandshake = ESNetSocketState(15)
k_ESNetSocketStateDisconnecting = ESNetSocketState(21)
k_ESNetSocketStateLocalDisconnect = ESNetSocketState(22)
k_ESNetSocketStateTimeoutDuringConnect = ESNetSocketState(23)
k_ESNetSocketStateRemoteEndDisconnected = ESNetSocketState(24)
k_ESNetSocketStateConnectionBroken = ESNetSocketState(25)

class ESNetSocketConnectionType(c_int):
    pass

k_ESNetSocketConnectionTypeNotConnected = ESNetSocketConnectionType(0)
k_ESNetSocketConnectionTypeUDP = ESNetSocketConnectionType(1)
k_ESNetSocketConnectionTypeUDPRelay = ESNetSocketConnectionType(2)

class EVRScreenshotType(c_int):
    pass

k_EVRScreenshotType_None = EVRScreenshotType(0)
k_EVRScreenshotType_Mono = EVRScreenshotType(1)
k_EVRScreenshotType_Stereo = EVRScreenshotType(2)
k_EVRScreenshotType_MonoCubemap = EVRScreenshotType(3)
k_EVRScreenshotType_MonoPanorama = EVRScreenshotType(4)
k_EVRScreenshotType_StereoPanorama = EVRScreenshotType(5)

class AudioPlayback_Status(c_int):
    pass

AudioPlayback_Undefined = AudioPlayback_Status(0)
AudioPlayback_Playing = AudioPlayback_Status(1)
AudioPlayback_Paused = AudioPlayback_Status(2)
AudioPlayback_Idle = AudioPlayback_Status(3)

class EHTTPMethod(c_int):
    pass

k_EHTTPMethodInvalid = EHTTPMethod(0)
k_EHTTPMethodGET = EHTTPMethod(1)
k_EHTTPMethodHEAD = EHTTPMethod(2)
k_EHTTPMethodPOST = EHTTPMethod(3)
k_EHTTPMethodPUT = EHTTPMethod(4)
k_EHTTPMethodDELETE = EHTTPMethod(5)
k_EHTTPMethodOPTIONS = EHTTPMethod(6)
k_EHTTPMethodPATCH = EHTTPMethod(7)

class EHTTPStatusCode(c_int):
    pass

k_EHTTPStatusCodeInvalid = EHTTPStatusCode(0)
k_EHTTPStatusCode100Continue = EHTTPStatusCode(100)
k_EHTTPStatusCode101SwitchingProtocols = EHTTPStatusCode(101)
k_EHTTPStatusCode200OK = EHTTPStatusCode(200)
k_EHTTPStatusCode201Created = EHTTPStatusCode(201)
k_EHTTPStatusCode202Accepted = EHTTPStatusCode(202)
k_EHTTPStatusCode203NonAuthoritative = EHTTPStatusCode(203)
k_EHTTPStatusCode204NoContent = EHTTPStatusCode(204)
k_EHTTPStatusCode205ResetContent = EHTTPStatusCode(205)
k_EHTTPStatusCode206PartialContent = EHTTPStatusCode(206)
k_EHTTPStatusCode300MultipleChoices = EHTTPStatusCode(300)
k_EHTTPStatusCode301MovedPermanently = EHTTPStatusCode(301)
k_EHTTPStatusCode302Found = EHTTPStatusCode(302)
k_EHTTPStatusCode303SeeOther = EHTTPStatusCode(303)
k_EHTTPStatusCode304NotModified = EHTTPStatusCode(304)
k_EHTTPStatusCode305UseProxy = EHTTPStatusCode(305)
k_EHTTPStatusCode307TemporaryRedirect = EHTTPStatusCode(307)
k_EHTTPStatusCode400BadRequest = EHTTPStatusCode(400)
k_EHTTPStatusCode401Unauthorized = EHTTPStatusCode(401)
k_EHTTPStatusCode402PaymentRequired = EHTTPStatusCode(402)
k_EHTTPStatusCode403Forbidden = EHTTPStatusCode(403)
k_EHTTPStatusCode404NotFound = EHTTPStatusCode(404)
k_EHTTPStatusCode405MethodNotAllowed = EHTTPStatusCode(405)
k_EHTTPStatusCode406NotAcceptable = EHTTPStatusCode(406)
k_EHTTPStatusCode407ProxyAuthRequired = EHTTPStatusCode(407)
k_EHTTPStatusCode408RequestTimeout = EHTTPStatusCode(408)
k_EHTTPStatusCode409Conflict = EHTTPStatusCode(409)
k_EHTTPStatusCode410Gone = EHTTPStatusCode(410)
k_EHTTPStatusCode411LengthRequired = EHTTPStatusCode(411)
k_EHTTPStatusCode412PreconditionFailed = EHTTPStatusCode(412)
k_EHTTPStatusCode413RequestEntityTooLarge = EHTTPStatusCode(413)
k_EHTTPStatusCode414RequestURITooLong = EHTTPStatusCode(414)
k_EHTTPStatusCode415UnsupportedMediaType = EHTTPStatusCode(415)
k_EHTTPStatusCode416RequestedRangeNotSatisfiable = EHTTPStatusCode(416)
k_EHTTPStatusCode417ExpectationFailed = EHTTPStatusCode(417)
k_EHTTPStatusCode4xxUnknown = EHTTPStatusCode(418)
k_EHTTPStatusCode429TooManyRequests = EHTTPStatusCode(429)
k_EHTTPStatusCode444ConnectionClosed = EHTTPStatusCode(444)
k_EHTTPStatusCode500InternalServerError = EHTTPStatusCode(500)
k_EHTTPStatusCode501NotImplemented = EHTTPStatusCode(501)
k_EHTTPStatusCode502BadGateway = EHTTPStatusCode(502)
k_EHTTPStatusCode503ServiceUnavailable = EHTTPStatusCode(503)
k_EHTTPStatusCode504GatewayTimeout = EHTTPStatusCode(504)
k_EHTTPStatusCode505HTTPVersionNotSupported = EHTTPStatusCode(505)
k_EHTTPStatusCode5xxUnknown = EHTTPStatusCode(599)

class EInputSourceMode(c_int):
    pass

k_EInputSourceMode_None = EInputSourceMode(0)
k_EInputSourceMode_Dpad = EInputSourceMode(1)
k_EInputSourceMode_Buttons = EInputSourceMode(2)
k_EInputSourceMode_FourButtons = EInputSourceMode(3)
k_EInputSourceMode_AbsoluteMouse = EInputSourceMode(4)
k_EInputSourceMode_RelativeMouse = EInputSourceMode(5)
k_EInputSourceMode_JoystickMove = EInputSourceMode(6)
k_EInputSourceMode_JoystickMouse = EInputSourceMode(7)
k_EInputSourceMode_JoystickCamera = EInputSourceMode(8)
k_EInputSourceMode_ScrollWheel = EInputSourceMode(9)
k_EInputSourceMode_Trigger = EInputSourceMode(10)
k_EInputSourceMode_TouchMenu = EInputSourceMode(11)
k_EInputSourceMode_MouseJoystick = EInputSourceMode(12)
k_EInputSourceMode_MouseRegion = EInputSourceMode(13)
k_EInputSourceMode_RadialMenu = EInputSourceMode(14)
k_EInputSourceMode_SingleButton = EInputSourceMode(15)
k_EInputSourceMode_Switches = EInputSourceMode(16)

class EInputActionOrigin(c_int):
    pass

k_EInputActionOrigin_None = EInputActionOrigin(0)
k_EInputActionOrigin_SteamController_A = EInputActionOrigin(1)
k_EInputActionOrigin_SteamController_B = EInputActionOrigin(2)
k_EInputActionOrigin_SteamController_X = EInputActionOrigin(3)
k_EInputActionOrigin_SteamController_Y = EInputActionOrigin(4)
k_EInputActionOrigin_SteamController_LeftBumper = EInputActionOrigin(5)
k_EInputActionOrigin_SteamController_RightBumper = EInputActionOrigin(6)
k_EInputActionOrigin_SteamController_LeftGrip = EInputActionOrigin(7)
k_EInputActionOrigin_SteamController_RightGrip = EInputActionOrigin(8)
k_EInputActionOrigin_SteamController_Start = EInputActionOrigin(9)
k_EInputActionOrigin_SteamController_Back = EInputActionOrigin(10)
k_EInputActionOrigin_SteamController_LeftPad_Touch = EInputActionOrigin(11)
k_EInputActionOrigin_SteamController_LeftPad_Swipe = EInputActionOrigin(12)
k_EInputActionOrigin_SteamController_LeftPad_Click = EInputActionOrigin(13)
k_EInputActionOrigin_SteamController_LeftPad_DPadNorth = EInputActionOrigin(14)
k_EInputActionOrigin_SteamController_LeftPad_DPadSouth = EInputActionOrigin(15)
k_EInputActionOrigin_SteamController_LeftPad_DPadWest = EInputActionOrigin(16)
k_EInputActionOrigin_SteamController_LeftPad_DPadEast = EInputActionOrigin(17)
k_EInputActionOrigin_SteamController_RightPad_Touch = EInputActionOrigin(18)
k_EInputActionOrigin_SteamController_RightPad_Swipe = EInputActionOrigin(19)
k_EInputActionOrigin_SteamController_RightPad_Click = EInputActionOrigin(20)
k_EInputActionOrigin_SteamController_RightPad_DPadNorth = EInputActionOrigin(21)
k_EInputActionOrigin_SteamController_RightPad_DPadSouth = EInputActionOrigin(22)
k_EInputActionOrigin_SteamController_RightPad_DPadWest = EInputActionOrigin(23)
k_EInputActionOrigin_SteamController_RightPad_DPadEast = EInputActionOrigin(24)
k_EInputActionOrigin_SteamController_LeftTrigger_Pull = EInputActionOrigin(25)
k_EInputActionOrigin_SteamController_LeftTrigger_Click = EInputActionOrigin(26)
k_EInputActionOrigin_SteamController_RightTrigger_Pull = EInputActionOrigin(27)
k_EInputActionOrigin_SteamController_RightTrigger_Click = EInputActionOrigin(28)
k_EInputActionOrigin_SteamController_LeftStick_Move = EInputActionOrigin(29)
k_EInputActionOrigin_SteamController_LeftStick_Click = EInputActionOrigin(30)
k_EInputActionOrigin_SteamController_LeftStick_DPadNorth = EInputActionOrigin(31)
k_EInputActionOrigin_SteamController_LeftStick_DPadSouth = EInputActionOrigin(32)
k_EInputActionOrigin_SteamController_LeftStick_DPadWest = EInputActionOrigin(33)
k_EInputActionOrigin_SteamController_LeftStick_DPadEast = EInputActionOrigin(34)
k_EInputActionOrigin_SteamController_Gyro_Move = EInputActionOrigin(35)
k_EInputActionOrigin_SteamController_Gyro_Pitch = EInputActionOrigin(36)
k_EInputActionOrigin_SteamController_Gyro_Yaw = EInputActionOrigin(37)
k_EInputActionOrigin_SteamController_Gyro_Roll = EInputActionOrigin(38)
k_EInputActionOrigin_SteamController_Reserved0 = EInputActionOrigin(39)
k_EInputActionOrigin_SteamController_Reserved1 = EInputActionOrigin(40)
k_EInputActionOrigin_SteamController_Reserved2 = EInputActionOrigin(41)
k_EInputActionOrigin_SteamController_Reserved3 = EInputActionOrigin(42)
k_EInputActionOrigin_SteamController_Reserved4 = EInputActionOrigin(43)
k_EInputActionOrigin_SteamController_Reserved5 = EInputActionOrigin(44)
k_EInputActionOrigin_SteamController_Reserved6 = EInputActionOrigin(45)
k_EInputActionOrigin_SteamController_Reserved7 = EInputActionOrigin(46)
k_EInputActionOrigin_SteamController_Reserved8 = EInputActionOrigin(47)
k_EInputActionOrigin_SteamController_Reserved9 = EInputActionOrigin(48)
k_EInputActionOrigin_SteamController_Reserved10 = EInputActionOrigin(49)
k_EInputActionOrigin_PS4_X = EInputActionOrigin(50)
k_EInputActionOrigin_PS4_Circle = EInputActionOrigin(51)
k_EInputActionOrigin_PS4_Triangle = EInputActionOrigin(52)
k_EInputActionOrigin_PS4_Square = EInputActionOrigin(53)
k_EInputActionOrigin_PS4_LeftBumper = EInputActionOrigin(54)
k_EInputActionOrigin_PS4_RightBumper = EInputActionOrigin(55)
k_EInputActionOrigin_PS4_Options = EInputActionOrigin(56)
k_EInputActionOrigin_PS4_Share = EInputActionOrigin(57)
k_EInputActionOrigin_PS4_LeftPad_Touch = EInputActionOrigin(58)
k_EInputActionOrigin_PS4_LeftPad_Swipe = EInputActionOrigin(59)
k_EInputActionOrigin_PS4_LeftPad_Click = EInputActionOrigin(60)
k_EInputActionOrigin_PS4_LeftPad_DPadNorth = EInputActionOrigin(61)
k_EInputActionOrigin_PS4_LeftPad_DPadSouth = EInputActionOrigin(62)
k_EInputActionOrigin_PS4_LeftPad_DPadWest = EInputActionOrigin(63)
k_EInputActionOrigin_PS4_LeftPad_DPadEast = EInputActionOrigin(64)
k_EInputActionOrigin_PS4_RightPad_Touch = EInputActionOrigin(65)
k_EInputActionOrigin_PS4_RightPad_Swipe = EInputActionOrigin(66)
k_EInputActionOrigin_PS4_RightPad_Click = EInputActionOrigin(67)
k_EInputActionOrigin_PS4_RightPad_DPadNorth = EInputActionOrigin(68)
k_EInputActionOrigin_PS4_RightPad_DPadSouth = EInputActionOrigin(69)
k_EInputActionOrigin_PS4_RightPad_DPadWest = EInputActionOrigin(70)
k_EInputActionOrigin_PS4_RightPad_DPadEast = EInputActionOrigin(71)
k_EInputActionOrigin_PS4_CenterPad_Touch = EInputActionOrigin(72)
k_EInputActionOrigin_PS4_CenterPad_Swipe = EInputActionOrigin(73)
k_EInputActionOrigin_PS4_CenterPad_Click = EInputActionOrigin(74)
k_EInputActionOrigin_PS4_CenterPad_DPadNorth = EInputActionOrigin(75)
k_EInputActionOrigin_PS4_CenterPad_DPadSouth = EInputActionOrigin(76)
k_EInputActionOrigin_PS4_CenterPad_DPadWest = EInputActionOrigin(77)
k_EInputActionOrigin_PS4_CenterPad_DPadEast = EInputActionOrigin(78)
k_EInputActionOrigin_PS4_LeftTrigger_Pull = EInputActionOrigin(79)
k_EInputActionOrigin_PS4_LeftTrigger_Click = EInputActionOrigin(80)
k_EInputActionOrigin_PS4_RightTrigger_Pull = EInputActionOrigin(81)
k_EInputActionOrigin_PS4_RightTrigger_Click = EInputActionOrigin(82)
k_EInputActionOrigin_PS4_LeftStick_Move = EInputActionOrigin(83)
k_EInputActionOrigin_PS4_LeftStick_Click = EInputActionOrigin(84)
k_EInputActionOrigin_PS4_LeftStick_DPadNorth = EInputActionOrigin(85)
k_EInputActionOrigin_PS4_LeftStick_DPadSouth = EInputActionOrigin(86)
k_EInputActionOrigin_PS4_LeftStick_DPadWest = EInputActionOrigin(87)
k_EInputActionOrigin_PS4_LeftStick_DPadEast = EInputActionOrigin(88)
k_EInputActionOrigin_PS4_RightStick_Move = EInputActionOrigin(89)
k_EInputActionOrigin_PS4_RightStick_Click = EInputActionOrigin(90)
k_EInputActionOrigin_PS4_RightStick_DPadNorth = EInputActionOrigin(91)
k_EInputActionOrigin_PS4_RightStick_DPadSouth = EInputActionOrigin(92)
k_EInputActionOrigin_PS4_RightStick_DPadWest = EInputActionOrigin(93)
k_EInputActionOrigin_PS4_RightStick_DPadEast = EInputActionOrigin(94)
k_EInputActionOrigin_PS4_DPad_North = EInputActionOrigin(95)
k_EInputActionOrigin_PS4_DPad_South = EInputActionOrigin(96)
k_EInputActionOrigin_PS4_DPad_West = EInputActionOrigin(97)
k_EInputActionOrigin_PS4_DPad_East = EInputActionOrigin(98)
k_EInputActionOrigin_PS4_Gyro_Move = EInputActionOrigin(99)
k_EInputActionOrigin_PS4_Gyro_Pitch = EInputActionOrigin(100)
k_EInputActionOrigin_PS4_Gyro_Yaw = EInputActionOrigin(101)
k_EInputActionOrigin_PS4_Gyro_Roll = EInputActionOrigin(102)
k_EInputActionOrigin_PS4_DPad_Move = EInputActionOrigin(103)
k_EInputActionOrigin_PS4_Reserved1 = EInputActionOrigin(104)
k_EInputActionOrigin_PS4_Reserved2 = EInputActionOrigin(105)
k_EInputActionOrigin_PS4_Reserved3 = EInputActionOrigin(106)
k_EInputActionOrigin_PS4_Reserved4 = EInputActionOrigin(107)
k_EInputActionOrigin_PS4_Reserved5 = EInputActionOrigin(108)
k_EInputActionOrigin_PS4_Reserved6 = EInputActionOrigin(109)
k_EInputActionOrigin_PS4_Reserved7 = EInputActionOrigin(110)
k_EInputActionOrigin_PS4_Reserved8 = EInputActionOrigin(111)
k_EInputActionOrigin_PS4_Reserved9 = EInputActionOrigin(112)
k_EInputActionOrigin_PS4_Reserved10 = EInputActionOrigin(113)
k_EInputActionOrigin_XBoxOne_A = EInputActionOrigin(114)
k_EInputActionOrigin_XBoxOne_B = EInputActionOrigin(115)
k_EInputActionOrigin_XBoxOne_X = EInputActionOrigin(116)
k_EInputActionOrigin_XBoxOne_Y = EInputActionOrigin(117)
k_EInputActionOrigin_XBoxOne_LeftBumper = EInputActionOrigin(118)
k_EInputActionOrigin_XBoxOne_RightBumper = EInputActionOrigin(119)
k_EInputActionOrigin_XBoxOne_Menu = EInputActionOrigin(120)
k_EInputActionOrigin_XBoxOne_View = EInputActionOrigin(121)
k_EInputActionOrigin_XBoxOne_LeftTrigger_Pull = EInputActionOrigin(122)
k_EInputActionOrigin_XBoxOne_LeftTrigger_Click = EInputActionOrigin(123)
k_EInputActionOrigin_XBoxOne_RightTrigger_Pull = EInputActionOrigin(124)
k_EInputActionOrigin_XBoxOne_RightTrigger_Click = EInputActionOrigin(125)
k_EInputActionOrigin_XBoxOne_LeftStick_Move = EInputActionOrigin(126)
k_EInputActionOrigin_XBoxOne_LeftStick_Click = EInputActionOrigin(127)
k_EInputActionOrigin_XBoxOne_LeftStick_DPadNorth = EInputActionOrigin(128)
k_EInputActionOrigin_XBoxOne_LeftStick_DPadSouth = EInputActionOrigin(129)
k_EInputActionOrigin_XBoxOne_LeftStick_DPadWest = EInputActionOrigin(130)
k_EInputActionOrigin_XBoxOne_LeftStick_DPadEast = EInputActionOrigin(131)
k_EInputActionOrigin_XBoxOne_RightStick_Move = EInputActionOrigin(132)
k_EInputActionOrigin_XBoxOne_RightStick_Click = EInputActionOrigin(133)
k_EInputActionOrigin_XBoxOne_RightStick_DPadNorth = EInputActionOrigin(134)
k_EInputActionOrigin_XBoxOne_RightStick_DPadSouth = EInputActionOrigin(135)
k_EInputActionOrigin_XBoxOne_RightStick_DPadWest = EInputActionOrigin(136)
k_EInputActionOrigin_XBoxOne_RightStick_DPadEast = EInputActionOrigin(137)
k_EInputActionOrigin_XBoxOne_DPad_North = EInputActionOrigin(138)
k_EInputActionOrigin_XBoxOne_DPad_South = EInputActionOrigin(139)
k_EInputActionOrigin_XBoxOne_DPad_West = EInputActionOrigin(140)
k_EInputActionOrigin_XBoxOne_DPad_East = EInputActionOrigin(141)
k_EInputActionOrigin_XBoxOne_DPad_Move = EInputActionOrigin(142)
k_EInputActionOrigin_XBoxOne_LeftGrip_Lower = EInputActionOrigin(143)
k_EInputActionOrigin_XBoxOne_LeftGrip_Upper = EInputActionOrigin(144)
k_EInputActionOrigin_XBoxOne_RightGrip_Lower = EInputActionOrigin(145)
k_EInputActionOrigin_XBoxOne_RightGrip_Upper = EInputActionOrigin(146)
k_EInputActionOrigin_XBoxOne_Share = EInputActionOrigin(147)
k_EInputActionOrigin_XBoxOne_Reserved6 = EInputActionOrigin(148)
k_EInputActionOrigin_XBoxOne_Reserved7 = EInputActionOrigin(149)
k_EInputActionOrigin_XBoxOne_Reserved8 = EInputActionOrigin(150)
k_EInputActionOrigin_XBoxOne_Reserved9 = EInputActionOrigin(151)
k_EInputActionOrigin_XBoxOne_Reserved10 = EInputActionOrigin(152)
k_EInputActionOrigin_XBox360_A = EInputActionOrigin(153)
k_EInputActionOrigin_XBox360_B = EInputActionOrigin(154)
k_EInputActionOrigin_XBox360_X = EInputActionOrigin(155)
k_EInputActionOrigin_XBox360_Y = EInputActionOrigin(156)
k_EInputActionOrigin_XBox360_LeftBumper = EInputActionOrigin(157)
k_EInputActionOrigin_XBox360_RightBumper = EInputActionOrigin(158)
k_EInputActionOrigin_XBox360_Start = EInputActionOrigin(159)
k_EInputActionOrigin_XBox360_Back = EInputActionOrigin(160)
k_EInputActionOrigin_XBox360_LeftTrigger_Pull = EInputActionOrigin(161)
k_EInputActionOrigin_XBox360_LeftTrigger_Click = EInputActionOrigin(162)
k_EInputActionOrigin_XBox360_RightTrigger_Pull = EInputActionOrigin(163)
k_EInputActionOrigin_XBox360_RightTrigger_Click = EInputActionOrigin(164)
k_EInputActionOrigin_XBox360_LeftStick_Move = EInputActionOrigin(165)
k_EInputActionOrigin_XBox360_LeftStick_Click = EInputActionOrigin(166)
k_EInputActionOrigin_XBox360_LeftStick_DPadNorth = EInputActionOrigin(167)
k_EInputActionOrigin_XBox360_LeftStick_DPadSouth = EInputActionOrigin(168)
k_EInputActionOrigin_XBox360_LeftStick_DPadWest = EInputActionOrigin(169)
k_EInputActionOrigin_XBox360_LeftStick_DPadEast = EInputActionOrigin(170)
k_EInputActionOrigin_XBox360_RightStick_Move = EInputActionOrigin(171)
k_EInputActionOrigin_XBox360_RightStick_Click = EInputActionOrigin(172)
k_EInputActionOrigin_XBox360_RightStick_DPadNorth = EInputActionOrigin(173)
k_EInputActionOrigin_XBox360_RightStick_DPadSouth = EInputActionOrigin(174)
k_EInputActionOrigin_XBox360_RightStick_DPadWest = EInputActionOrigin(175)
k_EInputActionOrigin_XBox360_RightStick_DPadEast = EInputActionOrigin(176)
k_EInputActionOrigin_XBox360_DPad_North = EInputActionOrigin(177)
k_EInputActionOrigin_XBox360_DPad_South = EInputActionOrigin(178)
k_EInputActionOrigin_XBox360_DPad_West = EInputActionOrigin(179)
k_EInputActionOrigin_XBox360_DPad_East = EInputActionOrigin(180)
k_EInputActionOrigin_XBox360_DPad_Move = EInputActionOrigin(181)
k_EInputActionOrigin_XBox360_Reserved1 = EInputActionOrigin(182)
k_EInputActionOrigin_XBox360_Reserved2 = EInputActionOrigin(183)
k_EInputActionOrigin_XBox360_Reserved3 = EInputActionOrigin(184)
k_EInputActionOrigin_XBox360_Reserved4 = EInputActionOrigin(185)
k_EInputActionOrigin_XBox360_Reserved5 = EInputActionOrigin(186)
k_EInputActionOrigin_XBox360_Reserved6 = EInputActionOrigin(187)
k_EInputActionOrigin_XBox360_Reserved7 = EInputActionOrigin(188)
k_EInputActionOrigin_XBox360_Reserved8 = EInputActionOrigin(189)
k_EInputActionOrigin_XBox360_Reserved9 = EInputActionOrigin(190)
k_EInputActionOrigin_XBox360_Reserved10 = EInputActionOrigin(191)
k_EInputActionOrigin_Switch_A = EInputActionOrigin(192)
k_EInputActionOrigin_Switch_B = EInputActionOrigin(193)
k_EInputActionOrigin_Switch_X = EInputActionOrigin(194)
k_EInputActionOrigin_Switch_Y = EInputActionOrigin(195)
k_EInputActionOrigin_Switch_LeftBumper = EInputActionOrigin(196)
k_EInputActionOrigin_Switch_RightBumper = EInputActionOrigin(197)
k_EInputActionOrigin_Switch_Plus = EInputActionOrigin(198)
k_EInputActionOrigin_Switch_Minus = EInputActionOrigin(199)
k_EInputActionOrigin_Switch_Capture = EInputActionOrigin(200)
k_EInputActionOrigin_Switch_LeftTrigger_Pull = EInputActionOrigin(201)
k_EInputActionOrigin_Switch_LeftTrigger_Click = EInputActionOrigin(202)
k_EInputActionOrigin_Switch_RightTrigger_Pull = EInputActionOrigin(203)
k_EInputActionOrigin_Switch_RightTrigger_Click = EInputActionOrigin(204)
k_EInputActionOrigin_Switch_LeftStick_Move = EInputActionOrigin(205)
k_EInputActionOrigin_Switch_LeftStick_Click = EInputActionOrigin(206)
k_EInputActionOrigin_Switch_LeftStick_DPadNorth = EInputActionOrigin(207)
k_EInputActionOrigin_Switch_LeftStick_DPadSouth = EInputActionOrigin(208)
k_EInputActionOrigin_Switch_LeftStick_DPadWest = EInputActionOrigin(209)
k_EInputActionOrigin_Switch_LeftStick_DPadEast = EInputActionOrigin(210)
k_EInputActionOrigin_Switch_RightStick_Move = EInputActionOrigin(211)
k_EInputActionOrigin_Switch_RightStick_Click = EInputActionOrigin(212)
k_EInputActionOrigin_Switch_RightStick_DPadNorth = EInputActionOrigin(213)
k_EInputActionOrigin_Switch_RightStick_DPadSouth = EInputActionOrigin(214)
k_EInputActionOrigin_Switch_RightStick_DPadWest = EInputActionOrigin(215)
k_EInputActionOrigin_Switch_RightStick_DPadEast = EInputActionOrigin(216)
k_EInputActionOrigin_Switch_DPad_North = EInputActionOrigin(217)
k_EInputActionOrigin_Switch_DPad_South = EInputActionOrigin(218)
k_EInputActionOrigin_Switch_DPad_West = EInputActionOrigin(219)
k_EInputActionOrigin_Switch_DPad_East = EInputActionOrigin(220)
k_EInputActionOrigin_Switch_ProGyro_Move = EInputActionOrigin(221)
k_EInputActionOrigin_Switch_ProGyro_Pitch = EInputActionOrigin(222)
k_EInputActionOrigin_Switch_ProGyro_Yaw = EInputActionOrigin(223)
k_EInputActionOrigin_Switch_ProGyro_Roll = EInputActionOrigin(224)
k_EInputActionOrigin_Switch_DPad_Move = EInputActionOrigin(225)
k_EInputActionOrigin_Switch_Reserved1 = EInputActionOrigin(226)
k_EInputActionOrigin_Switch_Reserved2 = EInputActionOrigin(227)
k_EInputActionOrigin_Switch_Reserved3 = EInputActionOrigin(228)
k_EInputActionOrigin_Switch_Reserved4 = EInputActionOrigin(229)
k_EInputActionOrigin_Switch_Reserved5 = EInputActionOrigin(230)
k_EInputActionOrigin_Switch_Reserved6 = EInputActionOrigin(231)
k_EInputActionOrigin_Switch_Reserved7 = EInputActionOrigin(232)
k_EInputActionOrigin_Switch_Reserved8 = EInputActionOrigin(233)
k_EInputActionOrigin_Switch_Reserved9 = EInputActionOrigin(234)
k_EInputActionOrigin_Switch_Reserved10 = EInputActionOrigin(235)
k_EInputActionOrigin_Switch_RightGyro_Move = EInputActionOrigin(236)
k_EInputActionOrigin_Switch_RightGyro_Pitch = EInputActionOrigin(237)
k_EInputActionOrigin_Switch_RightGyro_Yaw = EInputActionOrigin(238)
k_EInputActionOrigin_Switch_RightGyro_Roll = EInputActionOrigin(239)
k_EInputActionOrigin_Switch_LeftGyro_Move = EInputActionOrigin(240)
k_EInputActionOrigin_Switch_LeftGyro_Pitch = EInputActionOrigin(241)
k_EInputActionOrigin_Switch_LeftGyro_Yaw = EInputActionOrigin(242)
k_EInputActionOrigin_Switch_LeftGyro_Roll = EInputActionOrigin(243)
k_EInputActionOrigin_Switch_LeftGrip_Lower = EInputActionOrigin(244)
k_EInputActionOrigin_Switch_LeftGrip_Upper = EInputActionOrigin(245)
k_EInputActionOrigin_Switch_RightGrip_Lower = EInputActionOrigin(246)
k_EInputActionOrigin_Switch_RightGrip_Upper = EInputActionOrigin(247)
k_EInputActionOrigin_Switch_Reserved11 = EInputActionOrigin(248)
k_EInputActionOrigin_Switch_Reserved12 = EInputActionOrigin(249)
k_EInputActionOrigin_Switch_Reserved13 = EInputActionOrigin(250)
k_EInputActionOrigin_Switch_Reserved14 = EInputActionOrigin(251)
k_EInputActionOrigin_Switch_Reserved15 = EInputActionOrigin(252)
k_EInputActionOrigin_Switch_Reserved16 = EInputActionOrigin(253)
k_EInputActionOrigin_Switch_Reserved17 = EInputActionOrigin(254)
k_EInputActionOrigin_Switch_Reserved18 = EInputActionOrigin(255)
k_EInputActionOrigin_Switch_Reserved19 = EInputActionOrigin(256)
k_EInputActionOrigin_Switch_Reserved20 = EInputActionOrigin(257)
k_EInputActionOrigin_PS5_X = EInputActionOrigin(258)
k_EInputActionOrigin_PS5_Circle = EInputActionOrigin(259)
k_EInputActionOrigin_PS5_Triangle = EInputActionOrigin(260)
k_EInputActionOrigin_PS5_Square = EInputActionOrigin(261)
k_EInputActionOrigin_PS5_LeftBumper = EInputActionOrigin(262)
k_EInputActionOrigin_PS5_RightBumper = EInputActionOrigin(263)
k_EInputActionOrigin_PS5_Option = EInputActionOrigin(264)
k_EInputActionOrigin_PS5_Create = EInputActionOrigin(265)
k_EInputActionOrigin_PS5_Mute = EInputActionOrigin(266)
k_EInputActionOrigin_PS5_LeftPad_Touch = EInputActionOrigin(267)
k_EInputActionOrigin_PS5_LeftPad_Swipe = EInputActionOrigin(268)
k_EInputActionOrigin_PS5_LeftPad_Click = EInputActionOrigin(269)
k_EInputActionOrigin_PS5_LeftPad_DPadNorth = EInputActionOrigin(270)
k_EInputActionOrigin_PS5_LeftPad_DPadSouth = EInputActionOrigin(271)
k_EInputActionOrigin_PS5_LeftPad_DPadWest = EInputActionOrigin(272)
k_EInputActionOrigin_PS5_LeftPad_DPadEast = EInputActionOrigin(273)
k_EInputActionOrigin_PS5_RightPad_Touch = EInputActionOrigin(274)
k_EInputActionOrigin_PS5_RightPad_Swipe = EInputActionOrigin(275)
k_EInputActionOrigin_PS5_RightPad_Click = EInputActionOrigin(276)
k_EInputActionOrigin_PS5_RightPad_DPadNorth = EInputActionOrigin(277)
k_EInputActionOrigin_PS5_RightPad_DPadSouth = EInputActionOrigin(278)
k_EInputActionOrigin_PS5_RightPad_DPadWest = EInputActionOrigin(279)
k_EInputActionOrigin_PS5_RightPad_DPadEast = EInputActionOrigin(280)
k_EInputActionOrigin_PS5_CenterPad_Touch = EInputActionOrigin(281)
k_EInputActionOrigin_PS5_CenterPad_Swipe = EInputActionOrigin(282)
k_EInputActionOrigin_PS5_CenterPad_Click = EInputActionOrigin(283)
k_EInputActionOrigin_PS5_CenterPad_DPadNorth = EInputActionOrigin(284)
k_EInputActionOrigin_PS5_CenterPad_DPadSouth = EInputActionOrigin(285)
k_EInputActionOrigin_PS5_CenterPad_DPadWest = EInputActionOrigin(286)
k_EInputActionOrigin_PS5_CenterPad_DPadEast = EInputActionOrigin(287)
k_EInputActionOrigin_PS5_LeftTrigger_Pull = EInputActionOrigin(288)
k_EInputActionOrigin_PS5_LeftTrigger_Click = EInputActionOrigin(289)
k_EInputActionOrigin_PS5_RightTrigger_Pull = EInputActionOrigin(290)
k_EInputActionOrigin_PS5_RightTrigger_Click = EInputActionOrigin(291)
k_EInputActionOrigin_PS5_LeftStick_Move = EInputActionOrigin(292)
k_EInputActionOrigin_PS5_LeftStick_Click = EInputActionOrigin(293)
k_EInputActionOrigin_PS5_LeftStick_DPadNorth = EInputActionOrigin(294)
k_EInputActionOrigin_PS5_LeftStick_DPadSouth = EInputActionOrigin(295)
k_EInputActionOrigin_PS5_LeftStick_DPadWest = EInputActionOrigin(296)
k_EInputActionOrigin_PS5_LeftStick_DPadEast = EInputActionOrigin(297)
k_EInputActionOrigin_PS5_RightStick_Move = EInputActionOrigin(298)
k_EInputActionOrigin_PS5_RightStick_Click = EInputActionOrigin(299)
k_EInputActionOrigin_PS5_RightStick_DPadNorth = EInputActionOrigin(300)
k_EInputActionOrigin_PS5_RightStick_DPadSouth = EInputActionOrigin(301)
k_EInputActionOrigin_PS5_RightStick_DPadWest = EInputActionOrigin(302)
k_EInputActionOrigin_PS5_RightStick_DPadEast = EInputActionOrigin(303)
k_EInputActionOrigin_PS5_DPad_North = EInputActionOrigin(304)
k_EInputActionOrigin_PS5_DPad_South = EInputActionOrigin(305)
k_EInputActionOrigin_PS5_DPad_West = EInputActionOrigin(306)
k_EInputActionOrigin_PS5_DPad_East = EInputActionOrigin(307)
k_EInputActionOrigin_PS5_Gyro_Move = EInputActionOrigin(308)
k_EInputActionOrigin_PS5_Gyro_Pitch = EInputActionOrigin(309)
k_EInputActionOrigin_PS5_Gyro_Yaw = EInputActionOrigin(310)
k_EInputActionOrigin_PS5_Gyro_Roll = EInputActionOrigin(311)
k_EInputActionOrigin_PS5_DPad_Move = EInputActionOrigin(312)
k_EInputActionOrigin_PS5_Reserved1 = EInputActionOrigin(313)
k_EInputActionOrigin_PS5_Reserved2 = EInputActionOrigin(314)
k_EInputActionOrigin_PS5_Reserved3 = EInputActionOrigin(315)
k_EInputActionOrigin_PS5_Reserved4 = EInputActionOrigin(316)
k_EInputActionOrigin_PS5_Reserved5 = EInputActionOrigin(317)
k_EInputActionOrigin_PS5_Reserved6 = EInputActionOrigin(318)
k_EInputActionOrigin_PS5_Reserved7 = EInputActionOrigin(319)
k_EInputActionOrigin_PS5_Reserved8 = EInputActionOrigin(320)
k_EInputActionOrigin_PS5_Reserved9 = EInputActionOrigin(321)
k_EInputActionOrigin_PS5_Reserved10 = EInputActionOrigin(322)
k_EInputActionOrigin_PS5_Reserved11 = EInputActionOrigin(323)
k_EInputActionOrigin_PS5_Reserved12 = EInputActionOrigin(324)
k_EInputActionOrigin_PS5_Reserved13 = EInputActionOrigin(325)
k_EInputActionOrigin_PS5_Reserved14 = EInputActionOrigin(326)
k_EInputActionOrigin_PS5_Reserved15 = EInputActionOrigin(327)
k_EInputActionOrigin_PS5_Reserved16 = EInputActionOrigin(328)
k_EInputActionOrigin_PS5_Reserved17 = EInputActionOrigin(329)
k_EInputActionOrigin_PS5_Reserved18 = EInputActionOrigin(330)
k_EInputActionOrigin_PS5_Reserved19 = EInputActionOrigin(331)
k_EInputActionOrigin_PS5_Reserved20 = EInputActionOrigin(332)
k_EInputActionOrigin_SteamDeck_A = EInputActionOrigin(333)
k_EInputActionOrigin_SteamDeck_B = EInputActionOrigin(334)
k_EInputActionOrigin_SteamDeck_X = EInputActionOrigin(335)
k_EInputActionOrigin_SteamDeck_Y = EInputActionOrigin(336)
k_EInputActionOrigin_SteamDeck_L1 = EInputActionOrigin(337)
k_EInputActionOrigin_SteamDeck_R1 = EInputActionOrigin(338)
k_EInputActionOrigin_SteamDeck_Menu = EInputActionOrigin(339)
k_EInputActionOrigin_SteamDeck_View = EInputActionOrigin(340)
k_EInputActionOrigin_SteamDeck_LeftPad_Touch = EInputActionOrigin(341)
k_EInputActionOrigin_SteamDeck_LeftPad_Swipe = EInputActionOrigin(342)
k_EInputActionOrigin_SteamDeck_LeftPad_Click = EInputActionOrigin(343)
k_EInputActionOrigin_SteamDeck_LeftPad_DPadNorth = EInputActionOrigin(344)
k_EInputActionOrigin_SteamDeck_LeftPad_DPadSouth = EInputActionOrigin(345)
k_EInputActionOrigin_SteamDeck_LeftPad_DPadWest = EInputActionOrigin(346)
k_EInputActionOrigin_SteamDeck_LeftPad_DPadEast = EInputActionOrigin(347)
k_EInputActionOrigin_SteamDeck_RightPad_Touch = EInputActionOrigin(348)
k_EInputActionOrigin_SteamDeck_RightPad_Swipe = EInputActionOrigin(349)
k_EInputActionOrigin_SteamDeck_RightPad_Click = EInputActionOrigin(350)
k_EInputActionOrigin_SteamDeck_RightPad_DPadNorth = EInputActionOrigin(351)
k_EInputActionOrigin_SteamDeck_RightPad_DPadSouth = EInputActionOrigin(352)
k_EInputActionOrigin_SteamDeck_RightPad_DPadWest = EInputActionOrigin(353)
k_EInputActionOrigin_SteamDeck_RightPad_DPadEast = EInputActionOrigin(354)
k_EInputActionOrigin_SteamDeck_L2_SoftPull = EInputActionOrigin(355)
k_EInputActionOrigin_SteamDeck_L2 = EInputActionOrigin(356)
k_EInputActionOrigin_SteamDeck_R2_SoftPull = EInputActionOrigin(357)
k_EInputActionOrigin_SteamDeck_R2 = EInputActionOrigin(358)
k_EInputActionOrigin_SteamDeck_LeftStick_Move = EInputActionOrigin(359)
k_EInputActionOrigin_SteamDeck_L3 = EInputActionOrigin(360)
k_EInputActionOrigin_SteamDeck_LeftStick_DPadNorth = EInputActionOrigin(361)
k_EInputActionOrigin_SteamDeck_LeftStick_DPadSouth = EInputActionOrigin(362)
k_EInputActionOrigin_SteamDeck_LeftStick_DPadWest = EInputActionOrigin(363)
k_EInputActionOrigin_SteamDeck_LeftStick_DPadEast = EInputActionOrigin(364)
k_EInputActionOrigin_SteamDeck_LeftStick_Touch = EInputActionOrigin(365)
k_EInputActionOrigin_SteamDeck_RightStick_Move = EInputActionOrigin(366)
k_EInputActionOrigin_SteamDeck_R3 = EInputActionOrigin(367)
k_EInputActionOrigin_SteamDeck_RightStick_DPadNorth = EInputActionOrigin(368)
k_EInputActionOrigin_SteamDeck_RightStick_DPadSouth = EInputActionOrigin(369)
k_EInputActionOrigin_SteamDeck_RightStick_DPadWest = EInputActionOrigin(370)
k_EInputActionOrigin_SteamDeck_RightStick_DPadEast = EInputActionOrigin(371)
k_EInputActionOrigin_SteamDeck_RightStick_Touch = EInputActionOrigin(372)
k_EInputActionOrigin_SteamDeck_L4 = EInputActionOrigin(373)
k_EInputActionOrigin_SteamDeck_R4 = EInputActionOrigin(374)
k_EInputActionOrigin_SteamDeck_L5 = EInputActionOrigin(375)
k_EInputActionOrigin_SteamDeck_R5 = EInputActionOrigin(376)
k_EInputActionOrigin_SteamDeck_DPad_Move = EInputActionOrigin(377)
k_EInputActionOrigin_SteamDeck_DPad_North = EInputActionOrigin(378)
k_EInputActionOrigin_SteamDeck_DPad_South = EInputActionOrigin(379)
k_EInputActionOrigin_SteamDeck_DPad_West = EInputActionOrigin(380)
k_EInputActionOrigin_SteamDeck_DPad_East = EInputActionOrigin(381)
k_EInputActionOrigin_SteamDeck_Gyro_Move = EInputActionOrigin(382)
k_EInputActionOrigin_SteamDeck_Gyro_Pitch = EInputActionOrigin(383)
k_EInputActionOrigin_SteamDeck_Gyro_Yaw = EInputActionOrigin(384)
k_EInputActionOrigin_SteamDeck_Gyro_Roll = EInputActionOrigin(385)
k_EInputActionOrigin_SteamDeck_Reserved1 = EInputActionOrigin(386)
k_EInputActionOrigin_SteamDeck_Reserved2 = EInputActionOrigin(387)
k_EInputActionOrigin_SteamDeck_Reserved3 = EInputActionOrigin(388)
k_EInputActionOrigin_SteamDeck_Reserved4 = EInputActionOrigin(389)
k_EInputActionOrigin_SteamDeck_Reserved5 = EInputActionOrigin(390)
k_EInputActionOrigin_SteamDeck_Reserved6 = EInputActionOrigin(391)
k_EInputActionOrigin_SteamDeck_Reserved7 = EInputActionOrigin(392)
k_EInputActionOrigin_SteamDeck_Reserved8 = EInputActionOrigin(393)
k_EInputActionOrigin_SteamDeck_Reserved9 = EInputActionOrigin(394)
k_EInputActionOrigin_SteamDeck_Reserved10 = EInputActionOrigin(395)
k_EInputActionOrigin_SteamDeck_Reserved11 = EInputActionOrigin(396)
k_EInputActionOrigin_SteamDeck_Reserved12 = EInputActionOrigin(397)
k_EInputActionOrigin_SteamDeck_Reserved13 = EInputActionOrigin(398)
k_EInputActionOrigin_SteamDeck_Reserved14 = EInputActionOrigin(399)
k_EInputActionOrigin_SteamDeck_Reserved15 = EInputActionOrigin(400)
k_EInputActionOrigin_SteamDeck_Reserved16 = EInputActionOrigin(401)
k_EInputActionOrigin_SteamDeck_Reserved17 = EInputActionOrigin(402)
k_EInputActionOrigin_SteamDeck_Reserved18 = EInputActionOrigin(403)
k_EInputActionOrigin_SteamDeck_Reserved19 = EInputActionOrigin(404)
k_EInputActionOrigin_SteamDeck_Reserved20 = EInputActionOrigin(405)
k_EInputActionOrigin_Count = EInputActionOrigin(406)
k_EInputActionOrigin_MaximumPossibleValue = EInputActionOrigin(32767)

class EXboxOrigin(c_int):
    pass

k_EXboxOrigin_A = EXboxOrigin(0)
k_EXboxOrigin_B = EXboxOrigin(1)
k_EXboxOrigin_X = EXboxOrigin(2)
k_EXboxOrigin_Y = EXboxOrigin(3)
k_EXboxOrigin_LeftBumper = EXboxOrigin(4)
k_EXboxOrigin_RightBumper = EXboxOrigin(5)
k_EXboxOrigin_Menu = EXboxOrigin(6)
k_EXboxOrigin_View = EXboxOrigin(7)
k_EXboxOrigin_LeftTrigger_Pull = EXboxOrigin(8)
k_EXboxOrigin_LeftTrigger_Click = EXboxOrigin(9)
k_EXboxOrigin_RightTrigger_Pull = EXboxOrigin(10)
k_EXboxOrigin_RightTrigger_Click = EXboxOrigin(11)
k_EXboxOrigin_LeftStick_Move = EXboxOrigin(12)
k_EXboxOrigin_LeftStick_Click = EXboxOrigin(13)
k_EXboxOrigin_LeftStick_DPadNorth = EXboxOrigin(14)
k_EXboxOrigin_LeftStick_DPadSouth = EXboxOrigin(15)
k_EXboxOrigin_LeftStick_DPadWest = EXboxOrigin(16)
k_EXboxOrigin_LeftStick_DPadEast = EXboxOrigin(17)
k_EXboxOrigin_RightStick_Move = EXboxOrigin(18)
k_EXboxOrigin_RightStick_Click = EXboxOrigin(19)
k_EXboxOrigin_RightStick_DPadNorth = EXboxOrigin(20)
k_EXboxOrigin_RightStick_DPadSouth = EXboxOrigin(21)
k_EXboxOrigin_RightStick_DPadWest = EXboxOrigin(22)
k_EXboxOrigin_RightStick_DPadEast = EXboxOrigin(23)
k_EXboxOrigin_DPad_North = EXboxOrigin(24)
k_EXboxOrigin_DPad_South = EXboxOrigin(25)
k_EXboxOrigin_DPad_West = EXboxOrigin(26)
k_EXboxOrigin_DPad_East = EXboxOrigin(27)
k_EXboxOrigin_Count = EXboxOrigin(28)

class ESteamControllerPad(c_int):
    pass

k_ESteamControllerPad_Left = ESteamControllerPad(0)
k_ESteamControllerPad_Right = ESteamControllerPad(1)

class EControllerHapticLocation(c_int):
    pass

k_EControllerHapticLocation_Left = EControllerHapticLocation(1)
k_EControllerHapticLocation_Right = EControllerHapticLocation(2)
k_EControllerHapticLocation_Both = EControllerHapticLocation(3)

class EControllerHapticType(c_int):
    pass

k_EControllerHapticType_Off = EControllerHapticType(0)
k_EControllerHapticType_Tick = EControllerHapticType(1)
k_EControllerHapticType_Click = EControllerHapticType(2)

class ESteamInputType(c_int):
    pass

k_ESteamInputType_Unknown = ESteamInputType(0)
k_ESteamInputType_SteamController = ESteamInputType(1)
k_ESteamInputType_XBox360Controller = ESteamInputType(2)
k_ESteamInputType_XBoxOneController = ESteamInputType(3)
k_ESteamInputType_GenericGamepad = ESteamInputType(4)
k_ESteamInputType_PS4Controller = ESteamInputType(5)
k_ESteamInputType_AppleMFiController = ESteamInputType(6)
k_ESteamInputType_AndroidController = ESteamInputType(7)
k_ESteamInputType_SwitchJoyConPair = ESteamInputType(8)
k_ESteamInputType_SwitchJoyConSingle = ESteamInputType(9)
k_ESteamInputType_SwitchProController = ESteamInputType(10)
k_ESteamInputType_MobileTouch = ESteamInputType(11)
k_ESteamInputType_PS3Controller = ESteamInputType(12)
k_ESteamInputType_PS5Controller = ESteamInputType(13)
k_ESteamInputType_SteamDeckController = ESteamInputType(14)
k_ESteamInputType_Count = ESteamInputType(15)
k_ESteamInputType_MaximumPossibleValue = ESteamInputType(255)

class ESteamInputConfigurationEnableType(c_int):
    pass

k_ESteamInputConfigurationEnableType_None = ESteamInputConfigurationEnableType(0)
k_ESteamInputConfigurationEnableType_Playstation = ESteamInputConfigurationEnableType(1)
k_ESteamInputConfigurationEnableType_Xbox = ESteamInputConfigurationEnableType(2)
k_ESteamInputConfigurationEnableType_Generic = ESteamInputConfigurationEnableType(4)
k_ESteamInputConfigurationEnableType_Switch = ESteamInputConfigurationEnableType(8)

class ESteamInputLEDFlag(c_int):
    pass

k_ESteamInputLEDFlag_SetColor = ESteamInputLEDFlag(0)
k_ESteamInputLEDFlag_RestoreUserDefault = ESteamInputLEDFlag(1)

class ESteamInputGlyphSize(c_int):
    pass

k_ESteamInputGlyphSize_Small = ESteamInputGlyphSize(0)
k_ESteamInputGlyphSize_Medium = ESteamInputGlyphSize(1)
k_ESteamInputGlyphSize_Large = ESteamInputGlyphSize(2)
k_ESteamInputGlyphSize_Count = ESteamInputGlyphSize(3)

class ESteamInputGlyphStyle(c_int):
    pass

ESteamInputGlyphStyle_Knockout = ESteamInputGlyphStyle(0)
ESteamInputGlyphStyle_Light = ESteamInputGlyphStyle(1)
ESteamInputGlyphStyle_Dark = ESteamInputGlyphStyle(2)
ESteamInputGlyphStyle_NeutralColorABXY = ESteamInputGlyphStyle(16)
ESteamInputGlyphStyle_SolidABXY = ESteamInputGlyphStyle(32)

class ESteamInputActionEventType(c_int):
    pass

ESteamInputActionEventType_DigitalAction = ESteamInputActionEventType(0)
ESteamInputActionEventType_AnalogAction = ESteamInputActionEventType(1)

class EControllerActionOrigin(c_int):
    pass

k_EControllerActionOrigin_None = EControllerActionOrigin(0)
k_EControllerActionOrigin_A = EControllerActionOrigin(1)
k_EControllerActionOrigin_B = EControllerActionOrigin(2)
k_EControllerActionOrigin_X = EControllerActionOrigin(3)
k_EControllerActionOrigin_Y = EControllerActionOrigin(4)
k_EControllerActionOrigin_LeftBumper = EControllerActionOrigin(5)
k_EControllerActionOrigin_RightBumper = EControllerActionOrigin(6)
k_EControllerActionOrigin_LeftGrip = EControllerActionOrigin(7)
k_EControllerActionOrigin_RightGrip = EControllerActionOrigin(8)
k_EControllerActionOrigin_Start = EControllerActionOrigin(9)
k_EControllerActionOrigin_Back = EControllerActionOrigin(10)
k_EControllerActionOrigin_LeftPad_Touch = EControllerActionOrigin(11)
k_EControllerActionOrigin_LeftPad_Swipe = EControllerActionOrigin(12)
k_EControllerActionOrigin_LeftPad_Click = EControllerActionOrigin(13)
k_EControllerActionOrigin_LeftPad_DPadNorth = EControllerActionOrigin(14)
k_EControllerActionOrigin_LeftPad_DPadSouth = EControllerActionOrigin(15)
k_EControllerActionOrigin_LeftPad_DPadWest = EControllerActionOrigin(16)
k_EControllerActionOrigin_LeftPad_DPadEast = EControllerActionOrigin(17)
k_EControllerActionOrigin_RightPad_Touch = EControllerActionOrigin(18)
k_EControllerActionOrigin_RightPad_Swipe = EControllerActionOrigin(19)
k_EControllerActionOrigin_RightPad_Click = EControllerActionOrigin(20)
k_EControllerActionOrigin_RightPad_DPadNorth = EControllerActionOrigin(21)
k_EControllerActionOrigin_RightPad_DPadSouth = EControllerActionOrigin(22)
k_EControllerActionOrigin_RightPad_DPadWest = EControllerActionOrigin(23)
k_EControllerActionOrigin_RightPad_DPadEast = EControllerActionOrigin(24)
k_EControllerActionOrigin_LeftTrigger_Pull = EControllerActionOrigin(25)
k_EControllerActionOrigin_LeftTrigger_Click = EControllerActionOrigin(26)
k_EControllerActionOrigin_RightTrigger_Pull = EControllerActionOrigin(27)
k_EControllerActionOrigin_RightTrigger_Click = EControllerActionOrigin(28)
k_EControllerActionOrigin_LeftStick_Move = EControllerActionOrigin(29)
k_EControllerActionOrigin_LeftStick_Click = EControllerActionOrigin(30)
k_EControllerActionOrigin_LeftStick_DPadNorth = EControllerActionOrigin(31)
k_EControllerActionOrigin_LeftStick_DPadSouth = EControllerActionOrigin(32)
k_EControllerActionOrigin_LeftStick_DPadWest = EControllerActionOrigin(33)
k_EControllerActionOrigin_LeftStick_DPadEast = EControllerActionOrigin(34)
k_EControllerActionOrigin_Gyro_Move = EControllerActionOrigin(35)
k_EControllerActionOrigin_Gyro_Pitch = EControllerActionOrigin(36)
k_EControllerActionOrigin_Gyro_Yaw = EControllerActionOrigin(37)
k_EControllerActionOrigin_Gyro_Roll = EControllerActionOrigin(38)
k_EControllerActionOrigin_PS4_X = EControllerActionOrigin(39)
k_EControllerActionOrigin_PS4_Circle = EControllerActionOrigin(40)
k_EControllerActionOrigin_PS4_Triangle = EControllerActionOrigin(41)
k_EControllerActionOrigin_PS4_Square = EControllerActionOrigin(42)
k_EControllerActionOrigin_PS4_LeftBumper = EControllerActionOrigin(43)
k_EControllerActionOrigin_PS4_RightBumper = EControllerActionOrigin(44)
k_EControllerActionOrigin_PS4_Options = EControllerActionOrigin(45)
k_EControllerActionOrigin_PS4_Share = EControllerActionOrigin(46)
k_EControllerActionOrigin_PS4_LeftPad_Touch = EControllerActionOrigin(47)
k_EControllerActionOrigin_PS4_LeftPad_Swipe = EControllerActionOrigin(48)
k_EControllerActionOrigin_PS4_LeftPad_Click = EControllerActionOrigin(49)
k_EControllerActionOrigin_PS4_LeftPad_DPadNorth = EControllerActionOrigin(50)
k_EControllerActionOrigin_PS4_LeftPad_DPadSouth = EControllerActionOrigin(51)
k_EControllerActionOrigin_PS4_LeftPad_DPadWest = EControllerActionOrigin(52)
k_EControllerActionOrigin_PS4_LeftPad_DPadEast = EControllerActionOrigin(53)
k_EControllerActionOrigin_PS4_RightPad_Touch = EControllerActionOrigin(54)
k_EControllerActionOrigin_PS4_RightPad_Swipe = EControllerActionOrigin(55)
k_EControllerActionOrigin_PS4_RightPad_Click = EControllerActionOrigin(56)
k_EControllerActionOrigin_PS4_RightPad_DPadNorth = EControllerActionOrigin(57)
k_EControllerActionOrigin_PS4_RightPad_DPadSouth = EControllerActionOrigin(58)
k_EControllerActionOrigin_PS4_RightPad_DPadWest = EControllerActionOrigin(59)
k_EControllerActionOrigin_PS4_RightPad_DPadEast = EControllerActionOrigin(60)
k_EControllerActionOrigin_PS4_CenterPad_Touch = EControllerActionOrigin(61)
k_EControllerActionOrigin_PS4_CenterPad_Swipe = EControllerActionOrigin(62)
k_EControllerActionOrigin_PS4_CenterPad_Click = EControllerActionOrigin(63)
k_EControllerActionOrigin_PS4_CenterPad_DPadNorth = EControllerActionOrigin(64)
k_EControllerActionOrigin_PS4_CenterPad_DPadSouth = EControllerActionOrigin(65)
k_EControllerActionOrigin_PS4_CenterPad_DPadWest = EControllerActionOrigin(66)
k_EControllerActionOrigin_PS4_CenterPad_DPadEast = EControllerActionOrigin(67)
k_EControllerActionOrigin_PS4_LeftTrigger_Pull = EControllerActionOrigin(68)
k_EControllerActionOrigin_PS4_LeftTrigger_Click = EControllerActionOrigin(69)
k_EControllerActionOrigin_PS4_RightTrigger_Pull = EControllerActionOrigin(70)
k_EControllerActionOrigin_PS4_RightTrigger_Click = EControllerActionOrigin(71)
k_EControllerActionOrigin_PS4_LeftStick_Move = EControllerActionOrigin(72)
k_EControllerActionOrigin_PS4_LeftStick_Click = EControllerActionOrigin(73)
k_EControllerActionOrigin_PS4_LeftStick_DPadNorth = EControllerActionOrigin(74)
k_EControllerActionOrigin_PS4_LeftStick_DPadSouth = EControllerActionOrigin(75)
k_EControllerActionOrigin_PS4_LeftStick_DPadWest = EControllerActionOrigin(76)
k_EControllerActionOrigin_PS4_LeftStick_DPadEast = EControllerActionOrigin(77)
k_EControllerActionOrigin_PS4_RightStick_Move = EControllerActionOrigin(78)
k_EControllerActionOrigin_PS4_RightStick_Click = EControllerActionOrigin(79)
k_EControllerActionOrigin_PS4_RightStick_DPadNorth = EControllerActionOrigin(80)
k_EControllerActionOrigin_PS4_RightStick_DPadSouth = EControllerActionOrigin(81)
k_EControllerActionOrigin_PS4_RightStick_DPadWest = EControllerActionOrigin(82)
k_EControllerActionOrigin_PS4_RightStick_DPadEast = EControllerActionOrigin(83)
k_EControllerActionOrigin_PS4_DPad_North = EControllerActionOrigin(84)
k_EControllerActionOrigin_PS4_DPad_South = EControllerActionOrigin(85)
k_EControllerActionOrigin_PS4_DPad_West = EControllerActionOrigin(86)
k_EControllerActionOrigin_PS4_DPad_East = EControllerActionOrigin(87)
k_EControllerActionOrigin_PS4_Gyro_Move = EControllerActionOrigin(88)
k_EControllerActionOrigin_PS4_Gyro_Pitch = EControllerActionOrigin(89)
k_EControllerActionOrigin_PS4_Gyro_Yaw = EControllerActionOrigin(90)
k_EControllerActionOrigin_PS4_Gyro_Roll = EControllerActionOrigin(91)
k_EControllerActionOrigin_XBoxOne_A = EControllerActionOrigin(92)
k_EControllerActionOrigin_XBoxOne_B = EControllerActionOrigin(93)
k_EControllerActionOrigin_XBoxOne_X = EControllerActionOrigin(94)
k_EControllerActionOrigin_XBoxOne_Y = EControllerActionOrigin(95)
k_EControllerActionOrigin_XBoxOne_LeftBumper = EControllerActionOrigin(96)
k_EControllerActionOrigin_XBoxOne_RightBumper = EControllerActionOrigin(97)
k_EControllerActionOrigin_XBoxOne_Menu = EControllerActionOrigin(98)
k_EControllerActionOrigin_XBoxOne_View = EControllerActionOrigin(99)
k_EControllerActionOrigin_XBoxOne_LeftTrigger_Pull = EControllerActionOrigin(100)
k_EControllerActionOrigin_XBoxOne_LeftTrigger_Click = EControllerActionOrigin(101)
k_EControllerActionOrigin_XBoxOne_RightTrigger_Pull = EControllerActionOrigin(102)
k_EControllerActionOrigin_XBoxOne_RightTrigger_Click = EControllerActionOrigin(103)
k_EControllerActionOrigin_XBoxOne_LeftStick_Move = EControllerActionOrigin(104)
k_EControllerActionOrigin_XBoxOne_LeftStick_Click = EControllerActionOrigin(105)
k_EControllerActionOrigin_XBoxOne_LeftStick_DPadNorth = EControllerActionOrigin(106)
k_EControllerActionOrigin_XBoxOne_LeftStick_DPadSouth = EControllerActionOrigin(107)
k_EControllerActionOrigin_XBoxOne_LeftStick_DPadWest = EControllerActionOrigin(108)
k_EControllerActionOrigin_XBoxOne_LeftStick_DPadEast = EControllerActionOrigin(109)
k_EControllerActionOrigin_XBoxOne_RightStick_Move = EControllerActionOrigin(110)
k_EControllerActionOrigin_XBoxOne_RightStick_Click = EControllerActionOrigin(111)
k_EControllerActionOrigin_XBoxOne_RightStick_DPadNorth = EControllerActionOrigin(112)
k_EControllerActionOrigin_XBoxOne_RightStick_DPadSouth = EControllerActionOrigin(113)
k_EControllerActionOrigin_XBoxOne_RightStick_DPadWest = EControllerActionOrigin(114)
k_EControllerActionOrigin_XBoxOne_RightStick_DPadEast = EControllerActionOrigin(115)
k_EControllerActionOrigin_XBoxOne_DPad_North = EControllerActionOrigin(116)
k_EControllerActionOrigin_XBoxOne_DPad_South = EControllerActionOrigin(117)
k_EControllerActionOrigin_XBoxOne_DPad_West = EControllerActionOrigin(118)
k_EControllerActionOrigin_XBoxOne_DPad_East = EControllerActionOrigin(119)
k_EControllerActionOrigin_XBox360_A = EControllerActionOrigin(120)
k_EControllerActionOrigin_XBox360_B = EControllerActionOrigin(121)
k_EControllerActionOrigin_XBox360_X = EControllerActionOrigin(122)
k_EControllerActionOrigin_XBox360_Y = EControllerActionOrigin(123)
k_EControllerActionOrigin_XBox360_LeftBumper = EControllerActionOrigin(124)
k_EControllerActionOrigin_XBox360_RightBumper = EControllerActionOrigin(125)
k_EControllerActionOrigin_XBox360_Start = EControllerActionOrigin(126)
k_EControllerActionOrigin_XBox360_Back = EControllerActionOrigin(127)
k_EControllerActionOrigin_XBox360_LeftTrigger_Pull = EControllerActionOrigin(128)
k_EControllerActionOrigin_XBox360_LeftTrigger_Click = EControllerActionOrigin(129)
k_EControllerActionOrigin_XBox360_RightTrigger_Pull = EControllerActionOrigin(130)
k_EControllerActionOrigin_XBox360_RightTrigger_Click = EControllerActionOrigin(131)
k_EControllerActionOrigin_XBox360_LeftStick_Move = EControllerActionOrigin(132)
k_EControllerActionOrigin_XBox360_LeftStick_Click = EControllerActionOrigin(133)
k_EControllerActionOrigin_XBox360_LeftStick_DPadNorth = EControllerActionOrigin(134)
k_EControllerActionOrigin_XBox360_LeftStick_DPadSouth = EControllerActionOrigin(135)
k_EControllerActionOrigin_XBox360_LeftStick_DPadWest = EControllerActionOrigin(136)
k_EControllerActionOrigin_XBox360_LeftStick_DPadEast = EControllerActionOrigin(137)
k_EControllerActionOrigin_XBox360_RightStick_Move = EControllerActionOrigin(138)
k_EControllerActionOrigin_XBox360_RightStick_Click = EControllerActionOrigin(139)
k_EControllerActionOrigin_XBox360_RightStick_DPadNorth = EControllerActionOrigin(140)
k_EControllerActionOrigin_XBox360_RightStick_DPadSouth = EControllerActionOrigin(141)
k_EControllerActionOrigin_XBox360_RightStick_DPadWest = EControllerActionOrigin(142)
k_EControllerActionOrigin_XBox360_RightStick_DPadEast = EControllerActionOrigin(143)
k_EControllerActionOrigin_XBox360_DPad_North = EControllerActionOrigin(144)
k_EControllerActionOrigin_XBox360_DPad_South = EControllerActionOrigin(145)
k_EControllerActionOrigin_XBox360_DPad_West = EControllerActionOrigin(146)
k_EControllerActionOrigin_XBox360_DPad_East = EControllerActionOrigin(147)
k_EControllerActionOrigin_SteamV2_A = EControllerActionOrigin(148)
k_EControllerActionOrigin_SteamV2_B = EControllerActionOrigin(149)
k_EControllerActionOrigin_SteamV2_X = EControllerActionOrigin(150)
k_EControllerActionOrigin_SteamV2_Y = EControllerActionOrigin(151)
k_EControllerActionOrigin_SteamV2_LeftBumper = EControllerActionOrigin(152)
k_EControllerActionOrigin_SteamV2_RightBumper = EControllerActionOrigin(153)
k_EControllerActionOrigin_SteamV2_LeftGrip_Lower = EControllerActionOrigin(154)
k_EControllerActionOrigin_SteamV2_LeftGrip_Upper = EControllerActionOrigin(155)
k_EControllerActionOrigin_SteamV2_RightGrip_Lower = EControllerActionOrigin(156)
k_EControllerActionOrigin_SteamV2_RightGrip_Upper = EControllerActionOrigin(157)
k_EControllerActionOrigin_SteamV2_LeftBumper_Pressure = EControllerActionOrigin(158)
k_EControllerActionOrigin_SteamV2_RightBumper_Pressure = EControllerActionOrigin(159)
k_EControllerActionOrigin_SteamV2_LeftGrip_Pressure = EControllerActionOrigin(160)
k_EControllerActionOrigin_SteamV2_RightGrip_Pressure = EControllerActionOrigin(161)
k_EControllerActionOrigin_SteamV2_LeftGrip_Upper_Pressure = EControllerActionOrigin(162)
k_EControllerActionOrigin_SteamV2_RightGrip_Upper_Pressure = EControllerActionOrigin(163)
k_EControllerActionOrigin_SteamV2_Start = EControllerActionOrigin(164)
k_EControllerActionOrigin_SteamV2_Back = EControllerActionOrigin(165)
k_EControllerActionOrigin_SteamV2_LeftPad_Touch = EControllerActionOrigin(166)
k_EControllerActionOrigin_SteamV2_LeftPad_Swipe = EControllerActionOrigin(167)
k_EControllerActionOrigin_SteamV2_LeftPad_Click = EControllerActionOrigin(168)
k_EControllerActionOrigin_SteamV2_LeftPad_Pressure = EControllerActionOrigin(169)
k_EControllerActionOrigin_SteamV2_LeftPad_DPadNorth = EControllerActionOrigin(170)
k_EControllerActionOrigin_SteamV2_LeftPad_DPadSouth = EControllerActionOrigin(171)
k_EControllerActionOrigin_SteamV2_LeftPad_DPadWest = EControllerActionOrigin(172)
k_EControllerActionOrigin_SteamV2_LeftPad_DPadEast = EControllerActionOrigin(173)
k_EControllerActionOrigin_SteamV2_RightPad_Touch = EControllerActionOrigin(174)
k_EControllerActionOrigin_SteamV2_RightPad_Swipe = EControllerActionOrigin(175)
k_EControllerActionOrigin_SteamV2_RightPad_Click = EControllerActionOrigin(176)
k_EControllerActionOrigin_SteamV2_RightPad_Pressure = EControllerActionOrigin(177)
k_EControllerActionOrigin_SteamV2_RightPad_DPadNorth = EControllerActionOrigin(178)
k_EControllerActionOrigin_SteamV2_RightPad_DPadSouth = EControllerActionOrigin(179)
k_EControllerActionOrigin_SteamV2_RightPad_DPadWest = EControllerActionOrigin(180)
k_EControllerActionOrigin_SteamV2_RightPad_DPadEast = EControllerActionOrigin(181)
k_EControllerActionOrigin_SteamV2_LeftTrigger_Pull = EControllerActionOrigin(182)
k_EControllerActionOrigin_SteamV2_LeftTrigger_Click = EControllerActionOrigin(183)
k_EControllerActionOrigin_SteamV2_RightTrigger_Pull = EControllerActionOrigin(184)
k_EControllerActionOrigin_SteamV2_RightTrigger_Click = EControllerActionOrigin(185)
k_EControllerActionOrigin_SteamV2_LeftStick_Move = EControllerActionOrigin(186)
k_EControllerActionOrigin_SteamV2_LeftStick_Click = EControllerActionOrigin(187)
k_EControllerActionOrigin_SteamV2_LeftStick_DPadNorth = EControllerActionOrigin(188)
k_EControllerActionOrigin_SteamV2_LeftStick_DPadSouth = EControllerActionOrigin(189)
k_EControllerActionOrigin_SteamV2_LeftStick_DPadWest = EControllerActionOrigin(190)
k_EControllerActionOrigin_SteamV2_LeftStick_DPadEast = EControllerActionOrigin(191)
k_EControllerActionOrigin_SteamV2_Gyro_Move = EControllerActionOrigin(192)
k_EControllerActionOrigin_SteamV2_Gyro_Pitch = EControllerActionOrigin(193)
k_EControllerActionOrigin_SteamV2_Gyro_Yaw = EControllerActionOrigin(194)
k_EControllerActionOrigin_SteamV2_Gyro_Roll = EControllerActionOrigin(195)
k_EControllerActionOrigin_Switch_A = EControllerActionOrigin(196)
k_EControllerActionOrigin_Switch_B = EControllerActionOrigin(197)
k_EControllerActionOrigin_Switch_X = EControllerActionOrigin(198)
k_EControllerActionOrigin_Switch_Y = EControllerActionOrigin(199)
k_EControllerActionOrigin_Switch_LeftBumper = EControllerActionOrigin(200)
k_EControllerActionOrigin_Switch_RightBumper = EControllerActionOrigin(201)
k_EControllerActionOrigin_Switch_Plus = EControllerActionOrigin(202)
k_EControllerActionOrigin_Switch_Minus = EControllerActionOrigin(203)
k_EControllerActionOrigin_Switch_Capture = EControllerActionOrigin(204)
k_EControllerActionOrigin_Switch_LeftTrigger_Pull = EControllerActionOrigin(205)
k_EControllerActionOrigin_Switch_LeftTrigger_Click = EControllerActionOrigin(206)
k_EControllerActionOrigin_Switch_RightTrigger_Pull = EControllerActionOrigin(207)
k_EControllerActionOrigin_Switch_RightTrigger_Click = EControllerActionOrigin(208)
k_EControllerActionOrigin_Switch_LeftStick_Move = EControllerActionOrigin(209)
k_EControllerActionOrigin_Switch_LeftStick_Click = EControllerActionOrigin(210)
k_EControllerActionOrigin_Switch_LeftStick_DPadNorth = EControllerActionOrigin(211)
k_EControllerActionOrigin_Switch_LeftStick_DPadSouth = EControllerActionOrigin(212)
k_EControllerActionOrigin_Switch_LeftStick_DPadWest = EControllerActionOrigin(213)
k_EControllerActionOrigin_Switch_LeftStick_DPadEast = EControllerActionOrigin(214)
k_EControllerActionOrigin_Switch_RightStick_Move = EControllerActionOrigin(215)
k_EControllerActionOrigin_Switch_RightStick_Click = EControllerActionOrigin(216)
k_EControllerActionOrigin_Switch_RightStick_DPadNorth = EControllerActionOrigin(217)
k_EControllerActionOrigin_Switch_RightStick_DPadSouth = EControllerActionOrigin(218)
k_EControllerActionOrigin_Switch_RightStick_DPadWest = EControllerActionOrigin(219)
k_EControllerActionOrigin_Switch_RightStick_DPadEast = EControllerActionOrigin(220)
k_EControllerActionOrigin_Switch_DPad_North = EControllerActionOrigin(221)
k_EControllerActionOrigin_Switch_DPad_South = EControllerActionOrigin(222)
k_EControllerActionOrigin_Switch_DPad_West = EControllerActionOrigin(223)
k_EControllerActionOrigin_Switch_DPad_East = EControllerActionOrigin(224)
k_EControllerActionOrigin_Switch_ProGyro_Move = EControllerActionOrigin(225)
k_EControllerActionOrigin_Switch_ProGyro_Pitch = EControllerActionOrigin(226)
k_EControllerActionOrigin_Switch_ProGyro_Yaw = EControllerActionOrigin(227)
k_EControllerActionOrigin_Switch_ProGyro_Roll = EControllerActionOrigin(228)
k_EControllerActionOrigin_Switch_RightGyro_Move = EControllerActionOrigin(229)
k_EControllerActionOrigin_Switch_RightGyro_Pitch = EControllerActionOrigin(230)
k_EControllerActionOrigin_Switch_RightGyro_Yaw = EControllerActionOrigin(231)
k_EControllerActionOrigin_Switch_RightGyro_Roll = EControllerActionOrigin(232)
k_EControllerActionOrigin_Switch_LeftGyro_Move = EControllerActionOrigin(233)
k_EControllerActionOrigin_Switch_LeftGyro_Pitch = EControllerActionOrigin(234)
k_EControllerActionOrigin_Switch_LeftGyro_Yaw = EControllerActionOrigin(235)
k_EControllerActionOrigin_Switch_LeftGyro_Roll = EControllerActionOrigin(236)
k_EControllerActionOrigin_Switch_LeftGrip_Lower = EControllerActionOrigin(237)
k_EControllerActionOrigin_Switch_LeftGrip_Upper = EControllerActionOrigin(238)
k_EControllerActionOrigin_Switch_RightGrip_Lower = EControllerActionOrigin(239)
k_EControllerActionOrigin_Switch_RightGrip_Upper = EControllerActionOrigin(240)
k_EControllerActionOrigin_PS4_DPad_Move = EControllerActionOrigin(241)
k_EControllerActionOrigin_XBoxOne_DPad_Move = EControllerActionOrigin(242)
k_EControllerActionOrigin_XBox360_DPad_Move = EControllerActionOrigin(243)
k_EControllerActionOrigin_Switch_DPad_Move = EControllerActionOrigin(244)
k_EControllerActionOrigin_PS5_X = EControllerActionOrigin(245)
k_EControllerActionOrigin_PS5_Circle = EControllerActionOrigin(246)
k_EControllerActionOrigin_PS5_Triangle = EControllerActionOrigin(247)
k_EControllerActionOrigin_PS5_Square = EControllerActionOrigin(248)
k_EControllerActionOrigin_PS5_LeftBumper = EControllerActionOrigin(249)
k_EControllerActionOrigin_PS5_RightBumper = EControllerActionOrigin(250)
k_EControllerActionOrigin_PS5_Option = EControllerActionOrigin(251)
k_EControllerActionOrigin_PS5_Create = EControllerActionOrigin(252)
k_EControllerActionOrigin_PS5_Mute = EControllerActionOrigin(253)
k_EControllerActionOrigin_PS5_LeftPad_Touch = EControllerActionOrigin(254)
k_EControllerActionOrigin_PS5_LeftPad_Swipe = EControllerActionOrigin(255)
k_EControllerActionOrigin_PS5_LeftPad_Click = EControllerActionOrigin(256)
k_EControllerActionOrigin_PS5_LeftPad_DPadNorth = EControllerActionOrigin(257)
k_EControllerActionOrigin_PS5_LeftPad_DPadSouth = EControllerActionOrigin(258)
k_EControllerActionOrigin_PS5_LeftPad_DPadWest = EControllerActionOrigin(259)
k_EControllerActionOrigin_PS5_LeftPad_DPadEast = EControllerActionOrigin(260)
k_EControllerActionOrigin_PS5_RightPad_Touch = EControllerActionOrigin(261)
k_EControllerActionOrigin_PS5_RightPad_Swipe = EControllerActionOrigin(262)
k_EControllerActionOrigin_PS5_RightPad_Click = EControllerActionOrigin(263)
k_EControllerActionOrigin_PS5_RightPad_DPadNorth = EControllerActionOrigin(264)
k_EControllerActionOrigin_PS5_RightPad_DPadSouth = EControllerActionOrigin(265)
k_EControllerActionOrigin_PS5_RightPad_DPadWest = EControllerActionOrigin(266)
k_EControllerActionOrigin_PS5_RightPad_DPadEast = EControllerActionOrigin(267)
k_EControllerActionOrigin_PS5_CenterPad_Touch = EControllerActionOrigin(268)
k_EControllerActionOrigin_PS5_CenterPad_Swipe = EControllerActionOrigin(269)
k_EControllerActionOrigin_PS5_CenterPad_Click = EControllerActionOrigin(270)
k_EControllerActionOrigin_PS5_CenterPad_DPadNorth = EControllerActionOrigin(271)
k_EControllerActionOrigin_PS5_CenterPad_DPadSouth = EControllerActionOrigin(272)
k_EControllerActionOrigin_PS5_CenterPad_DPadWest = EControllerActionOrigin(273)
k_EControllerActionOrigin_PS5_CenterPad_DPadEast = EControllerActionOrigin(274)
k_EControllerActionOrigin_PS5_LeftTrigger_Pull = EControllerActionOrigin(275)
k_EControllerActionOrigin_PS5_LeftTrigger_Click = EControllerActionOrigin(276)
k_EControllerActionOrigin_PS5_RightTrigger_Pull = EControllerActionOrigin(277)
k_EControllerActionOrigin_PS5_RightTrigger_Click = EControllerActionOrigin(278)
k_EControllerActionOrigin_PS5_LeftStick_Move = EControllerActionOrigin(279)
k_EControllerActionOrigin_PS5_LeftStick_Click = EControllerActionOrigin(280)
k_EControllerActionOrigin_PS5_LeftStick_DPadNorth = EControllerActionOrigin(281)
k_EControllerActionOrigin_PS5_LeftStick_DPadSouth = EControllerActionOrigin(282)
k_EControllerActionOrigin_PS5_LeftStick_DPadWest = EControllerActionOrigin(283)
k_EControllerActionOrigin_PS5_LeftStick_DPadEast = EControllerActionOrigin(284)
k_EControllerActionOrigin_PS5_RightStick_Move = EControllerActionOrigin(285)
k_EControllerActionOrigin_PS5_RightStick_Click = EControllerActionOrigin(286)
k_EControllerActionOrigin_PS5_RightStick_DPadNorth = EControllerActionOrigin(287)
k_EControllerActionOrigin_PS5_RightStick_DPadSouth = EControllerActionOrigin(288)
k_EControllerActionOrigin_PS5_RightStick_DPadWest = EControllerActionOrigin(289)
k_EControllerActionOrigin_PS5_RightStick_DPadEast = EControllerActionOrigin(290)
k_EControllerActionOrigin_PS5_DPad_Move = EControllerActionOrigin(291)
k_EControllerActionOrigin_PS5_DPad_North = EControllerActionOrigin(292)
k_EControllerActionOrigin_PS5_DPad_South = EControllerActionOrigin(293)
k_EControllerActionOrigin_PS5_DPad_West = EControllerActionOrigin(294)
k_EControllerActionOrigin_PS5_DPad_East = EControllerActionOrigin(295)
k_EControllerActionOrigin_PS5_Gyro_Move = EControllerActionOrigin(296)
k_EControllerActionOrigin_PS5_Gyro_Pitch = EControllerActionOrigin(297)
k_EControllerActionOrigin_PS5_Gyro_Yaw = EControllerActionOrigin(298)
k_EControllerActionOrigin_PS5_Gyro_Roll = EControllerActionOrigin(299)
k_EControllerActionOrigin_XBoxOne_LeftGrip_Lower = EControllerActionOrigin(300)
k_EControllerActionOrigin_XBoxOne_LeftGrip_Upper = EControllerActionOrigin(301)
k_EControllerActionOrigin_XBoxOne_RightGrip_Lower = EControllerActionOrigin(302)
k_EControllerActionOrigin_XBoxOne_RightGrip_Upper = EControllerActionOrigin(303)
k_EControllerActionOrigin_XBoxOne_Share = EControllerActionOrigin(304)
k_EControllerActionOrigin_SteamDeck_A = EControllerActionOrigin(305)
k_EControllerActionOrigin_SteamDeck_B = EControllerActionOrigin(306)
k_EControllerActionOrigin_SteamDeck_X = EControllerActionOrigin(307)
k_EControllerActionOrigin_SteamDeck_Y = EControllerActionOrigin(308)
k_EControllerActionOrigin_SteamDeck_L1 = EControllerActionOrigin(309)
k_EControllerActionOrigin_SteamDeck_R1 = EControllerActionOrigin(310)
k_EControllerActionOrigin_SteamDeck_Menu = EControllerActionOrigin(311)
k_EControllerActionOrigin_SteamDeck_View = EControllerActionOrigin(312)
k_EControllerActionOrigin_SteamDeck_LeftPad_Touch = EControllerActionOrigin(313)
k_EControllerActionOrigin_SteamDeck_LeftPad_Swipe = EControllerActionOrigin(314)
k_EControllerActionOrigin_SteamDeck_LeftPad_Click = EControllerActionOrigin(315)
k_EControllerActionOrigin_SteamDeck_LeftPad_DPadNorth = EControllerActionOrigin(316)
k_EControllerActionOrigin_SteamDeck_LeftPad_DPadSouth = EControllerActionOrigin(317)
k_EControllerActionOrigin_SteamDeck_LeftPad_DPadWest = EControllerActionOrigin(318)
k_EControllerActionOrigin_SteamDeck_LeftPad_DPadEast = EControllerActionOrigin(319)
k_EControllerActionOrigin_SteamDeck_RightPad_Touch = EControllerActionOrigin(320)
k_EControllerActionOrigin_SteamDeck_RightPad_Swipe = EControllerActionOrigin(321)
k_EControllerActionOrigin_SteamDeck_RightPad_Click = EControllerActionOrigin(322)
k_EControllerActionOrigin_SteamDeck_RightPad_DPadNorth = EControllerActionOrigin(323)
k_EControllerActionOrigin_SteamDeck_RightPad_DPadSouth = EControllerActionOrigin(324)
k_EControllerActionOrigin_SteamDeck_RightPad_DPadWest = EControllerActionOrigin(325)
k_EControllerActionOrigin_SteamDeck_RightPad_DPadEast = EControllerActionOrigin(326)
k_EControllerActionOrigin_SteamDeck_L2_SoftPull = EControllerActionOrigin(327)
k_EControllerActionOrigin_SteamDeck_L2 = EControllerActionOrigin(328)
k_EControllerActionOrigin_SteamDeck_R2_SoftPull = EControllerActionOrigin(329)
k_EControllerActionOrigin_SteamDeck_R2 = EControllerActionOrigin(330)
k_EControllerActionOrigin_SteamDeck_LeftStick_Move = EControllerActionOrigin(331)
k_EControllerActionOrigin_SteamDeck_L3 = EControllerActionOrigin(332)
k_EControllerActionOrigin_SteamDeck_LeftStick_DPadNorth = EControllerActionOrigin(333)
k_EControllerActionOrigin_SteamDeck_LeftStick_DPadSouth = EControllerActionOrigin(334)
k_EControllerActionOrigin_SteamDeck_LeftStick_DPadWest = EControllerActionOrigin(335)
k_EControllerActionOrigin_SteamDeck_LeftStick_DPadEast = EControllerActionOrigin(336)
k_EControllerActionOrigin_SteamDeck_LeftStick_Touch = EControllerActionOrigin(337)
k_EControllerActionOrigin_SteamDeck_RightStick_Move = EControllerActionOrigin(338)
k_EControllerActionOrigin_SteamDeck_R3 = EControllerActionOrigin(339)
k_EControllerActionOrigin_SteamDeck_RightStick_DPadNorth = EControllerActionOrigin(340)
k_EControllerActionOrigin_SteamDeck_RightStick_DPadSouth = EControllerActionOrigin(341)
k_EControllerActionOrigin_SteamDeck_RightStick_DPadWest = EControllerActionOrigin(342)
k_EControllerActionOrigin_SteamDeck_RightStick_DPadEast = EControllerActionOrigin(343)
k_EControllerActionOrigin_SteamDeck_RightStick_Touch = EControllerActionOrigin(344)
k_EControllerActionOrigin_SteamDeck_L4 = EControllerActionOrigin(345)
k_EControllerActionOrigin_SteamDeck_R4 = EControllerActionOrigin(346)
k_EControllerActionOrigin_SteamDeck_L5 = EControllerActionOrigin(347)
k_EControllerActionOrigin_SteamDeck_R5 = EControllerActionOrigin(348)
k_EControllerActionOrigin_SteamDeck_DPad_Move = EControllerActionOrigin(349)
k_EControllerActionOrigin_SteamDeck_DPad_North = EControllerActionOrigin(350)
k_EControllerActionOrigin_SteamDeck_DPad_South = EControllerActionOrigin(351)
k_EControllerActionOrigin_SteamDeck_DPad_West = EControllerActionOrigin(352)
k_EControllerActionOrigin_SteamDeck_DPad_East = EControllerActionOrigin(353)
k_EControllerActionOrigin_SteamDeck_Gyro_Move = EControllerActionOrigin(354)
k_EControllerActionOrigin_SteamDeck_Gyro_Pitch = EControllerActionOrigin(355)
k_EControllerActionOrigin_SteamDeck_Gyro_Yaw = EControllerActionOrigin(356)
k_EControllerActionOrigin_SteamDeck_Gyro_Roll = EControllerActionOrigin(357)
k_EControllerActionOrigin_SteamDeck_Reserved1 = EControllerActionOrigin(358)
k_EControllerActionOrigin_SteamDeck_Reserved2 = EControllerActionOrigin(359)
k_EControllerActionOrigin_SteamDeck_Reserved3 = EControllerActionOrigin(360)
k_EControllerActionOrigin_SteamDeck_Reserved4 = EControllerActionOrigin(361)
k_EControllerActionOrigin_SteamDeck_Reserved5 = EControllerActionOrigin(362)
k_EControllerActionOrigin_SteamDeck_Reserved6 = EControllerActionOrigin(363)
k_EControllerActionOrigin_SteamDeck_Reserved7 = EControllerActionOrigin(364)
k_EControllerActionOrigin_SteamDeck_Reserved8 = EControllerActionOrigin(365)
k_EControllerActionOrigin_SteamDeck_Reserved9 = EControllerActionOrigin(366)
k_EControllerActionOrigin_SteamDeck_Reserved10 = EControllerActionOrigin(367)
k_EControllerActionOrigin_SteamDeck_Reserved11 = EControllerActionOrigin(368)
k_EControllerActionOrigin_SteamDeck_Reserved12 = EControllerActionOrigin(369)
k_EControllerActionOrigin_SteamDeck_Reserved13 = EControllerActionOrigin(370)
k_EControllerActionOrigin_SteamDeck_Reserved14 = EControllerActionOrigin(371)
k_EControllerActionOrigin_SteamDeck_Reserved15 = EControllerActionOrigin(372)
k_EControllerActionOrigin_SteamDeck_Reserved16 = EControllerActionOrigin(373)
k_EControllerActionOrigin_SteamDeck_Reserved17 = EControllerActionOrigin(374)
k_EControllerActionOrigin_SteamDeck_Reserved18 = EControllerActionOrigin(375)
k_EControllerActionOrigin_SteamDeck_Reserved19 = EControllerActionOrigin(376)
k_EControllerActionOrigin_SteamDeck_Reserved20 = EControllerActionOrigin(377)
k_EControllerActionOrigin_Count = EControllerActionOrigin(378)
k_EControllerActionOrigin_MaximumPossibleValue = EControllerActionOrigin(32767)

class ESteamControllerLEDFlag(c_int):
    pass

k_ESteamControllerLEDFlag_SetColor = ESteamControllerLEDFlag(0)
k_ESteamControllerLEDFlag_RestoreUserDefault = ESteamControllerLEDFlag(1)

class EUGCMatchingUGCType(c_int):
    pass

k_EUGCMatchingUGCType_Items = EUGCMatchingUGCType(0)
k_EUGCMatchingUGCType_Items_Mtx = EUGCMatchingUGCType(1)
k_EUGCMatchingUGCType_Items_ReadyToUse = EUGCMatchingUGCType(2)
k_EUGCMatchingUGCType_Collections = EUGCMatchingUGCType(3)
k_EUGCMatchingUGCType_Artwork = EUGCMatchingUGCType(4)
k_EUGCMatchingUGCType_Videos = EUGCMatchingUGCType(5)
k_EUGCMatchingUGCType_Screenshots = EUGCMatchingUGCType(6)
k_EUGCMatchingUGCType_AllGuides = EUGCMatchingUGCType(7)
k_EUGCMatchingUGCType_WebGuides = EUGCMatchingUGCType(8)
k_EUGCMatchingUGCType_IntegratedGuides = EUGCMatchingUGCType(9)
k_EUGCMatchingUGCType_UsableInGame = EUGCMatchingUGCType(10)
k_EUGCMatchingUGCType_ControllerBindings = EUGCMatchingUGCType(11)
k_EUGCMatchingUGCType_GameManagedItems = EUGCMatchingUGCType(12)
k_EUGCMatchingUGCType_All = EUGCMatchingUGCType(-1)

class EUserUGCList(c_int):
    pass

k_EUserUGCList_Published = EUserUGCList(0)
k_EUserUGCList_VotedOn = EUserUGCList(1)
k_EUserUGCList_VotedUp = EUserUGCList(2)
k_EUserUGCList_VotedDown = EUserUGCList(3)
k_EUserUGCList_WillVoteLater = EUserUGCList(4)
k_EUserUGCList_Favorited = EUserUGCList(5)
k_EUserUGCList_Subscribed = EUserUGCList(6)
k_EUserUGCList_UsedOrPlayed = EUserUGCList(7)
k_EUserUGCList_Followed = EUserUGCList(8)

class EUserUGCListSortOrder(c_int):
    pass

k_EUserUGCListSortOrder_CreationOrderDesc = EUserUGCListSortOrder(0)
k_EUserUGCListSortOrder_CreationOrderAsc = EUserUGCListSortOrder(1)
k_EUserUGCListSortOrder_TitleAsc = EUserUGCListSortOrder(2)
k_EUserUGCListSortOrder_LastUpdatedDesc = EUserUGCListSortOrder(3)
k_EUserUGCListSortOrder_SubscriptionDateDesc = EUserUGCListSortOrder(4)
k_EUserUGCListSortOrder_VoteScoreDesc = EUserUGCListSortOrder(5)
k_EUserUGCListSortOrder_ForModeration = EUserUGCListSortOrder(6)

class EUGCQuery(c_int):
    pass

k_EUGCQuery_RankedByVote = EUGCQuery(0)
k_EUGCQuery_RankedByPublicationDate = EUGCQuery(1)
k_EUGCQuery_AcceptedForGameRankedByAcceptanceDate = EUGCQuery(2)
k_EUGCQuery_RankedByTrend = EUGCQuery(3)
k_EUGCQuery_FavoritedByFriendsRankedByPublicationDate = EUGCQuery(4)
k_EUGCQuery_CreatedByFriendsRankedByPublicationDate = EUGCQuery(5)
k_EUGCQuery_RankedByNumTimesReported = EUGCQuery(6)
k_EUGCQuery_CreatedByFollowedUsersRankedByPublicationDate = EUGCQuery(7)
k_EUGCQuery_NotYetRated = EUGCQuery(8)
k_EUGCQuery_RankedByTotalVotesAsc = EUGCQuery(9)
k_EUGCQuery_RankedByVotesUp = EUGCQuery(10)
k_EUGCQuery_RankedByTextSearch = EUGCQuery(11)
k_EUGCQuery_RankedByTotalUniqueSubscriptions = EUGCQuery(12)
k_EUGCQuery_RankedByPlaytimeTrend = EUGCQuery(13)
k_EUGCQuery_RankedByTotalPlaytime = EUGCQuery(14)
k_EUGCQuery_RankedByAveragePlaytimeTrend = EUGCQuery(15)
k_EUGCQuery_RankedByLifetimeAveragePlaytime = EUGCQuery(16)
k_EUGCQuery_RankedByPlaytimeSessionsTrend = EUGCQuery(17)
k_EUGCQuery_RankedByLifetimePlaytimeSessions = EUGCQuery(18)
k_EUGCQuery_RankedByLastUpdatedDate = EUGCQuery(19)

class EItemUpdateStatus(c_int):
    pass

k_EItemUpdateStatusInvalid = EItemUpdateStatus(0)
k_EItemUpdateStatusPreparingConfig = EItemUpdateStatus(1)
k_EItemUpdateStatusPreparingContent = EItemUpdateStatus(2)
k_EItemUpdateStatusUploadingContent = EItemUpdateStatus(3)
k_EItemUpdateStatusUploadingPreviewFile = EItemUpdateStatus(4)
k_EItemUpdateStatusCommittingChanges = EItemUpdateStatus(5)

class EItemState(c_int):
    pass

k_EItemStateNone = EItemState(0)
k_EItemStateSubscribed = EItemState(1)
k_EItemStateLegacyItem = EItemState(2)
k_EItemStateInstalled = EItemState(4)
k_EItemStateNeedsUpdate = EItemState(8)
k_EItemStateDownloading = EItemState(16)
k_EItemStateDownloadPending = EItemState(32)

class EItemStatistic(c_int):
    pass

k_EItemStatistic_NumSubscriptions = EItemStatistic(0)
k_EItemStatistic_NumFavorites = EItemStatistic(1)
k_EItemStatistic_NumFollowers = EItemStatistic(2)
k_EItemStatistic_NumUniqueSubscriptions = EItemStatistic(3)
k_EItemStatistic_NumUniqueFavorites = EItemStatistic(4)
k_EItemStatistic_NumUniqueFollowers = EItemStatistic(5)
k_EItemStatistic_NumUniqueWebsiteViews = EItemStatistic(6)
k_EItemStatistic_ReportScore = EItemStatistic(7)
k_EItemStatistic_NumSecondsPlayed = EItemStatistic(8)
k_EItemStatistic_NumPlaytimeSessions = EItemStatistic(9)
k_EItemStatistic_NumComments = EItemStatistic(10)
k_EItemStatistic_NumSecondsPlayedDuringTimePeriod = EItemStatistic(11)
k_EItemStatistic_NumPlaytimeSessionsDuringTimePeriod = EItemStatistic(12)

class EItemPreviewType(c_int):
    pass

k_EItemPreviewType_Image = EItemPreviewType(0)
k_EItemPreviewType_YouTubeVideo = EItemPreviewType(1)
k_EItemPreviewType_Sketchfab = EItemPreviewType(2)
k_EItemPreviewType_EnvironmentMap_HorizontalCross = EItemPreviewType(3)
k_EItemPreviewType_EnvironmentMap_LatLong = EItemPreviewType(4)
k_EItemPreviewType_ReservedMax = EItemPreviewType(255)

class ESteamItemFlags(c_int):
    pass

k_ESteamItemNoTrade = ESteamItemFlags(1)
k_ESteamItemRemoved = ESteamItemFlags(256)
k_ESteamItemConsumed = ESteamItemFlags(512)

class EParentalFeature(c_int):
    pass

k_EFeatureInvalid = EParentalFeature(0)
k_EFeatureStore = EParentalFeature(1)
k_EFeatureCommunity = EParentalFeature(2)
k_EFeatureProfile = EParentalFeature(3)
k_EFeatureFriends = EParentalFeature(4)
k_EFeatureNews = EParentalFeature(5)
k_EFeatureTrading = EParentalFeature(6)
k_EFeatureSettings = EParentalFeature(7)
k_EFeatureConsole = EParentalFeature(8)
k_EFeatureBrowser = EParentalFeature(9)
k_EFeatureParentalSetup = EParentalFeature(10)
k_EFeatureLibrary = EParentalFeature(11)
k_EFeatureTest = EParentalFeature(12)
k_EFeatureSiteLicense = EParentalFeature(13)
k_EFeatureMax = EParentalFeature(14)

class ESteamDeviceFormFactor(c_int):
    pass

k_ESteamDeviceFormFactorUnknown = ESteamDeviceFormFactor(0)
k_ESteamDeviceFormFactorPhone = ESteamDeviceFormFactor(1)
k_ESteamDeviceFormFactorTablet = ESteamDeviceFormFactor(2)
k_ESteamDeviceFormFactorComputer = ESteamDeviceFormFactor(3)
k_ESteamDeviceFormFactorTV = ESteamDeviceFormFactor(4)

class ESteamNetworkingAvailability(c_int):
    pass

k_ESteamNetworkingAvailability_CannotTry = ESteamNetworkingAvailability(-102)
k_ESteamNetworkingAvailability_Failed = ESteamNetworkingAvailability(-101)
k_ESteamNetworkingAvailability_Previously = ESteamNetworkingAvailability(-100)
k_ESteamNetworkingAvailability_Retrying = ESteamNetworkingAvailability(-10)
k_ESteamNetworkingAvailability_NeverTried = ESteamNetworkingAvailability(1)
k_ESteamNetworkingAvailability_Waiting = ESteamNetworkingAvailability(2)
k_ESteamNetworkingAvailability_Attempting = ESteamNetworkingAvailability(3)
k_ESteamNetworkingAvailability_Current = ESteamNetworkingAvailability(100)
k_ESteamNetworkingAvailability_Unknown = ESteamNetworkingAvailability(0)
k_ESteamNetworkingAvailability__Force32bit = ESteamNetworkingAvailability(2147483647)

class ESteamNetworkingIdentityType(c_int):
    pass

k_ESteamNetworkingIdentityType_Invalid = ESteamNetworkingIdentityType(0)
k_ESteamNetworkingIdentityType_SteamID = ESteamNetworkingIdentityType(16)
k_ESteamNetworkingIdentityType_XboxPairwiseID = ESteamNetworkingIdentityType(17)
k_ESteamNetworkingIdentityType_SonyPSN = ESteamNetworkingIdentityType(18)
k_ESteamNetworkingIdentityType_GoogleStadia = ESteamNetworkingIdentityType(19)
k_ESteamNetworkingIdentityType_IPAddress = ESteamNetworkingIdentityType(1)
k_ESteamNetworkingIdentityType_GenericString = ESteamNetworkingIdentityType(2)
k_ESteamNetworkingIdentityType_GenericBytes = ESteamNetworkingIdentityType(3)
k_ESteamNetworkingIdentityType_UnknownType = ESteamNetworkingIdentityType(4)
k_ESteamNetworkingIdentityType__Force32bit = ESteamNetworkingIdentityType(2147483647)

class ESteamNetworkingFakeIPType(c_int):
    pass

k_ESteamNetworkingFakeIPType_Invalid = ESteamNetworkingFakeIPType(0)
k_ESteamNetworkingFakeIPType_NotFake = ESteamNetworkingFakeIPType(1)
k_ESteamNetworkingFakeIPType_GlobalIPv4 = ESteamNetworkingFakeIPType(2)
k_ESteamNetworkingFakeIPType_LocalIPv4 = ESteamNetworkingFakeIPType(3)
k_ESteamNetworkingFakeIPType__Force32Bit = ESteamNetworkingFakeIPType(2147483647)

class ESteamNetworkingConnectionState(c_int):
    pass

k_ESteamNetworkingConnectionState_None = ESteamNetworkingConnectionState(0)
k_ESteamNetworkingConnectionState_Connecting = ESteamNetworkingConnectionState(1)
k_ESteamNetworkingConnectionState_FindingRoute = ESteamNetworkingConnectionState(2)
k_ESteamNetworkingConnectionState_Connected = ESteamNetworkingConnectionState(3)
k_ESteamNetworkingConnectionState_ClosedByPeer = ESteamNetworkingConnectionState(4)
k_ESteamNetworkingConnectionState_ProblemDetectedLocally = ESteamNetworkingConnectionState(5)
k_ESteamNetworkingConnectionState_FinWait = ESteamNetworkingConnectionState(-1)
k_ESteamNetworkingConnectionState_Linger = ESteamNetworkingConnectionState(-2)
k_ESteamNetworkingConnectionState_Dead = ESteamNetworkingConnectionState(-3)
k_ESteamNetworkingConnectionState__Force32Bit = ESteamNetworkingConnectionState(2147483647)

class ESteamNetConnectionEnd(c_int):
    pass

k_ESteamNetConnectionEnd_Invalid = ESteamNetConnectionEnd(0)
k_ESteamNetConnectionEnd_App_Min = ESteamNetConnectionEnd(1000)
k_ESteamNetConnectionEnd_App_Generic = ESteamNetConnectionEnd(1000)
k_ESteamNetConnectionEnd_App_Max = ESteamNetConnectionEnd(1999)
k_ESteamNetConnectionEnd_AppException_Min = ESteamNetConnectionEnd(2000)
k_ESteamNetConnectionEnd_AppException_Generic = ESteamNetConnectionEnd(2000)
k_ESteamNetConnectionEnd_AppException_Max = ESteamNetConnectionEnd(2999)
k_ESteamNetConnectionEnd_Local_Min = ESteamNetConnectionEnd(3000)
k_ESteamNetConnectionEnd_Local_OfflineMode = ESteamNetConnectionEnd(3001)
k_ESteamNetConnectionEnd_Local_ManyRelayConnectivity = ESteamNetConnectionEnd(3002)
k_ESteamNetConnectionEnd_Local_HostedServerPrimaryRelay = ESteamNetConnectionEnd(3003)
k_ESteamNetConnectionEnd_Local_NetworkConfig = ESteamNetConnectionEnd(3004)
k_ESteamNetConnectionEnd_Local_Rights = ESteamNetConnectionEnd(3005)
k_ESteamNetConnectionEnd_Local_P2P_ICE_NoPublicAddresses = ESteamNetConnectionEnd(3006)
k_ESteamNetConnectionEnd_Local_Max = ESteamNetConnectionEnd(3999)
k_ESteamNetConnectionEnd_Remote_Min = ESteamNetConnectionEnd(4000)
k_ESteamNetConnectionEnd_Remote_Timeout = ESteamNetConnectionEnd(4001)
k_ESteamNetConnectionEnd_Remote_BadCrypt = ESteamNetConnectionEnd(4002)
k_ESteamNetConnectionEnd_Remote_BadCert = ESteamNetConnectionEnd(4003)
k_ESteamNetConnectionEnd_Remote_BadProtocolVersion = ESteamNetConnectionEnd(4006)
k_ESteamNetConnectionEnd_Remote_P2P_ICE_NoPublicAddresses = ESteamNetConnectionEnd(4007)
k_ESteamNetConnectionEnd_Remote_Max = ESteamNetConnectionEnd(4999)
k_ESteamNetConnectionEnd_Misc_Min = ESteamNetConnectionEnd(5000)
k_ESteamNetConnectionEnd_Misc_Generic = ESteamNetConnectionEnd(5001)
k_ESteamNetConnectionEnd_Misc_InternalError = ESteamNetConnectionEnd(5002)
k_ESteamNetConnectionEnd_Misc_Timeout = ESteamNetConnectionEnd(5003)
k_ESteamNetConnectionEnd_Misc_SteamConnectivity = ESteamNetConnectionEnd(5005)
k_ESteamNetConnectionEnd_Misc_NoRelaySessionsToClient = ESteamNetConnectionEnd(5006)
k_ESteamNetConnectionEnd_Misc_P2P_Rendezvous = ESteamNetConnectionEnd(5008)
k_ESteamNetConnectionEnd_Misc_P2P_NAT_Firewall = ESteamNetConnectionEnd(5009)
k_ESteamNetConnectionEnd_Misc_PeerSentNoConnection = ESteamNetConnectionEnd(5010)
k_ESteamNetConnectionEnd_Misc_Max = ESteamNetConnectionEnd(5999)
k_ESteamNetConnectionEnd__Force32Bit = ESteamNetConnectionEnd(2147483647)

class ESteamNetworkingConfigScope(c_int):
    pass

k_ESteamNetworkingConfig_Global = ESteamNetworkingConfigScope(1)
k_ESteamNetworkingConfig_SocketsInterface = ESteamNetworkingConfigScope(2)
k_ESteamNetworkingConfig_ListenSocket = ESteamNetworkingConfigScope(3)
k_ESteamNetworkingConfig_Connection = ESteamNetworkingConfigScope(4)
k_ESteamNetworkingConfigScope__Force32Bit = ESteamNetworkingConfigScope(2147483647)

class ESteamNetworkingConfigDataType(c_int):
    pass

k_ESteamNetworkingConfig_Int32 = ESteamNetworkingConfigDataType(1)
k_ESteamNetworkingConfig_Int64 = ESteamNetworkingConfigDataType(2)
k_ESteamNetworkingConfig_Float = ESteamNetworkingConfigDataType(3)
k_ESteamNetworkingConfig_String = ESteamNetworkingConfigDataType(4)
k_ESteamNetworkingConfig_Ptr = ESteamNetworkingConfigDataType(5)
k_ESteamNetworkingConfigDataType__Force32Bit = ESteamNetworkingConfigDataType(2147483647)

class ESteamNetworkingConfigValue(c_int):
    pass

k_ESteamNetworkingConfig_Invalid = ESteamNetworkingConfigValue(0)
k_ESteamNetworkingConfig_TimeoutInitial = ESteamNetworkingConfigValue(24)
k_ESteamNetworkingConfig_TimeoutConnected = ESteamNetworkingConfigValue(25)
k_ESteamNetworkingConfig_SendBufferSize = ESteamNetworkingConfigValue(9)
k_ESteamNetworkingConfig_ConnectionUserData = ESteamNetworkingConfigValue(40)
k_ESteamNetworkingConfig_SendRateMin = ESteamNetworkingConfigValue(10)
k_ESteamNetworkingConfig_SendRateMax = ESteamNetworkingConfigValue(11)
k_ESteamNetworkingConfig_NagleTime = ESteamNetworkingConfigValue(12)
k_ESteamNetworkingConfig_IP_AllowWithoutAuth = ESteamNetworkingConfigValue(23)
k_ESteamNetworkingConfig_MTU_PacketSize = ESteamNetworkingConfigValue(32)
k_ESteamNetworkingConfig_MTU_DataSize = ESteamNetworkingConfigValue(33)
k_ESteamNetworkingConfig_Unencrypted = ESteamNetworkingConfigValue(34)
k_ESteamNetworkingConfig_SymmetricConnect = ESteamNetworkingConfigValue(37)
k_ESteamNetworkingConfig_LocalVirtualPort = ESteamNetworkingConfigValue(38)
k_ESteamNetworkingConfig_DualWifi_Enable = ESteamNetworkingConfigValue(39)
k_ESteamNetworkingConfig_EnableDiagnosticsUI = ESteamNetworkingConfigValue(46)
k_ESteamNetworkingConfig_FakePacketLoss_Send = ESteamNetworkingConfigValue(2)
k_ESteamNetworkingConfig_FakePacketLoss_Recv = ESteamNetworkingConfigValue(3)
k_ESteamNetworkingConfig_FakePacketLag_Send = ESteamNetworkingConfigValue(4)
k_ESteamNetworkingConfig_FakePacketLag_Recv = ESteamNetworkingConfigValue(5)
k_ESteamNetworkingConfig_FakePacketReorder_Send = ESteamNetworkingConfigValue(6)
k_ESteamNetworkingConfig_FakePacketReorder_Recv = ESteamNetworkingConfigValue(7)
k_ESteamNetworkingConfig_FakePacketReorder_Time = ESteamNetworkingConfigValue(8)
k_ESteamNetworkingConfig_FakePacketDup_Send = ESteamNetworkingConfigValue(26)
k_ESteamNetworkingConfig_FakePacketDup_Recv = ESteamNetworkingConfigValue(27)
k_ESteamNetworkingConfig_FakePacketDup_TimeMax = ESteamNetworkingConfigValue(28)
k_ESteamNetworkingConfig_PacketTraceMaxBytes = ESteamNetworkingConfigValue(41)
k_ESteamNetworkingConfig_FakeRateLimit_Send_Rate = ESteamNetworkingConfigValue(42)
k_ESteamNetworkingConfig_FakeRateLimit_Send_Burst = ESteamNetworkingConfigValue(43)
k_ESteamNetworkingConfig_FakeRateLimit_Recv_Rate = ESteamNetworkingConfigValue(44)
k_ESteamNetworkingConfig_FakeRateLimit_Recv_Burst = ESteamNetworkingConfigValue(45)
k_ESteamNetworkingConfig_Callback_ConnectionStatusChanged = ESteamNetworkingConfigValue(201)
k_ESteamNetworkingConfig_Callback_AuthStatusChanged = ESteamNetworkingConfigValue(202)
k_ESteamNetworkingConfig_Callback_RelayNetworkStatusChanged = ESteamNetworkingConfigValue(203)
k_ESteamNetworkingConfig_Callback_MessagesSessionRequest = ESteamNetworkingConfigValue(204)
k_ESteamNetworkingConfig_Callback_MessagesSessionFailed = ESteamNetworkingConfigValue(205)
k_ESteamNetworkingConfig_Callback_CreateConnectionSignaling = ESteamNetworkingConfigValue(206)
k_ESteamNetworkingConfig_Callback_FakeIPResult = ESteamNetworkingConfigValue(207)
k_ESteamNetworkingConfig_P2P_STUN_ServerList = ESteamNetworkingConfigValue(103)
k_ESteamNetworkingConfig_P2P_Transport_ICE_Enable = ESteamNetworkingConfigValue(104)
k_ESteamNetworkingConfig_P2P_Transport_ICE_Penalty = ESteamNetworkingConfigValue(105)
k_ESteamNetworkingConfig_P2P_Transport_SDR_Penalty = ESteamNetworkingConfigValue(106)
k_ESteamNetworkingConfig_SDRClient_ConsecutitivePingTimeoutsFailInitial = ESteamNetworkingConfigValue(19)
k_ESteamNetworkingConfig_SDRClient_ConsecutitivePingTimeoutsFail = ESteamNetworkingConfigValue(20)
k_ESteamNetworkingConfig_SDRClient_MinPingsBeforePingAccurate = ESteamNetworkingConfigValue(21)
k_ESteamNetworkingConfig_SDRClient_SingleSocket = ESteamNetworkingConfigValue(22)
k_ESteamNetworkingConfig_SDRClient_ForceRelayCluster = ESteamNetworkingConfigValue(29)
k_ESteamNetworkingConfig_SDRClient_DebugTicketAddress = ESteamNetworkingConfigValue(30)
k_ESteamNetworkingConfig_SDRClient_ForceProxyAddr = ESteamNetworkingConfigValue(31)
k_ESteamNetworkingConfig_SDRClient_FakeClusterPing = ESteamNetworkingConfigValue(36)
k_ESteamNetworkingConfig_LogLevel_AckRTT = ESteamNetworkingConfigValue(13)
k_ESteamNetworkingConfig_LogLevel_PacketDecode = ESteamNetworkingConfigValue(14)
k_ESteamNetworkingConfig_LogLevel_Message = ESteamNetworkingConfigValue(15)
k_ESteamNetworkingConfig_LogLevel_PacketGaps = ESteamNetworkingConfigValue(16)
k_ESteamNetworkingConfig_LogLevel_P2PRendezvous = ESteamNetworkingConfigValue(17)
k_ESteamNetworkingConfig_LogLevel_SDRRelayPings = ESteamNetworkingConfigValue(18)
k_ESteamNetworkingConfig_DELETED_EnumerateDevVars = ESteamNetworkingConfigValue(35)
k_ESteamNetworkingConfigValue__Force32Bit = ESteamNetworkingConfigValue(2147483647)

class ESteamNetworkingGetConfigValueResult(c_int):
    pass

k_ESteamNetworkingGetConfigValue_BadValue = ESteamNetworkingGetConfigValueResult(-1)
k_ESteamNetworkingGetConfigValue_BadScopeObj = ESteamNetworkingGetConfigValueResult(-2)
k_ESteamNetworkingGetConfigValue_BufferTooSmall = ESteamNetworkingGetConfigValueResult(-3)
k_ESteamNetworkingGetConfigValue_OK = ESteamNetworkingGetConfigValueResult(1)
k_ESteamNetworkingGetConfigValue_OKInherited = ESteamNetworkingGetConfigValueResult(2)
k_ESteamNetworkingGetConfigValueResult__Force32Bit = ESteamNetworkingGetConfigValueResult(2147483647)

class ESteamNetworkingSocketsDebugOutputType(c_int):
    pass

k_ESteamNetworkingSocketsDebugOutputType_None = ESteamNetworkingSocketsDebugOutputType(0)
k_ESteamNetworkingSocketsDebugOutputType_Bug = ESteamNetworkingSocketsDebugOutputType(1)
k_ESteamNetworkingSocketsDebugOutputType_Error = ESteamNetworkingSocketsDebugOutputType(2)
k_ESteamNetworkingSocketsDebugOutputType_Important = ESteamNetworkingSocketsDebugOutputType(3)
k_ESteamNetworkingSocketsDebugOutputType_Warning = ESteamNetworkingSocketsDebugOutputType(4)
k_ESteamNetworkingSocketsDebugOutputType_Msg = ESteamNetworkingSocketsDebugOutputType(5)
k_ESteamNetworkingSocketsDebugOutputType_Verbose = ESteamNetworkingSocketsDebugOutputType(6)
k_ESteamNetworkingSocketsDebugOutputType_Debug = ESteamNetworkingSocketsDebugOutputType(7)
k_ESteamNetworkingSocketsDebugOutputType_Everything = ESteamNetworkingSocketsDebugOutputType(8)
k_ESteamNetworkingSocketsDebugOutputType__Force32Bit = ESteamNetworkingSocketsDebugOutputType(2147483647)

class EServerMode(c_int):
    pass

eServerModeInvalid = EServerMode(0)
eServerModeNoAuthentication = EServerMode(1)
eServerModeAuthentication = EServerMode(2)
eServerModeAuthenticationAndSecure = EServerMode(3)


# Enums

class EFailureType(c_int):
    pass

k_EFailureFlushedCallbackQueue = EFailureType(0)
k_EFailurePipeFail = EFailureType(1)


# Enums

class PlayerAcceptState_t(c_int):
    pass

k_EStateUnknown = PlayerAcceptState_t(0)
k_EStatePlayerAccepted = PlayerAcceptState_t(1)
k_EStatePlayerDeclined = PlayerAcceptState_t(2)

class SteamIPAddress_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_rgubIPv6', (c_ubyte * 16)),
        ('m_eType', ESteamIPType),
    ]

    def t_IsSet(self, ):
        return SteamIPAddress_t_IsSet(byref(self), ) # type: ignore

class FriendGameInfo_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_gameID', c_ulonglong),
        ('m_unGameIP', c_uint),
        ('m_usGamePort', c_ushort),
        ('m_usQueryPort', c_ushort),
        ('m_steamIDLobby', c_ulonglong),
    ]

class MatchMakingKeyValuePair_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_szKey', (c_byte * 256)),
        ('m_szValue', (c_byte * 256)),
    ]

    def t_Construct(self, ):
        return MatchMakingKeyValuePair_t_Construct(byref(self), ) # type: ignore

class servernetadr_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_usConnectionPort', c_ushort),
        ('m_usQueryPort', c_ushort),
        ('m_unIP', c_uint),
    ]

    def t_Construct(self, ):
        return servernetadr_t_Construct(byref(self), ) # type: ignore

    def t_Init(self, ip, usQueryPort, usConnectionPort):
        return servernetadr_t_Init(byref(self), ip, usQueryPort, usConnectionPort) # type: ignore

    def t_GetQueryPort(self, ):
        return servernetadr_t_GetQueryPort(byref(self), ) # type: ignore

    def t_SetQueryPort(self, usPort):
        return servernetadr_t_SetQueryPort(byref(self), usPort) # type: ignore

    def t_GetConnectionPort(self, ):
        return servernetadr_t_GetConnectionPort(byref(self), ) # type: ignore

    def t_SetConnectionPort(self, usPort):
        return servernetadr_t_SetConnectionPort(byref(self), usPort) # type: ignore

    def t_GetIP(self, ):
        return servernetadr_t_GetIP(byref(self), ) # type: ignore

    def t_SetIP(self, unIP):
        return servernetadr_t_SetIP(byref(self), unIP) # type: ignore

    def t_GetConnectionAddressString(self, ):
        return servernetadr_t_GetConnectionAddressString(byref(self), ) # type: ignore

    def t_GetQueryAddressString(self, ):
        return servernetadr_t_GetQueryAddressString(byref(self), ) # type: ignore

    def t_IsLessThan(self, netadr):
        return servernetadr_t_IsLessThan(byref(self), netadr) # type: ignore

    def t_Assign(self, that):
        return servernetadr_t_Assign(byref(self), that) # type: ignore

class gameserveritem_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_NetAdr', servernetadr_t),
        ('m_nPing', c_int),
        ('m_bHadSuccessfulResponse', c_bool),
        ('m_bDoNotRefresh', c_bool),
        ('m_szGameDir', (c_byte * 32)),
        ('m_szMap', (c_byte * 32)),
        ('m_szGameDescription', (c_byte * 64)),
        ('m_nAppID', c_uint),
        ('m_nPlayers', c_int),
        ('m_nMaxPlayers', c_int),
        ('m_nBotPlayers', c_int),
        ('m_bPassword', c_bool),
        ('m_bSecure', c_bool),
        ('m_ulTimeLastPlayed', c_uint),
        ('m_nServerVersion', c_int),
        ('m_szServerName', (c_byte * 64)),
        ('m_szGameTags', (c_byte * 128)),
        ('m_steamID', c_ulonglong),
    ]

    def t_Construct(self, ):
        return gameserveritem_t_Construct(byref(self), ) # type: ignore

    def t_GetName(self, ):
        return gameserveritem_t_GetName(byref(self), ) # type: ignore

    def t_SetName(self, pName):
        return gameserveritem_t_SetName(byref(self), pName) # type: ignore

class SteamPartyBeaconLocation_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eType', ESteamPartyBeaconLocationType),
        ('m_ulLocationID', c_ulonglong),
    ]

class SteamParamStringArray_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ppStrings', POINTER(c_char_p)),
        ('m_nNumStrings', c_int),
    ]

class LeaderboardEntry_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDUser', c_ulonglong),
        ('m_nGlobalRank', c_int),
        ('m_nScore', c_int),
        ('m_cDetails', c_int),
        ('m_hUGC', c_ulonglong),
    ]

class P2PSessionState_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bConnectionActive', c_ubyte),
        ('m_bConnecting', c_ubyte),
        ('m_eP2PSessionError', c_ubyte),
        ('m_bUsingRelay', c_ubyte),
        ('m_nBytesQueuedForSend', c_int),
        ('m_nPacketsQueuedForSend', c_int),
        ('m_nRemoteIP', c_uint),
        ('m_nRemotePort', c_ushort),
    ]

class InputAnalogActionData_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('eMode', EInputSourceMode),
        ('x', c_float),
        ('y', c_float),
        ('bActive', c_bool),
    ]

class InputDigitalActionData_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('bState', c_bool),
        ('bActive', c_bool),
    ]

class InputMotionData_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('rotQuatX', c_float),
        ('rotQuatY', c_float),
        ('rotQuatZ', c_float),
        ('rotQuatW', c_float),
        ('posAccelX', c_float),
        ('posAccelY', c_float),
        ('posAccelZ', c_float),
        ('rotVelX', c_float),
        ('rotVelY', c_float),
        ('rotVelZ', c_float),
    ]

class SteamInputActionEvent_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('controllerHandle', c_ulonglong),
        ('eEventType', ESteamInputActionEventType),
    ]

class SteamUGCDetails_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eResult', EResult),
        ('m_eFileType', EWorkshopFileType),
        ('m_nCreatorAppID', c_uint),
        ('m_nConsumerAppID', c_uint),
        ('m_rgchTitle', (c_byte * 129)),
        ('m_rgchDescription', (c_byte * 8000)),
        ('m_ulSteamIDOwner', c_ulonglong),
        ('m_rtimeCreated', c_uint),
        ('m_rtimeUpdated', c_uint),
        ('m_rtimeAddedToUserList', c_uint),
        ('m_eVisibility', ERemoteStoragePublishedFileVisibility),
        ('m_bBanned', c_bool),
        ('m_bAcceptedForUse', c_bool),
        ('m_bTagsTruncated', c_bool),
        ('m_rgchTags', (c_byte * 1025)),
        ('m_hFile', c_ulonglong),
        ('m_hPreviewFile', c_ulonglong),
        ('m_pchFileName', (c_byte * 260)),
        ('m_nFileSize', c_int),
        ('m_nPreviewFileSize', c_int),
        ('m_rgchURL', (c_byte * 256)),
        ('m_unVotesUp', c_uint),
        ('m_unVotesDown', c_uint),
        ('m_flScore', c_float),
        ('m_unNumChildren', c_uint),
    ]

class SteamItemDetails_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_itemId', c_ulonglong),
        ('m_iDefinition', c_int),
        ('m_unQuantity', c_ushort),
        ('m_unFlags', c_ushort),
    ]

class SteamNetworkingIPAddr(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ipv6', (c_ubyte * 16)),
        ('m_port', c_ushort),
    ]

    def Clear(self, ):
        return SteamNetworkingIPAddr_Clear(byref(self), ) # type: ignore

    def IsIPv6AllZeros(self, ):
        return SteamNetworkingIPAddr_IsIPv6AllZeros(byref(self), ) # type: ignore

    def SetIPv6(self, ipv6, nPort):
        return SteamNetworkingIPAddr_SetIPv6(byref(self), ipv6, nPort) # type: ignore

    def SetIPv4(self, nIP, nPort):
        return SteamNetworkingIPAddr_SetIPv4(byref(self), nIP, nPort) # type: ignore

    def IsIPv4(self, ):
        return SteamNetworkingIPAddr_IsIPv4(byref(self), ) # type: ignore

    def GetIPv4(self, ):
        return SteamNetworkingIPAddr_GetIPv4(byref(self), ) # type: ignore

    def SetIPv6LocalHost(self, nPort):
        return SteamNetworkingIPAddr_SetIPv6LocalHost(byref(self), nPort) # type: ignore

    def IsLocalHost(self, ):
        return SteamNetworkingIPAddr_IsLocalHost(byref(self), ) # type: ignore

    def ToString(self, buf, cbBuf, bWithPort):
        return SteamNetworkingIPAddr_ToString(byref(self), buf, cbBuf, bWithPort) # type: ignore

    def ParseString(self, pszStr):
        return SteamNetworkingIPAddr_ParseString(byref(self), pszStr) # type: ignore

    def IsEqualTo(self, x):
        return SteamNetworkingIPAddr_IsEqualTo(byref(self), x) # type: ignore

    def GetFakeIPType(self, ):
        return SteamNetworkingIPAddr_GetFakeIPType(byref(self), ) # type: ignore

    def IsFakeIP(self, ):
        return SteamNetworkingIPAddr_IsFakeIP(byref(self), ) # type: ignore

class SteamNetworkingIdentity(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eType', ESteamNetworkingIdentityType),
        ('m_cbSize', c_int),
        ('m_szUnknownRawString', (c_byte * 128)),
    ]

    def Clear(self, ):
        return SteamNetworkingIdentity_Clear(byref(self), ) # type: ignore

    def IsInvalid(self, ):
        return SteamNetworkingIdentity_IsInvalid(byref(self), ) # type: ignore

    def SetSteamID(self, steamID):
        return SteamNetworkingIdentity_SetSteamID(byref(self), steamID) # type: ignore

    def GetSteamID(self, ):
        return SteamNetworkingIdentity_GetSteamID(byref(self), ) # type: ignore

    def SetSteamID64(self, steamID):
        return SteamNetworkingIdentity_SetSteamID64(byref(self), steamID) # type: ignore

    def GetSteamID64(self, ):
        return SteamNetworkingIdentity_GetSteamID64(byref(self), ) # type: ignore

    def SetXboxPairwiseID(self, pszString):
        return SteamNetworkingIdentity_SetXboxPairwiseID(byref(self), pszString) # type: ignore

    def GetXboxPairwiseID(self, ):
        return SteamNetworkingIdentity_GetXboxPairwiseID(byref(self), ) # type: ignore

    def SetPSNID(self, id):
        return SteamNetworkingIdentity_SetPSNID(byref(self), id) # type: ignore

    def GetPSNID(self, ):
        return SteamNetworkingIdentity_GetPSNID(byref(self), ) # type: ignore

    def SetStadiaID(self, id):
        return SteamNetworkingIdentity_SetStadiaID(byref(self), id) # type: ignore

    def GetStadiaID(self, ):
        return SteamNetworkingIdentity_GetStadiaID(byref(self), ) # type: ignore

    def SetIPAddr(self, addr):
        return SteamNetworkingIdentity_SetIPAddr(byref(self), addr) # type: ignore

    def GetIPAddr(self, ):
        return SteamNetworkingIdentity_GetIPAddr(byref(self), ) # type: ignore

    def SetIPv4Addr(self, nIPv4, nPort):
        return SteamNetworkingIdentity_SetIPv4Addr(byref(self), nIPv4, nPort) # type: ignore

    def GetIPv4(self, ):
        return SteamNetworkingIdentity_GetIPv4(byref(self), ) # type: ignore

    def GetFakeIPType(self, ):
        return SteamNetworkingIdentity_GetFakeIPType(byref(self), ) # type: ignore

    def IsFakeIP(self, ):
        return SteamNetworkingIdentity_IsFakeIP(byref(self), ) # type: ignore

    def SetLocalHost(self, ):
        return SteamNetworkingIdentity_SetLocalHost(byref(self), ) # type: ignore

    def IsLocalHost(self, ):
        return SteamNetworkingIdentity_IsLocalHost(byref(self), ) # type: ignore

    def SetGenericString(self, pszString):
        return SteamNetworkingIdentity_SetGenericString(byref(self), pszString) # type: ignore

    def GetGenericString(self, ):
        return SteamNetworkingIdentity_GetGenericString(byref(self), ) # type: ignore

    def SetGenericBytes(self, data, cbLen):
        return SteamNetworkingIdentity_SetGenericBytes(byref(self), data, cbLen) # type: ignore

    def GetGenericBytes(self, cbLen):
        return SteamNetworkingIdentity_GetGenericBytes(byref(self), cbLen) # type: ignore

    def IsEqualTo(self, x):
        return SteamNetworkingIdentity_IsEqualTo(byref(self), x) # type: ignore

    def ToString(self, buf, cbBuf):
        return SteamNetworkingIdentity_ToString(byref(self), buf, cbBuf) # type: ignore

    def ParseString(self, pszStr):
        return SteamNetworkingIdentity_ParseString(byref(self), pszStr) # type: ignore

class SteamNetConnectionInfo_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_identityRemote', SteamNetworkingIdentity),
        ('m_nUserData', c_longlong),
        ('m_hListenSocket', c_uint),
        ('m_addrRemote', SteamNetworkingIPAddr),
        ('m__pad1', c_ushort),
        ('m_idPOPRemote', c_uint),
        ('m_idPOPRelay', c_uint),
        ('m_eState', ESteamNetworkingConnectionState),
        ('m_eEndReason', c_int),
        ('m_szEndDebug', (c_byte * 128)),
        ('m_szConnectionDescription', (c_byte * 128)),
        ('m_nFlags', c_int),
        ('reserved', (c_uint * 63)),
    ]

class SteamNetConnectionRealTimeStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eState', ESteamNetworkingConnectionState),
        ('m_nPing', c_int),
        ('m_flConnectionQualityLocal', c_float),
        ('m_flConnectionQualityRemote', c_float),
        ('m_flOutPacketsPerSec', c_float),
        ('m_flOutBytesPerSec', c_float),
        ('m_flInPacketsPerSec', c_float),
        ('m_flInBytesPerSec', c_float),
        ('m_nSendRateBytesPerSecond', c_int),
        ('m_cbPendingUnreliable', c_int),
        ('m_cbPendingReliable', c_int),
        ('m_cbSentUnackedReliable', c_int),
        ('m_usecQueueTime', c_longlong),
        ('reserved', (c_uint * 16)),
    ]

class SteamNetConnectionRealTimeLaneStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_cbPendingUnreliable', c_int),
        ('m_cbPendingReliable', c_int),
        ('m_cbSentUnackedReliable', c_int),
        ('_reservePad1', c_int),
        ('m_usecQueueTime', c_longlong),
        ('reserved', (c_uint * 10)),
    ]

class SteamNetworkingMessage_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_pData', c_void_p),
        ('m_cbSize', c_int),
        ('m_conn', c_uint),
        ('m_identityPeer', SteamNetworkingIdentity),
        ('m_nConnUserData', c_longlong),
        ('m_usecTimeReceived', c_longlong),
        ('m_nMessageNumber', c_longlong),
        ('m_pfnFreeData', c_void_p),
        ('m_pfnRelease', c_void_p),
        ('m_nChannel', c_int),
        ('m_nFlags', c_int),
        ('m_nUserData', c_longlong),
        ('m_idxLane', c_ushort),
        ('_pad1__', c_ushort),
    ]

    def t_Release(self, ):
        return SteamNetworkingMessage_t_Release(byref(self), ) # type: ignore

class SteamNetworkPingLocation_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_data', (c_ubyte * 512)),
    ]

class SteamNetworkingConfigValue_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eValue', ESteamNetworkingConfigValue),
        ('m_eDataType', ESteamNetworkingConfigDataType),
        ('m_int64', c_longlong),
    ]

    def t_SetInt32(self, eVal, data):
        return SteamNetworkingConfigValue_t_SetInt32(byref(self), eVal, data) # type: ignore

    def t_SetInt64(self, eVal, data):
        return SteamNetworkingConfigValue_t_SetInt64(byref(self), eVal, data) # type: ignore

    def t_SetFloat(self, eVal, data):
        return SteamNetworkingConfigValue_t_SetFloat(byref(self), eVal, data) # type: ignore

    def t_SetPtr(self, eVal, data):
        return SteamNetworkingConfigValue_t_SetPtr(byref(self), eVal, data) # type: ignore

    def t_SetString(self, eVal, data):
        return SteamNetworkingConfigValue_t_SetString(byref(self), eVal, data) # type: ignore

class SteamDatagramHostedAddress(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_cbSize', c_int),
        ('m_data', (c_byte * 128)),
    ]

    def Clear(self, ):
        return SteamDatagramHostedAddress_Clear(byref(self), ) # type: ignore

    def GetPopID(self, ):
        return SteamDatagramHostedAddress_GetPopID(byref(self), ) # type: ignore

    def SetDevAddress(self, nIP, nPort, popid):
        return SteamDatagramHostedAddress_SetDevAddress(byref(self), nIP, nPort, popid) # type: ignore

class SteamDatagramGameCoordinatorServerLogin(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_identity', SteamNetworkingIdentity),
        ('m_routing', SteamDatagramHostedAddress),
        ('m_nAppID', c_uint),
        ('m_rtime', c_uint),
        ('m_cbAppData', c_int),
        ('m_appData', (c_byte * 2048)),
    ]

class SteamServersConnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 101

class SteamServerConnectFailure_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_bStillRetrying', c_bool),
    ]
    callback_id = 102

class SteamServersDisconnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 103

class ClientGameServerDeny_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_uAppID', c_uint),
        ('m_unGameServerIP', c_uint),
        ('m_usGameServerPort', c_ushort),
        ('m_bSecure', c_ushort),
        ('m_uReason', c_uint),
    ]
    callback_id = 113

class IPCFailure_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eFailureType', c_ubyte),
    ]
    callback_id = 117

class LicensesUpdated_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 125

class ValidateAuthTicketResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamID', c_ulonglong),
        ('m_eAuthSessionResponse', EAuthSessionResponse),
        ('m_OwnerSteamID', c_ulonglong),
    ]
    callback_id = 143

class MicroTxnAuthorizationResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unAppID', c_uint),
        ('m_ulOrderID', c_ulonglong),
        ('m_bAuthorized', c_ubyte),
    ]
    callback_id = 152

class EncryptedAppTicketResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 154

class GetAuthSessionTicketResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hAuthTicket', c_uint),
        ('m_eResult', EResult),
    ]
    callback_id = 163

class GameWebCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_szURL', (c_byte * 256)),
    ]
    callback_id = 164

class StoreAuthURLResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_szURL', (c_byte * 512)),
    ]
    callback_id = 165

class MarketEligibilityResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bAllowed', c_bool),
        ('m_eNotAllowedReason', EMarketNotAllowedReasonFlags),
        ('m_rtAllowedAtTime', c_uint),
        ('m_cdaySteamGuardRequiredDays', c_int),
        ('m_cdayNewDeviceCooldown', c_int),
    ]
    callback_id = 166

class DurationControl_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_appid', c_uint),
        ('m_bApplicable', c_bool),
        ('m_csecsLast5h', c_int),
        ('m_progress', EDurationControlProgress),
        ('m_notification', EDurationControlNotification),
        ('m_csecsToday', c_int),
        ('m_csecsRemaining', c_int),
    ]
    callback_id = 167

class PersonaStateChange_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamID', c_ulonglong),
        ('m_nChangeFlags', c_int),
    ]
    callback_id = 304

class GameOverlayActivated_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bActive', c_ubyte),
    ]
    callback_id = 331

class GameServerChangeRequested_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_rgchServer', (c_byte * 64)),
        ('m_rgchPassword', (c_byte * 64)),
    ]
    callback_id = 332

class GameLobbyJoinRequested_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDLobby', c_ulonglong),
        ('m_steamIDFriend', c_ulonglong),
    ]
    callback_id = 333

class AvatarImageLoaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamID', c_ulonglong),
        ('m_iImage', c_int),
        ('m_iWide', c_int),
        ('m_iTall', c_int),
    ]
    callback_id = 334

class ClanOfficerListResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDClan', c_ulonglong),
        ('m_cOfficers', c_int),
        ('m_bSuccess', c_ubyte),
    ]
    callback_id = 335

class FriendRichPresenceUpdate_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDFriend', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 336

class GameRichPresenceJoinRequested_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDFriend', c_ulonglong),
        ('m_rgchConnect', (c_byte * 256)),
    ]
    callback_id = 337

class GameConnectedClanChatMsg_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDClanChat', c_ulonglong),
        ('m_steamIDUser', c_ulonglong),
        ('m_iMessageID', c_int),
    ]
    callback_id = 338

class GameConnectedChatJoin_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDClanChat', c_ulonglong),
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 339

class GameConnectedChatLeave_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDClanChat', c_ulonglong),
        ('m_steamIDUser', c_ulonglong),
        ('m_bKicked', c_bool),
        ('m_bDropped', c_bool),
    ]
    callback_id = 340

class DownloadClanActivityCountsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSuccess', c_bool),
    ]
    callback_id = 341

class JoinClanChatRoomCompletionResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDClanChat', c_ulonglong),
        ('m_eChatRoomEnterResponse', EChatRoomEnterResponse),
    ]
    callback_id = 342

class GameConnectedFriendChatMsg_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDUser', c_ulonglong),
        ('m_iMessageID', c_int),
    ]
    callback_id = 343

class FriendsGetFollowerCount_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_steamID', c_ulonglong),
        ('m_nCount', c_int),
    ]
    callback_id = 344

class FriendsIsFollowing_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_steamID', c_ulonglong),
        ('m_bIsFollowing', c_bool),
    ]
    callback_id = 345

class FriendsEnumerateFollowingList_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_rgSteamID', (c_ulonglong * 50)),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
    ]
    callback_id = 346

class SetPersonaNameResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSuccess', c_bool),
        ('m_bLocalSuccess', c_bool),
        ('m_result', EResult),
    ]
    callback_id = 347

class UnreadChatMessagesChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 348

class OverlayBrowserProtocolNavigation_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('rgchURI', (c_byte * 1024)),
    ]
    callback_id = 349

class IPCountry_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 701

class LowBatteryPower_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nMinutesBatteryLeft', c_ubyte),
    ]
    callback_id = 702

class SteamAPICallCompleted_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hAsyncCall', c_ulonglong),
        ('m_iCallback', c_int),
        ('m_cubParam', c_uint),
    ]
    callback_id = 703

class SteamShutdown_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 704

class CheckFileSignature_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eCheckFileSignature', ECheckFileSignature),
    ]
    callback_id = 705

class GamepadTextInputDismissed_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSubmitted', c_bool),
        ('m_unSubmittedText', c_uint),
    ]
    callback_id = 714

class AppResumingFromSuspend_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 736

class FloatingGamepadTextInputDismissed_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 738

class FavoritesListChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nIP', c_uint),
        ('m_nQueryPort', c_uint),
        ('m_nConnPort', c_uint),
        ('m_nAppID', c_uint),
        ('m_nFlags', c_uint),
        ('m_bAdd', c_bool),
        ('m_unAccountId', c_uint),
    ]
    callback_id = 502

class LobbyInvite_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDUser', c_ulonglong),
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulGameID', c_ulonglong),
    ]
    callback_id = 503

class LobbyEnter_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_rgfChatPermissions', c_uint),
        ('m_bLocked', c_bool),
        ('m_EChatRoomEnterResponse', c_uint),
    ]
    callback_id = 504

class LobbyDataUpdate_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulSteamIDMember', c_ulonglong),
        ('m_bSuccess', c_ubyte),
    ]
    callback_id = 505

class LobbyChatUpdate_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulSteamIDUserChanged', c_ulonglong),
        ('m_ulSteamIDMakingChange', c_ulonglong),
        ('m_rgfChatMemberStateChange', c_uint),
    ]
    callback_id = 506

class LobbyChatMsg_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulSteamIDUser', c_ulonglong),
        ('m_eChatEntryType', c_ubyte),
        ('m_iChatID', c_uint),
    ]
    callback_id = 507

class LobbyGameCreated_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulSteamIDGameServer', c_ulonglong),
        ('m_unIP', c_uint),
        ('m_usPort', c_ushort),
    ]
    callback_id = 509

class LobbyMatchList_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nLobbiesMatching', c_uint),
    ]
    callback_id = 510

class LobbyKicked_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulSteamIDLobby', c_ulonglong),
        ('m_ulSteamIDAdmin', c_ulonglong),
        ('m_bKickedDueToDisconnect', c_ubyte),
    ]
    callback_id = 512

class LobbyCreated_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ulSteamIDLobby', c_ulonglong),
    ]
    callback_id = 513

class PSNGameBootInviteResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bGameBootInviteExists', c_bool),
        ('m_steamIDLobby', c_ulonglong),
    ]
    callback_id = 515

class FavoritesListAccountsUpdated_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 516

class SearchForGameProgressCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ullSearchID', c_ulonglong),
        ('m_eResult', EResult),
        ('m_lobbyID', c_ulonglong),
        ('m_steamIDEndedSearch', c_ulonglong),
        ('m_nSecondsRemainingEstimate', c_int),
        ('m_cPlayersSearching', c_int),
    ]
    callback_id = 5201

class SearchForGameResultCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ullSearchID', c_ulonglong),
        ('m_eResult', EResult),
        ('m_nCountPlayersInGame', c_int),
        ('m_nCountAcceptedGame', c_int),
        ('m_steamIDHost', c_ulonglong),
        ('m_bFinalCallback', c_bool),
    ]
    callback_id = 5202

class RequestPlayersForGameProgressCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ullSearchID', c_ulonglong),
    ]
    callback_id = 5211

class RequestPlayersForGameResultCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ullSearchID', c_ulonglong),
        ('m_SteamIDPlayerFound', c_ulonglong),
        ('m_SteamIDLobby', c_ulonglong),
        ('m_ePlayerAcceptState', PlayerAcceptState_t),
        ('m_nPlayerIndex', c_int),
        ('m_nTotalPlayersFound', c_int),
        ('m_nTotalPlayersAcceptedGame', c_int),
        ('m_nSuggestedTeamIndex', c_int),
        ('m_ullUniqueGameID', c_ulonglong),
    ]
    callback_id = 5212

class RequestPlayersForGameFinalResultCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ullSearchID', c_ulonglong),
        ('m_ullUniqueGameID', c_ulonglong),
    ]
    callback_id = 5213

class SubmitPlayerResultResultCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('ullUniqueGameID', c_ulonglong),
        ('steamIDPlayer', c_ulonglong),
    ]
    callback_id = 5214

class EndGameResultCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('ullUniqueGameID', c_ulonglong),
    ]
    callback_id = 5215

class JoinPartyCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ulBeaconID', c_ulonglong),
        ('m_SteamIDBeaconOwner', c_ulonglong),
        ('m_rgchConnectString', (c_byte * 256)),
    ]
    callback_id = 5301

class CreateBeaconCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ulBeaconID', c_ulonglong),
    ]
    callback_id = 5302

class ReservationNotificationCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulBeaconID', c_ulonglong),
        ('m_steamIDJoiner', c_ulonglong),
    ]
    callback_id = 5303

class ChangeNumOpenSlotsCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 5304

class AvailableBeaconLocationsUpdated_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 5305

class ActiveBeaconsUpdated_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 5306

class RemoteStorageFileShareResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_hFile', c_ulonglong),
        ('m_rgchFilename', (c_byte * 260)),
    ]
    callback_id = 1307

class RemoteStoragePublishFileResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_bUserNeedsToAcceptWorkshopLegalAgreement', c_bool),
    ]
    callback_id = 1309

class RemoteStorageDeletePublishedFileResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 1311

class RemoteStorageEnumerateUserPublishedFilesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
        ('m_rgPublishedFileId', (c_ulonglong * 50)),
    ]
    callback_id = 1312

class RemoteStorageSubscribePublishedFileResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 1313

class RemoteStorageEnumerateUserSubscribedFilesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
        ('m_rgPublishedFileId', (c_ulonglong * 50)),
        ('m_rgRTimeSubscribed', (c_uint * 50)),
    ]
    callback_id = 1314

class RemoteStorageUnsubscribePublishedFileResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 1315

class RemoteStorageUpdatePublishedFileResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_bUserNeedsToAcceptWorkshopLegalAgreement', c_bool),
    ]
    callback_id = 1316

class RemoteStorageDownloadUGCResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_hFile', c_ulonglong),
        ('m_nAppID', c_uint),
        ('m_nSizeInBytes', c_int),
        ('m_pchFileName', (c_byte * 260)),
        ('m_ulSteamIDOwner', c_ulonglong),
    ]
    callback_id = 1317

class RemoteStorageGetPublishedFileDetailsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nCreatorAppID', c_uint),
        ('m_nConsumerAppID', c_uint),
        ('m_rgchTitle', (c_byte * 129)),
        ('m_rgchDescription', (c_byte * 8000)),
        ('m_hFile', c_ulonglong),
        ('m_hPreviewFile', c_ulonglong),
        ('m_ulSteamIDOwner', c_ulonglong),
        ('m_rtimeCreated', c_uint),
        ('m_rtimeUpdated', c_uint),
        ('m_eVisibility', ERemoteStoragePublishedFileVisibility),
        ('m_bBanned', c_bool),
        ('m_rgchTags', (c_byte * 1025)),
        ('m_bTagsTruncated', c_bool),
        ('m_pchFileName', (c_byte * 260)),
        ('m_nFileSize', c_int),
        ('m_nPreviewFileSize', c_int),
        ('m_rgchURL', (c_byte * 256)),
        ('m_eFileType', EWorkshopFileType),
        ('m_bAcceptedForUse', c_bool),
    ]
    callback_id = 1318

class RemoteStorageEnumerateWorkshopFilesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
        ('m_rgPublishedFileId', (c_ulonglong * 50)),
        ('m_rgScore', (c_float * 50)),
        ('m_nAppId', c_uint),
        ('m_unStartIndex', c_uint),
    ]
    callback_id = 1319

class RemoteStorageGetPublishedItemVoteDetailsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_unPublishedFileId', c_ulonglong),
        ('m_nVotesFor', c_int),
        ('m_nVotesAgainst', c_int),
        ('m_nReports', c_int),
        ('m_fScore', c_float),
    ]
    callback_id = 1320

class RemoteStoragePublishedFileSubscribed_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 1321

class RemoteStoragePublishedFileUnsubscribed_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 1322

class RemoteStoragePublishedFileDeleted_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 1323

class RemoteStorageUpdateUserPublishedItemVoteResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 1324

class RemoteStorageUserVoteDetails_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eVote', EWorkshopVote),
    ]
    callback_id = 1325

class RemoteStorageEnumerateUserSharedWorkshopFilesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
        ('m_rgPublishedFileId', (c_ulonglong * 50)),
    ]
    callback_id = 1326

class RemoteStorageSetUserPublishedFileActionResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eAction', EWorkshopFileAction),
    ]
    callback_id = 1327

class RemoteStorageEnumeratePublishedFilesByUserActionResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_eAction', EWorkshopFileAction),
        ('m_nResultsReturned', c_int),
        ('m_nTotalResultCount', c_int),
        ('m_rgPublishedFileId', (c_ulonglong * 50)),
        ('m_rgRTimeUpdated', (c_uint * 50)),
    ]
    callback_id = 1328

class RemoteStoragePublishFileProgress_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_dPercentFile', c_double),
        ('m_bPreview', c_bool),
    ]
    callback_id = 1329

class RemoteStoragePublishedFileUpdated_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
        ('m_ulUnused', c_ulonglong),
    ]
    callback_id = 1330

class RemoteStorageFileWriteAsyncComplete_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 1331

class RemoteStorageFileReadAsyncComplete_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hFileReadAsync', c_ulonglong),
        ('m_eResult', EResult),
        ('m_nOffset', c_uint),
        ('m_cubRead', c_uint),
    ]
    callback_id = 1332

class RemoteStorageLocalFileChange_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 1333

class UserStatsReceived_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_eResult', EResult),
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 1101

class UserStatsStored_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_eResult', EResult),
    ]
    callback_id = 1102

class UserAchievementStored_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_bGroupAchievement', c_bool),
        ('m_rgchAchievementName', (c_byte * 128)),
        ('m_nCurProgress', c_uint),
        ('m_nMaxProgress', c_uint),
    ]
    callback_id = 1103

class LeaderboardFindResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hSteamLeaderboard', c_ulonglong),
        ('m_bLeaderboardFound', c_ubyte),
    ]
    callback_id = 1104

class LeaderboardScoresDownloaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hSteamLeaderboard', c_ulonglong),
        ('m_hSteamLeaderboardEntries', c_ulonglong),
        ('m_cEntryCount', c_int),
    ]
    callback_id = 1105

class LeaderboardScoreUploaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSuccess', c_ubyte),
        ('m_hSteamLeaderboard', c_ulonglong),
        ('m_nScore', c_int),
        ('m_bScoreChanged', c_ubyte),
        ('m_nGlobalRankNew', c_int),
        ('m_nGlobalRankPrevious', c_int),
    ]
    callback_id = 1106

class NumberOfCurrentPlayers_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSuccess', c_ubyte),
        ('m_cPlayers', c_int),
    ]
    callback_id = 1107

class UserStatsUnloaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 1108

class UserAchievementIconFetched_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_rgchAchievementName', (c_byte * 128)),
        ('m_bAchieved', c_bool),
        ('m_nIconHandle', c_int),
    ]
    callback_id = 1109

class GlobalAchievementPercentagesReady_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_eResult', EResult),
    ]
    callback_id = 1110

class LeaderboardUGCSet_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_hSteamLeaderboard', c_ulonglong),
    ]
    callback_id = 1111

class PS3TrophiesInstalled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_eResult', EResult),
        ('m_ulRequiredDiskSpace', c_ulonglong),
    ]
    callback_id = 1112

class GlobalStatsReceived_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nGameID', c_ulonglong),
        ('m_eResult', EResult),
    ]
    callback_id = 1112

class DlcInstalled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nAppID', c_uint),
    ]
    callback_id = 1005

class RegisterActivationCodeResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', ERegisterActivationCodeResult),
        ('m_unPackageRegistered', c_uint),
    ]
    callback_id = 1008

class NewUrlLaunchParameters_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 1014

class AppProofOfPurchaseKeyResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nAppID', c_uint),
        ('m_cchKeyLength', c_uint),
        ('m_rgchKey', (c_byte * 240)),
    ]
    callback_id = 1021

class FileDetailsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_ulFileSize', c_ulonglong),
        ('m_FileSHA', (c_ubyte * 20)),
        ('m_unFlags', c_uint),
    ]
    callback_id = 1023

class TimedTrialStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unAppID', c_uint),
        ('m_bIsOffline', c_bool),
        ('m_unSecondsAllowed', c_uint),
        ('m_unSecondsPlayed', c_uint),
    ]
    callback_id = 1030

class P2PSessionRequest_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDRemote', c_ulonglong),
    ]
    callback_id = 1202

class P2PSessionConnectFail_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDRemote', c_ulonglong),
        ('m_eP2PSessionError', c_ubyte),
    ]
    callback_id = 1203

class SocketStatusCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hSocket', c_uint),
        ('m_hListenSocket', c_uint),
        ('m_steamIDRemote', c_ulonglong),
        ('m_eSNetSocketState', c_int),
    ]
    callback_id = 1201

class ScreenshotReady_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hLocal', c_uint),
        ('m_eResult', EResult),
    ]
    callback_id = 2301

class ScreenshotRequested_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 2302

class PlaybackStatusHasChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4001

class VolumeHasChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_flNewVolume', c_float),
    ]
    callback_id = 4002

class MusicPlayerRemoteWillActivate_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4101

class MusicPlayerRemoteWillDeactivate_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4102

class MusicPlayerRemoteToFront_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4103

class MusicPlayerWillQuit_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4104

class MusicPlayerWantsPlay_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4105

class MusicPlayerWantsPause_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4106

class MusicPlayerWantsPlayPrevious_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4107

class MusicPlayerWantsPlayNext_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4108

class MusicPlayerWantsShuffled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bShuffled', c_bool),
    ]
    callback_id = 4109

class MusicPlayerWantsLooped_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bLooped', c_bool),
    ]
    callback_id = 4110

class MusicPlayerWantsVolume_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_flNewVolume', c_float),
    ]
    callback_id = 4011

class MusicPlayerSelectsQueueEntry_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('nID', c_int),
    ]
    callback_id = 4012

class MusicPlayerSelectsPlaylistEntry_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('nID', c_int),
    ]
    callback_id = 4013

class MusicPlayerWantsPlayingRepeatStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPlayingRepeatStatus', c_int),
    ]
    callback_id = 4114

class HTTPRequestCompleted_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hRequest', c_uint),
        ('m_ulContextValue', c_ulonglong),
        ('m_bRequestSuccessful', c_bool),
        ('m_eStatusCode', EHTTPStatusCode),
        ('m_unBodySize', c_uint),
    ]
    callback_id = 2101

class HTTPRequestHeadersReceived_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hRequest', c_uint),
        ('m_ulContextValue', c_ulonglong),
    ]
    callback_id = 2102

class HTTPRequestDataReceived_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hRequest', c_uint),
        ('m_ulContextValue', c_ulonglong),
        ('m_cOffset', c_uint),
        ('m_cBytesReceived', c_uint),
    ]
    callback_id = 2103

class SteamInputDeviceConnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulConnectedDeviceHandle', c_ulonglong),
    ]
    callback_id = 2801

class SteamInputDeviceDisconnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_ulDisconnectedDeviceHandle', c_ulonglong),
    ]
    callback_id = 2802

class SteamInputConfigurationLoaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unAppID', c_uint),
        ('m_ulDeviceHandle', c_ulonglong),
        ('m_ulMappingCreator', c_ulonglong),
        ('m_unMajorRevision', c_uint),
        ('m_unMinorRevision', c_uint),
        ('m_bUsesSteamInputAPI', c_bool),
        ('m_bUsesGamepadAPI', c_bool),
    ]
    callback_id = 2803

class SteamUGCQueryCompleted_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_handle', c_ulonglong),
        ('m_eResult', EResult),
        ('m_unNumResultsReturned', c_uint),
        ('m_unTotalMatchingResults', c_uint),
        ('m_bCachedData', c_bool),
        ('m_rgchNextCursor', (c_byte * 256)),
    ]
    callback_id = 3401

class SteamUGCRequestUGCDetailsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_details', SteamUGCDetails_t),
        ('m_bCachedData', c_bool),
    ]
    callback_id = 3402

class CreateItemResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_bUserNeedsToAcceptWorkshopLegalAgreement', c_bool),
    ]
    callback_id = 3403

class SubmitItemUpdateResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_bUserNeedsToAcceptWorkshopLegalAgreement', c_bool),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 3404

class ItemInstalled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unAppID', c_uint),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 3405

class DownloadItemResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unAppID', c_uint),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eResult', EResult),
    ]
    callback_id = 3406

class UserFavoriteItemsListChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eResult', EResult),
        ('m_bWasAddRequest', c_bool),
    ]
    callback_id = 3407

class SetUserItemVoteResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eResult', EResult),
        ('m_bVoteUp', c_bool),
    ]
    callback_id = 3408

class GetUserItemVoteResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nPublishedFileId', c_ulonglong),
        ('m_eResult', EResult),
        ('m_bVotedUp', c_bool),
        ('m_bVotedDown', c_bool),
        ('m_bVoteSkipped', c_bool),
    ]
    callback_id = 3409

class StartPlaytimeTrackingResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 3410

class StopPlaytimeTrackingResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 3411

class AddUGCDependencyResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nChildPublishedFileId', c_ulonglong),
    ]
    callback_id = 3412

class RemoveUGCDependencyResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nChildPublishedFileId', c_ulonglong),
    ]
    callback_id = 3413

class AddAppDependencyResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 3414

class RemoveAppDependencyResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_nAppID', c_uint),
    ]
    callback_id = 3415

class GetAppDependenciesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
        ('m_rgAppIDs', (c_uint * 32)),
        ('m_nNumAppDependencies', c_uint),
        ('m_nTotalNumAppDependencies', c_uint),
    ]
    callback_id = 3416

class DeleteItemResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nPublishedFileId', c_ulonglong),
    ]
    callback_id = 3417

class UserSubscribedItemsListChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nAppID', c_uint),
    ]
    callback_id = 3418

class WorkshopEULAStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nAppID', c_uint),
        ('m_unVersion', c_uint),
        ('m_rtAction', c_uint),
        ('m_bAccepted', c_bool),
        ('m_bNeedsAction', c_bool),
    ]
    callback_id = 3420

class SteamAppInstalled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nAppID', c_uint),
        ('m_iInstallFolderIndex', c_int),
    ]
    callback_id = 3901

class SteamAppUninstalled_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_nAppID', c_uint),
        ('m_iInstallFolderIndex', c_int),
    ]
    callback_id = 3902

class HTML_BrowserReady_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
    ]
    callback_id = 4501

class HTML_NeedsPaint_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pBGRA', c_char_p),
        ('unWide', c_uint),
        ('unTall', c_uint),
        ('unUpdateX', c_uint),
        ('unUpdateY', c_uint),
        ('unUpdateWide', c_uint),
        ('unUpdateTall', c_uint),
        ('unScrollX', c_uint),
        ('unScrollY', c_uint),
        ('flPageScale', c_float),
        ('unPageSerial', c_uint),
    ]
    callback_id = 4502

class HTML_StartRequest_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchURL', c_char_p),
        ('pchTarget', c_char_p),
        ('pchPostData', c_char_p),
        ('bIsRedirect', c_bool),
    ]
    callback_id = 4503

class HTML_CloseBrowser_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
    ]
    callback_id = 4504

class HTML_URLChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchURL', c_char_p),
        ('pchPostData', c_char_p),
        ('bIsRedirect', c_bool),
        ('pchPageTitle', c_char_p),
        ('bNewNavigation', c_bool),
    ]
    callback_id = 4505

class HTML_FinishedRequest_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchURL', c_char_p),
        ('pchPageTitle', c_char_p),
    ]
    callback_id = 4506

class HTML_OpenLinkInNewTab_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchURL', c_char_p),
    ]
    callback_id = 4507

class HTML_ChangedTitle_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchTitle', c_char_p),
    ]
    callback_id = 4508

class HTML_SearchResults_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('unResults', c_uint),
        ('unCurrentMatch', c_uint),
    ]
    callback_id = 4509

class HTML_CanGoBackAndForward_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('bCanGoBack', c_bool),
        ('bCanGoForward', c_bool),
    ]
    callback_id = 4510

class HTML_HorizontalScroll_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('unScrollMax', c_uint),
        ('unScrollCurrent', c_uint),
        ('flPageScale', c_float),
        ('bVisible', c_bool),
        ('unPageSize', c_uint),
    ]
    callback_id = 4511

class HTML_VerticalScroll_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('unScrollMax', c_uint),
        ('unScrollCurrent', c_uint),
        ('flPageScale', c_float),
        ('bVisible', c_bool),
        ('unPageSize', c_uint),
    ]
    callback_id = 4512

class HTML_LinkAtPosition_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('x', c_uint),
        ('y', c_uint),
        ('pchURL', c_char_p),
        ('bInput', c_bool),
        ('bLiveLink', c_bool),
    ]
    callback_id = 4513

class HTML_JSAlert_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchMessage', c_char_p),
    ]
    callback_id = 4514

class HTML_JSConfirm_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchMessage', c_char_p),
    ]
    callback_id = 4515

class HTML_FileOpenDialog_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchTitle', c_char_p),
        ('pchInitialFile', c_char_p),
    ]
    callback_id = 4516

class HTML_NewWindow_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchURL', c_char_p),
        ('unX', c_uint),
        ('unY', c_uint),
        ('unWide', c_uint),
        ('unTall', c_uint),
        ('unNewWindow_BrowserHandle_IGNORE', c_uint),
    ]
    callback_id = 4521

class HTML_SetCursor_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('eMouseCursor', c_uint),
    ]
    callback_id = 4522

class HTML_StatusText_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchMsg', c_char_p),
    ]
    callback_id = 4523

class HTML_ShowToolTip_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchMsg', c_char_p),
    ]
    callback_id = 4524

class HTML_UpdateToolTip_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('pchMsg', c_char_p),
    ]
    callback_id = 4525

class HTML_HideToolTip_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
    ]
    callback_id = 4526

class HTML_BrowserRestarted_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('unBrowserHandle', c_uint),
        ('unOldBrowserHandle', c_uint),
    ]
    callback_id = 4527

class SteamInventoryResultReady_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_handle', c_int),
        ('m_result', EResult),
    ]
    callback_id = 4700

class SteamInventoryFullUpdate_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_handle', c_int),
    ]
    callback_id = 4701

class SteamInventoryDefinitionUpdate_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 4702

class SteamInventoryEligiblePromoItemDefIDs_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_result', EResult),
        ('m_steamID', c_ulonglong),
        ('m_numEligiblePromoItemDefs', c_int),
        ('m_bCachedData', c_bool),
    ]
    callback_id = 4703

class SteamInventoryStartPurchaseResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_result', EResult),
        ('m_ulOrderID', c_ulonglong),
        ('m_ulTransID', c_ulonglong),
    ]
    callback_id = 4704

class SteamInventoryRequestPricesResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_result', EResult),
        ('m_rgchCurrency', (c_byte * 4)),
    ]
    callback_id = 4705

class GetVideoURLResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_unVideoAppID', c_uint),
        ('m_rgchURL', (c_byte * 256)),
    ]
    callback_id = 4611

class GetOPFSettingsResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_unVideoAppID', c_uint),
    ]
    callback_id = 4624

class SteamParentalSettingsChanged_t(Structure):
    _pack_ = PACK
    _fields_ = [
    ]
    callback_id = 5001

class SteamRemotePlaySessionConnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unSessionID', c_uint),
    ]
    callback_id = 5701

class SteamRemotePlaySessionDisconnected_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_unSessionID', c_uint),
    ]
    callback_id = 5702

class SteamNetworkingMessagesSessionRequest_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_identityRemote', SteamNetworkingIdentity),
    ]
    callback_id = 1251

class SteamNetworkingMessagesSessionFailed_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_info', SteamNetConnectionInfo_t),
    ]
    callback_id = 1252

class SteamNetConnectionStatusChangedCallback_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_hConn', c_uint),
        ('m_info', SteamNetConnectionInfo_t),
        ('m_eOldState', ESteamNetworkingConnectionState),
    ]
    callback_id = 1221

class SteamNetAuthenticationStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eAvail', ESteamNetworkingAvailability),
        ('m_debugMsg', (c_byte * 256)),
    ]
    callback_id = 1222

class SteamRelayNetworkStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eAvail', ESteamNetworkingAvailability),
        ('m_bPingMeasurementInProgress', c_int),
        ('m_eAvailNetworkConfig', ESteamNetworkingAvailability),
        ('m_eAvailAnyRelay', ESteamNetworkingAvailability),
        ('m_debugMsg', (c_byte * 256)),
    ]
    callback_id = 1281

class GSClientApprove_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamID', c_ulonglong),
        ('m_OwnerSteamID', c_ulonglong),
    ]
    callback_id = 201

class GSClientDeny_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamID', c_ulonglong),
        ('m_eDenyReason', EDenyReason),
        ('m_rgchOptionalText', (c_byte * 128)),
    ]
    callback_id = 202

class GSClientKick_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamID', c_ulonglong),
        ('m_eDenyReason', EDenyReason),
    ]
    callback_id = 203

class GSClientAchievementStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamID', c_ulonglong),
        ('m_pchAchievement', (c_byte * 128)),
        ('m_bUnlocked', c_bool),
    ]
    callback_id = 206

class GSPolicyResponse_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_bSecure', c_ubyte),
    ]
    callback_id = 115

class GSGameplayStats_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_nRank', c_int),
        ('m_unTotalConnects', c_uint),
        ('m_unTotalMinutesPlayed', c_uint),
    ]
    callback_id = 207

class GSClientGroupStatus_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_SteamIDUser', c_ulonglong),
        ('m_SteamIDGroup', c_ulonglong),
        ('m_bMember', c_bool),
        ('m_bOfficer', c_bool),
    ]
    callback_id = 208

class GSReputation_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_unReputationScore', c_uint),
        ('m_bBanned', c_bool),
        ('m_unBannedIP', c_uint),
        ('m_usBannedPort', c_ushort),
        ('m_ulBannedGameID', c_ulonglong),
        ('m_unBanExpires', c_uint),
    ]
    callback_id = 209

class AssociateWithClanResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
    ]
    callback_id = 210

class ComputeNewPlayerCompatibilityResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_cPlayersThatDontLikeCandidate', c_int),
        ('m_cPlayersThatCandidateDoesntLike', c_int),
        ('m_cClanPlayersThatDontLikeCandidate', c_int),
        ('m_SteamIDCandidate', c_ulonglong),
    ]
    callback_id = 211

class GSStatsReceived_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 1800

class GSStatsStored_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 1801

class GSStatsUnloaded_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_steamIDUser', c_ulonglong),
    ]
    callback_id = 1108

class SteamNetworkingFakeIPResult_t(Structure):
    _pack_ = PACK
    _fields_ = [
        ('m_eResult', EResult),
        ('m_identity', SteamNetworkingIdentity),
        ('m_unIP', c_uint),
        ('m_unPorts', (c_ushort * 8)),
    ]
    callback_id = 1223

callback_by_id = {
101 : SteamServersConnected_t,
102 : SteamServerConnectFailure_t,
103 : SteamServersDisconnected_t,
113 : ClientGameServerDeny_t,
117 : IPCFailure_t,
125 : LicensesUpdated_t,
143 : ValidateAuthTicketResponse_t,
152 : MicroTxnAuthorizationResponse_t,
154 : EncryptedAppTicketResponse_t,
163 : GetAuthSessionTicketResponse_t,
164 : GameWebCallback_t,
165 : StoreAuthURLResponse_t,
166 : MarketEligibilityResponse_t,
167 : DurationControl_t,
304 : PersonaStateChange_t,
331 : GameOverlayActivated_t,
332 : GameServerChangeRequested_t,
333 : GameLobbyJoinRequested_t,
334 : AvatarImageLoaded_t,
335 : ClanOfficerListResponse_t,
336 : FriendRichPresenceUpdate_t,
337 : GameRichPresenceJoinRequested_t,
338 : GameConnectedClanChatMsg_t,
339 : GameConnectedChatJoin_t,
340 : GameConnectedChatLeave_t,
341 : DownloadClanActivityCountsResult_t,
342 : JoinClanChatRoomCompletionResult_t,
343 : GameConnectedFriendChatMsg_t,
344 : FriendsGetFollowerCount_t,
345 : FriendsIsFollowing_t,
346 : FriendsEnumerateFollowingList_t,
347 : SetPersonaNameResponse_t,
348 : UnreadChatMessagesChanged_t,
349 : OverlayBrowserProtocolNavigation_t,
701 : IPCountry_t,
702 : LowBatteryPower_t,
703 : SteamAPICallCompleted_t,
704 : SteamShutdown_t,
705 : CheckFileSignature_t,
714 : GamepadTextInputDismissed_t,
736 : AppResumingFromSuspend_t,
738 : FloatingGamepadTextInputDismissed_t,
502 : FavoritesListChanged_t,
503 : LobbyInvite_t,
504 : LobbyEnter_t,
505 : LobbyDataUpdate_t,
506 : LobbyChatUpdate_t,
507 : LobbyChatMsg_t,
509 : LobbyGameCreated_t,
510 : LobbyMatchList_t,
512 : LobbyKicked_t,
513 : LobbyCreated_t,
515 : PSNGameBootInviteResult_t,
516 : FavoritesListAccountsUpdated_t,
5201 : SearchForGameProgressCallback_t,
5202 : SearchForGameResultCallback_t,
5211 : RequestPlayersForGameProgressCallback_t,
5212 : RequestPlayersForGameResultCallback_t,
5213 : RequestPlayersForGameFinalResultCallback_t,
5214 : SubmitPlayerResultResultCallback_t,
5215 : EndGameResultCallback_t,
5301 : JoinPartyCallback_t,
5302 : CreateBeaconCallback_t,
5303 : ReservationNotificationCallback_t,
5304 : ChangeNumOpenSlotsCallback_t,
5305 : AvailableBeaconLocationsUpdated_t,
5306 : ActiveBeaconsUpdated_t,
1307 : RemoteStorageFileShareResult_t,
1309 : RemoteStoragePublishFileResult_t,
1311 : RemoteStorageDeletePublishedFileResult_t,
1312 : RemoteStorageEnumerateUserPublishedFilesResult_t,
1313 : RemoteStorageSubscribePublishedFileResult_t,
1314 : RemoteStorageEnumerateUserSubscribedFilesResult_t,
1315 : RemoteStorageUnsubscribePublishedFileResult_t,
1316 : RemoteStorageUpdatePublishedFileResult_t,
1317 : RemoteStorageDownloadUGCResult_t,
1318 : RemoteStorageGetPublishedFileDetailsResult_t,
1319 : RemoteStorageEnumerateWorkshopFilesResult_t,
1320 : RemoteStorageGetPublishedItemVoteDetailsResult_t,
1321 : RemoteStoragePublishedFileSubscribed_t,
1322 : RemoteStoragePublishedFileUnsubscribed_t,
1323 : RemoteStoragePublishedFileDeleted_t,
1324 : RemoteStorageUpdateUserPublishedItemVoteResult_t,
1325 : RemoteStorageUserVoteDetails_t,
1326 : RemoteStorageEnumerateUserSharedWorkshopFilesResult_t,
1327 : RemoteStorageSetUserPublishedFileActionResult_t,
1328 : RemoteStorageEnumeratePublishedFilesByUserActionResult_t,
1329 : RemoteStoragePublishFileProgress_t,
1330 : RemoteStoragePublishedFileUpdated_t,
1331 : RemoteStorageFileWriteAsyncComplete_t,
1332 : RemoteStorageFileReadAsyncComplete_t,
1333 : RemoteStorageLocalFileChange_t,
1101 : UserStatsReceived_t,
1102 : UserStatsStored_t,
1103 : UserAchievementStored_t,
1104 : LeaderboardFindResult_t,
1105 : LeaderboardScoresDownloaded_t,
1106 : LeaderboardScoreUploaded_t,
1107 : NumberOfCurrentPlayers_t,
1108 : UserStatsUnloaded_t,
1109 : UserAchievementIconFetched_t,
1110 : GlobalAchievementPercentagesReady_t,
1111 : LeaderboardUGCSet_t,
1112 : PS3TrophiesInstalled_t,
1112 : GlobalStatsReceived_t,
1005 : DlcInstalled_t,
1008 : RegisterActivationCodeResponse_t,
1014 : NewUrlLaunchParameters_t,
1021 : AppProofOfPurchaseKeyResponse_t,
1023 : FileDetailsResult_t,
1030 : TimedTrialStatus_t,
1202 : P2PSessionRequest_t,
1203 : P2PSessionConnectFail_t,
1201 : SocketStatusCallback_t,
2301 : ScreenshotReady_t,
2302 : ScreenshotRequested_t,
4001 : PlaybackStatusHasChanged_t,
4002 : VolumeHasChanged_t,
4101 : MusicPlayerRemoteWillActivate_t,
4102 : MusicPlayerRemoteWillDeactivate_t,
4103 : MusicPlayerRemoteToFront_t,
4104 : MusicPlayerWillQuit_t,
4105 : MusicPlayerWantsPlay_t,
4106 : MusicPlayerWantsPause_t,
4107 : MusicPlayerWantsPlayPrevious_t,
4108 : MusicPlayerWantsPlayNext_t,
4109 : MusicPlayerWantsShuffled_t,
4110 : MusicPlayerWantsLooped_t,
4011 : MusicPlayerWantsVolume_t,
4012 : MusicPlayerSelectsQueueEntry_t,
4013 : MusicPlayerSelectsPlaylistEntry_t,
4114 : MusicPlayerWantsPlayingRepeatStatus_t,
2101 : HTTPRequestCompleted_t,
2102 : HTTPRequestHeadersReceived_t,
2103 : HTTPRequestDataReceived_t,
2801 : SteamInputDeviceConnected_t,
2802 : SteamInputDeviceDisconnected_t,
2803 : SteamInputConfigurationLoaded_t,
3401 : SteamUGCQueryCompleted_t,
3402 : SteamUGCRequestUGCDetailsResult_t,
3403 : CreateItemResult_t,
3404 : SubmitItemUpdateResult_t,
3405 : ItemInstalled_t,
3406 : DownloadItemResult_t,
3407 : UserFavoriteItemsListChanged_t,
3408 : SetUserItemVoteResult_t,
3409 : GetUserItemVoteResult_t,
3410 : StartPlaytimeTrackingResult_t,
3411 : StopPlaytimeTrackingResult_t,
3412 : AddUGCDependencyResult_t,
3413 : RemoveUGCDependencyResult_t,
3414 : AddAppDependencyResult_t,
3415 : RemoveAppDependencyResult_t,
3416 : GetAppDependenciesResult_t,
3417 : DeleteItemResult_t,
3418 : UserSubscribedItemsListChanged_t,
3420 : WorkshopEULAStatus_t,
3901 : SteamAppInstalled_t,
3902 : SteamAppUninstalled_t,
4501 : HTML_BrowserReady_t,
4502 : HTML_NeedsPaint_t,
4503 : HTML_StartRequest_t,
4504 : HTML_CloseBrowser_t,
4505 : HTML_URLChanged_t,
4506 : HTML_FinishedRequest_t,
4507 : HTML_OpenLinkInNewTab_t,
4508 : HTML_ChangedTitle_t,
4509 : HTML_SearchResults_t,
4510 : HTML_CanGoBackAndForward_t,
4511 : HTML_HorizontalScroll_t,
4512 : HTML_VerticalScroll_t,
4513 : HTML_LinkAtPosition_t,
4514 : HTML_JSAlert_t,
4515 : HTML_JSConfirm_t,
4516 : HTML_FileOpenDialog_t,
4521 : HTML_NewWindow_t,
4522 : HTML_SetCursor_t,
4523 : HTML_StatusText_t,
4524 : HTML_ShowToolTip_t,
4525 : HTML_UpdateToolTip_t,
4526 : HTML_HideToolTip_t,
4527 : HTML_BrowserRestarted_t,
4700 : SteamInventoryResultReady_t,
4701 : SteamInventoryFullUpdate_t,
4702 : SteamInventoryDefinitionUpdate_t,
4703 : SteamInventoryEligiblePromoItemDefIDs_t,
4704 : SteamInventoryStartPurchaseResult_t,
4705 : SteamInventoryRequestPricesResult_t,
4611 : GetVideoURLResult_t,
4624 : GetOPFSettingsResult_t,
5001 : SteamParentalSettingsChanged_t,
5701 : SteamRemotePlaySessionConnected_t,
5702 : SteamRemotePlaySessionDisconnected_t,
1251 : SteamNetworkingMessagesSessionRequest_t,
1252 : SteamNetworkingMessagesSessionFailed_t,
1221 : SteamNetConnectionStatusChangedCallback_t,
1222 : SteamNetAuthenticationStatus_t,
1281 : SteamRelayNetworkStatus_t,
201 : GSClientApprove_t,
202 : GSClientDeny_t,
203 : GSClientKick_t,
206 : GSClientAchievementStatus_t,
115 : GSPolicyResponse_t,
207 : GSGameplayStats_t,
208 : GSClientGroupStatus_t,
209 : GSReputation_t,
210 : AssociateWithClanResult_t,
211 : ComputeNewPlayerCompatibilityResult_t,
1800 : GSStatsReceived_t,
1801 : GSStatsStored_t,
1108 : GSStatsUnloaded_t,
1223 : SteamNetworkingFakeIPResult_t,
}

class ISteamClient(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def CreateSteamPipe(self, ):
        return ISteamClient_CreateSteamPipe(byref(self), ) # type: ignore

    def BReleaseSteamPipe(self, hSteamPipe):
        return ISteamClient_BReleaseSteamPipe(byref(self), hSteamPipe) # type: ignore

    def ConnectToGlobalUser(self, hSteamPipe):
        return ISteamClient_ConnectToGlobalUser(byref(self), hSteamPipe) # type: ignore

    def CreateLocalUser(self, phSteamPipe, eAccountType):
        return ISteamClient_CreateLocalUser(byref(self), phSteamPipe, eAccountType) # type: ignore

    def ReleaseUser(self, hSteamPipe, hUser):
        return ISteamClient_ReleaseUser(byref(self), hSteamPipe, hUser) # type: ignore

    def GetISteamUser(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamUser(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamGameServer(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamGameServer(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def SetLocalIPBinding(self, unIP, usPort):
        return ISteamClient_SetLocalIPBinding(byref(self), unIP, usPort) # type: ignore

    def GetISteamFriends(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamFriends(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamUtils(self, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamUtils(byref(self), hSteamPipe, pchVersion) # type: ignore

    def GetISteamMatchmaking(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamMatchmaking(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamMatchmakingServers(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamMatchmakingServers(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamGenericInterface(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamGenericInterface(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamUserStats(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamUserStats(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamGameServerStats(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamGameServerStats(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamApps(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamApps(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamNetworking(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamNetworking(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamRemoteStorage(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamRemoteStorage(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamScreenshots(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamScreenshots(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamGameSearch(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamGameSearch(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetIPCCallCount(self, ):
        return ISteamClient_GetIPCCallCount(byref(self), ) # type: ignore

    def SetWarningMessageHook(self, pFunction):
        return ISteamClient_SetWarningMessageHook(byref(self), pFunction) # type: ignore

    def BShutdownIfAllPipesClosed(self, ):
        return ISteamClient_BShutdownIfAllPipesClosed(byref(self), ) # type: ignore

    def GetISteamHTTP(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamHTTP(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamController(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamController(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamUGC(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamUGC(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamAppList(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamAppList(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamMusic(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamMusic(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamMusicRemote(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamMusicRemote(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamHTMLSurface(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamHTMLSurface(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamInventory(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamInventory(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamVideo(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamVideo(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamParentalSettings(self, hSteamuser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamParentalSettings(byref(self), hSteamuser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamInput(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamInput(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamParties(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamParties(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

    def GetISteamRemotePlay(self, hSteamUser, hSteamPipe, pchVersion):
        return ISteamClient_GetISteamRemotePlay(byref(self), hSteamUser, hSteamPipe, pchVersion) # type: ignore

class ISteamUser(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetHSteamUser(self, ):
        return ISteamUser_GetHSteamUser(byref(self), ) # type: ignore

    def BLoggedOn(self, ):
        return ISteamUser_BLoggedOn(byref(self), ) # type: ignore

    def GetSteamID(self, ):
        return ISteamUser_GetSteamID(byref(self), ) # type: ignore

    def InitiateGameConnection_DEPRECATED(self, pAuthBlob, cbMaxAuthBlob, steamIDGameServer, unIPServer, usPortServer, bSecure):
        return ISteamUser_InitiateGameConnection_DEPRECATED(byref(self), pAuthBlob, cbMaxAuthBlob, steamIDGameServer, unIPServer, usPortServer, bSecure) # type: ignore

    def TerminateGameConnection_DEPRECATED(self, unIPServer, usPortServer):
        return ISteamUser_TerminateGameConnection_DEPRECATED(byref(self), unIPServer, usPortServer) # type: ignore

    def TrackAppUsageEvent(self, gameID, eAppUsageEvent, pchExtraInfo):
        return ISteamUser_TrackAppUsageEvent(byref(self), gameID, eAppUsageEvent, pchExtraInfo) # type: ignore

    def GetUserDataFolder(self, pchBuffer, cubBuffer):
        return ISteamUser_GetUserDataFolder(byref(self), pchBuffer, cubBuffer) # type: ignore

    def StartVoiceRecording(self, ):
        return ISteamUser_StartVoiceRecording(byref(self), ) # type: ignore

    def StopVoiceRecording(self, ):
        return ISteamUser_StopVoiceRecording(byref(self), ) # type: ignore

    def GetAvailableVoice(self, pcbCompressed, pcbUncompressed_Deprecated, nUncompressedVoiceDesiredSampleRate_Deprecated):
        return ISteamUser_GetAvailableVoice(byref(self), pcbCompressed, pcbUncompressed_Deprecated, nUncompressedVoiceDesiredSampleRate_Deprecated) # type: ignore

    def GetVoice(self, bWantCompressed, pDestBuffer, cbDestBufferSize, nBytesWritten, bWantUncompressed_Deprecated, pUncompressedDestBuffer_Deprecated, cbUncompressedDestBufferSize_Deprecated, nUncompressBytesWritten_Deprecated, nUncompressedVoiceDesiredSampleRate_Deprecated):
        return ISteamUser_GetVoice(byref(self), bWantCompressed, pDestBuffer, cbDestBufferSize, nBytesWritten, bWantUncompressed_Deprecated, pUncompressedDestBuffer_Deprecated, cbUncompressedDestBufferSize_Deprecated, nUncompressBytesWritten_Deprecated, nUncompressedVoiceDesiredSampleRate_Deprecated) # type: ignore

    def DecompressVoice(self, pCompressed, cbCompressed, pDestBuffer, cbDestBufferSize, nBytesWritten, nDesiredSampleRate):
        return ISteamUser_DecompressVoice(byref(self), pCompressed, cbCompressed, pDestBuffer, cbDestBufferSize, nBytesWritten, nDesiredSampleRate) # type: ignore

    def GetVoiceOptimalSampleRate(self, ):
        return ISteamUser_GetVoiceOptimalSampleRate(byref(self), ) # type: ignore

    def GetAuthSessionTicket(self, pTicket, cbMaxTicket, pcbTicket):
        return ISteamUser_GetAuthSessionTicket(byref(self), pTicket, cbMaxTicket, pcbTicket) # type: ignore

    def BeginAuthSession(self, pAuthTicket, cbAuthTicket, steamID):
        return ISteamUser_BeginAuthSession(byref(self), pAuthTicket, cbAuthTicket, steamID) # type: ignore

    def EndAuthSession(self, steamID):
        return ISteamUser_EndAuthSession(byref(self), steamID) # type: ignore

    def CancelAuthTicket(self, hAuthTicket):
        return ISteamUser_CancelAuthTicket(byref(self), hAuthTicket) # type: ignore

    def UserHasLicenseForApp(self, steamID, appID):
        return ISteamUser_UserHasLicenseForApp(byref(self), steamID, appID) # type: ignore

    def BIsBehindNAT(self, ):
        return ISteamUser_BIsBehindNAT(byref(self), ) # type: ignore

    def AdvertiseGame(self, steamIDGameServer, unIPServer, usPortServer):
        return ISteamUser_AdvertiseGame(byref(self), steamIDGameServer, unIPServer, usPortServer) # type: ignore

    def RequestEncryptedAppTicket(self, pDataToInclude, cbDataToInclude):
        return ISteamUser_RequestEncryptedAppTicket(byref(self), pDataToInclude, cbDataToInclude) # type: ignore

    def GetEncryptedAppTicket(self, pTicket, cbMaxTicket, pcbTicket):
        return ISteamUser_GetEncryptedAppTicket(byref(self), pTicket, cbMaxTicket, pcbTicket) # type: ignore

    def GetGameBadgeLevel(self, nSeries, bFoil):
        return ISteamUser_GetGameBadgeLevel(byref(self), nSeries, bFoil) # type: ignore

    def GetPlayerSteamLevel(self, ):
        return ISteamUser_GetPlayerSteamLevel(byref(self), ) # type: ignore

    def RequestStoreAuthURL(self, pchRedirectURL):
        return ISteamUser_RequestStoreAuthURL(byref(self), pchRedirectURL) # type: ignore

    def BIsPhoneVerified(self, ):
        return ISteamUser_BIsPhoneVerified(byref(self), ) # type: ignore

    def BIsTwoFactorEnabled(self, ):
        return ISteamUser_BIsTwoFactorEnabled(byref(self), ) # type: ignore

    def BIsPhoneIdentifying(self, ):
        return ISteamUser_BIsPhoneIdentifying(byref(self), ) # type: ignore

    def BIsPhoneRequiringVerification(self, ):
        return ISteamUser_BIsPhoneRequiringVerification(byref(self), ) # type: ignore

    def GetMarketEligibility(self, ):
        return ISteamUser_GetMarketEligibility(byref(self), ) # type: ignore

    def GetDurationControl(self, ):
        return ISteamUser_GetDurationControl(byref(self), ) # type: ignore

    def BSetDurationControlOnlineState(self, eNewState):
        return ISteamUser_BSetDurationControlOnlineState(byref(self), eNewState) # type: ignore

class ISteamFriends(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetPersonaName(self, ):
        return ISteamFriends_GetPersonaName(byref(self), ) # type: ignore

    def SetPersonaName(self, pchPersonaName):
        return ISteamFriends_SetPersonaName(byref(self), pchPersonaName) # type: ignore

    def GetPersonaState(self, ):
        return ISteamFriends_GetPersonaState(byref(self), ) # type: ignore

    def GetFriendCount(self, iFriendFlags):
        return ISteamFriends_GetFriendCount(byref(self), iFriendFlags) # type: ignore

    def GetFriendByIndex(self, iFriend, iFriendFlags):
        return ISteamFriends_GetFriendByIndex(byref(self), iFriend, iFriendFlags) # type: ignore

    def GetFriendRelationship(self, steamIDFriend):
        return ISteamFriends_GetFriendRelationship(byref(self), steamIDFriend) # type: ignore

    def GetFriendPersonaState(self, steamIDFriend):
        return ISteamFriends_GetFriendPersonaState(byref(self), steamIDFriend) # type: ignore

    def GetFriendPersonaName(self, steamIDFriend):
        return ISteamFriends_GetFriendPersonaName(byref(self), steamIDFriend) # type: ignore

    def GetFriendGamePlayed(self, steamIDFriend, pFriendGameInfo):
        return ISteamFriends_GetFriendGamePlayed(byref(self), steamIDFriend, pFriendGameInfo) # type: ignore

    def GetFriendPersonaNameHistory(self, steamIDFriend, iPersonaName):
        return ISteamFriends_GetFriendPersonaNameHistory(byref(self), steamIDFriend, iPersonaName) # type: ignore

    def GetFriendSteamLevel(self, steamIDFriend):
        return ISteamFriends_GetFriendSteamLevel(byref(self), steamIDFriend) # type: ignore

    def GetPlayerNickname(self, steamIDPlayer):
        return ISteamFriends_GetPlayerNickname(byref(self), steamIDPlayer) # type: ignore

    def GetFriendsGroupCount(self, ):
        return ISteamFriends_GetFriendsGroupCount(byref(self), ) # type: ignore

    def GetFriendsGroupIDByIndex(self, iFG):
        return ISteamFriends_GetFriendsGroupIDByIndex(byref(self), iFG) # type: ignore

    def GetFriendsGroupName(self, friendsGroupID):
        return ISteamFriends_GetFriendsGroupName(byref(self), friendsGroupID) # type: ignore

    def GetFriendsGroupMembersCount(self, friendsGroupID):
        return ISteamFriends_GetFriendsGroupMembersCount(byref(self), friendsGroupID) # type: ignore

    def GetFriendsGroupMembersList(self, friendsGroupID, pOutSteamIDMembers, nMembersCount):
        return ISteamFriends_GetFriendsGroupMembersList(byref(self), friendsGroupID, pOutSteamIDMembers, nMembersCount) # type: ignore

    def HasFriend(self, steamIDFriend, iFriendFlags):
        return ISteamFriends_HasFriend(byref(self), steamIDFriend, iFriendFlags) # type: ignore

    def GetClanCount(self, ):
        return ISteamFriends_GetClanCount(byref(self), ) # type: ignore

    def GetClanByIndex(self, iClan):
        return ISteamFriends_GetClanByIndex(byref(self), iClan) # type: ignore

    def GetClanName(self, steamIDClan):
        return ISteamFriends_GetClanName(byref(self), steamIDClan) # type: ignore

    def GetClanTag(self, steamIDClan):
        return ISteamFriends_GetClanTag(byref(self), steamIDClan) # type: ignore

    def GetClanActivityCounts(self, steamIDClan, pnOnline, pnInGame, pnChatting):
        return ISteamFriends_GetClanActivityCounts(byref(self), steamIDClan, pnOnline, pnInGame, pnChatting) # type: ignore

    def DownloadClanActivityCounts(self, psteamIDClans, cClansToRequest):
        return ISteamFriends_DownloadClanActivityCounts(byref(self), psteamIDClans, cClansToRequest) # type: ignore

    def GetFriendCountFromSource(self, steamIDSource):
        return ISteamFriends_GetFriendCountFromSource(byref(self), steamIDSource) # type: ignore

    def GetFriendFromSourceByIndex(self, steamIDSource, iFriend):
        return ISteamFriends_GetFriendFromSourceByIndex(byref(self), steamIDSource, iFriend) # type: ignore

    def IsUserInSource(self, steamIDUser, steamIDSource):
        return ISteamFriends_IsUserInSource(byref(self), steamIDUser, steamIDSource) # type: ignore

    def SetInGameVoiceSpeaking(self, steamIDUser, bSpeaking):
        return ISteamFriends_SetInGameVoiceSpeaking(byref(self), steamIDUser, bSpeaking) # type: ignore

    def ActivateGameOverlay(self, pchDialog):
        return ISteamFriends_ActivateGameOverlay(byref(self), pchDialog) # type: ignore

    def ActivateGameOverlayToUser(self, pchDialog, steamID):
        return ISteamFriends_ActivateGameOverlayToUser(byref(self), pchDialog, steamID) # type: ignore

    def ActivateGameOverlayToWebPage(self, pchURL, eMode):
        return ISteamFriends_ActivateGameOverlayToWebPage(byref(self), pchURL, eMode) # type: ignore

    def ActivateGameOverlayToStore(self, nAppID, eFlag):
        return ISteamFriends_ActivateGameOverlayToStore(byref(self), nAppID, eFlag) # type: ignore

    def SetPlayedWith(self, steamIDUserPlayedWith):
        return ISteamFriends_SetPlayedWith(byref(self), steamIDUserPlayedWith) # type: ignore

    def ActivateGameOverlayInviteDialog(self, steamIDLobby):
        return ISteamFriends_ActivateGameOverlayInviteDialog(byref(self), steamIDLobby) # type: ignore

    def GetSmallFriendAvatar(self, steamIDFriend):
        return ISteamFriends_GetSmallFriendAvatar(byref(self), steamIDFriend) # type: ignore

    def GetMediumFriendAvatar(self, steamIDFriend):
        return ISteamFriends_GetMediumFriendAvatar(byref(self), steamIDFriend) # type: ignore

    def GetLargeFriendAvatar(self, steamIDFriend):
        return ISteamFriends_GetLargeFriendAvatar(byref(self), steamIDFriend) # type: ignore

    def RequestUserInformation(self, steamIDUser, bRequireNameOnly):
        return ISteamFriends_RequestUserInformation(byref(self), steamIDUser, bRequireNameOnly) # type: ignore

    def RequestClanOfficerList(self, steamIDClan):
        return ISteamFriends_RequestClanOfficerList(byref(self), steamIDClan) # type: ignore

    def GetClanOwner(self, steamIDClan):
        return ISteamFriends_GetClanOwner(byref(self), steamIDClan) # type: ignore

    def GetClanOfficerCount(self, steamIDClan):
        return ISteamFriends_GetClanOfficerCount(byref(self), steamIDClan) # type: ignore

    def GetClanOfficerByIndex(self, steamIDClan, iOfficer):
        return ISteamFriends_GetClanOfficerByIndex(byref(self), steamIDClan, iOfficer) # type: ignore

    def GetUserRestrictions(self, ):
        return ISteamFriends_GetUserRestrictions(byref(self), ) # type: ignore

    def SetRichPresence(self, pchKey, pchValue):
        return ISteamFriends_SetRichPresence(byref(self), pchKey, pchValue) # type: ignore

    def ClearRichPresence(self, ):
        return ISteamFriends_ClearRichPresence(byref(self), ) # type: ignore

    def GetFriendRichPresence(self, steamIDFriend, pchKey):
        return ISteamFriends_GetFriendRichPresence(byref(self), steamIDFriend, pchKey) # type: ignore

    def GetFriendRichPresenceKeyCount(self, steamIDFriend):
        return ISteamFriends_GetFriendRichPresenceKeyCount(byref(self), steamIDFriend) # type: ignore

    def GetFriendRichPresenceKeyByIndex(self, steamIDFriend, iKey):
        return ISteamFriends_GetFriendRichPresenceKeyByIndex(byref(self), steamIDFriend, iKey) # type: ignore

    def RequestFriendRichPresence(self, steamIDFriend):
        return ISteamFriends_RequestFriendRichPresence(byref(self), steamIDFriend) # type: ignore

    def InviteUserToGame(self, steamIDFriend, pchConnectString):
        return ISteamFriends_InviteUserToGame(byref(self), steamIDFriend, pchConnectString) # type: ignore

    def GetCoplayFriendCount(self, ):
        return ISteamFriends_GetCoplayFriendCount(byref(self), ) # type: ignore

    def GetCoplayFriend(self, iCoplayFriend):
        return ISteamFriends_GetCoplayFriend(byref(self), iCoplayFriend) # type: ignore

    def GetFriendCoplayTime(self, steamIDFriend):
        return ISteamFriends_GetFriendCoplayTime(byref(self), steamIDFriend) # type: ignore

    def GetFriendCoplayGame(self, steamIDFriend):
        return ISteamFriends_GetFriendCoplayGame(byref(self), steamIDFriend) # type: ignore

    def JoinClanChatRoom(self, steamIDClan):
        return ISteamFriends_JoinClanChatRoom(byref(self), steamIDClan) # type: ignore

    def LeaveClanChatRoom(self, steamIDClan):
        return ISteamFriends_LeaveClanChatRoom(byref(self), steamIDClan) # type: ignore

    def GetClanChatMemberCount(self, steamIDClan):
        return ISteamFriends_GetClanChatMemberCount(byref(self), steamIDClan) # type: ignore

    def GetChatMemberByIndex(self, steamIDClan, iUser):
        return ISteamFriends_GetChatMemberByIndex(byref(self), steamIDClan, iUser) # type: ignore

    def SendClanChatMessage(self, steamIDClanChat, pchText):
        return ISteamFriends_SendClanChatMessage(byref(self), steamIDClanChat, pchText) # type: ignore

    def GetClanChatMessage(self, steamIDClanChat, iMessage, prgchText, cchTextMax, peChatEntryType, psteamidChatter):
        return ISteamFriends_GetClanChatMessage(byref(self), steamIDClanChat, iMessage, prgchText, cchTextMax, peChatEntryType, psteamidChatter) # type: ignore

    def IsClanChatAdmin(self, steamIDClanChat, steamIDUser):
        return ISteamFriends_IsClanChatAdmin(byref(self), steamIDClanChat, steamIDUser) # type: ignore

    def IsClanChatWindowOpenInSteam(self, steamIDClanChat):
        return ISteamFriends_IsClanChatWindowOpenInSteam(byref(self), steamIDClanChat) # type: ignore

    def OpenClanChatWindowInSteam(self, steamIDClanChat):
        return ISteamFriends_OpenClanChatWindowInSteam(byref(self), steamIDClanChat) # type: ignore

    def CloseClanChatWindowInSteam(self, steamIDClanChat):
        return ISteamFriends_CloseClanChatWindowInSteam(byref(self), steamIDClanChat) # type: ignore

    def SetListenForFriendsMessages(self, bInterceptEnabled):
        return ISteamFriends_SetListenForFriendsMessages(byref(self), bInterceptEnabled) # type: ignore

    def ReplyToFriendMessage(self, steamIDFriend, pchMsgToSend):
        return ISteamFriends_ReplyToFriendMessage(byref(self), steamIDFriend, pchMsgToSend) # type: ignore

    def GetFriendMessage(self, steamIDFriend, iMessageID, pvData, cubData, peChatEntryType):
        return ISteamFriends_GetFriendMessage(byref(self), steamIDFriend, iMessageID, pvData, cubData, peChatEntryType) # type: ignore

    def GetFollowerCount(self, steamID):
        return ISteamFriends_GetFollowerCount(byref(self), steamID) # type: ignore

    def IsFollowing(self, steamID):
        return ISteamFriends_IsFollowing(byref(self), steamID) # type: ignore

    def EnumerateFollowingList(self, unStartIndex):
        return ISteamFriends_EnumerateFollowingList(byref(self), unStartIndex) # type: ignore

    def IsClanPublic(self, steamIDClan):
        return ISteamFriends_IsClanPublic(byref(self), steamIDClan) # type: ignore

    def IsClanOfficialGameGroup(self, steamIDClan):
        return ISteamFriends_IsClanOfficialGameGroup(byref(self), steamIDClan) # type: ignore

    def GetNumChatsWithUnreadPriorityMessages(self, ):
        return ISteamFriends_GetNumChatsWithUnreadPriorityMessages(byref(self), ) # type: ignore

    def ActivateGameOverlayRemotePlayTogetherInviteDialog(self, steamIDLobby):
        return ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog(byref(self), steamIDLobby) # type: ignore

    def RegisterProtocolInOverlayBrowser(self, pchProtocol):
        return ISteamFriends_RegisterProtocolInOverlayBrowser(byref(self), pchProtocol) # type: ignore

    def ActivateGameOverlayInviteDialogConnectString(self, pchConnectString):
        return ISteamFriends_ActivateGameOverlayInviteDialogConnectString(byref(self), pchConnectString) # type: ignore

class ISteamUtils(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetSecondsSinceAppActive(self, ):
        return ISteamUtils_GetSecondsSinceAppActive(byref(self), ) # type: ignore

    def GetSecondsSinceComputerActive(self, ):
        return ISteamUtils_GetSecondsSinceComputerActive(byref(self), ) # type: ignore

    def GetConnectedUniverse(self, ):
        return ISteamUtils_GetConnectedUniverse(byref(self), ) # type: ignore

    def GetServerRealTime(self, ):
        return ISteamUtils_GetServerRealTime(byref(self), ) # type: ignore

    def GetIPCountry(self, ):
        return ISteamUtils_GetIPCountry(byref(self), ) # type: ignore

    def GetImageSize(self, iImage, pnWidth, pnHeight):
        return ISteamUtils_GetImageSize(byref(self), iImage, pnWidth, pnHeight) # type: ignore

    def GetImageRGBA(self, iImage, pubDest, nDestBufferSize):
        return ISteamUtils_GetImageRGBA(byref(self), iImage, pubDest, nDestBufferSize) # type: ignore

    def GetCurrentBatteryPower(self, ):
        return ISteamUtils_GetCurrentBatteryPower(byref(self), ) # type: ignore

    def GetAppID(self, ):
        return ISteamUtils_GetAppID(byref(self), ) # type: ignore

    def SetOverlayNotificationPosition(self, eNotificationPosition):
        return ISteamUtils_SetOverlayNotificationPosition(byref(self), eNotificationPosition) # type: ignore

    def IsAPICallCompleted(self, hSteamAPICall, pbFailed):
        return ISteamUtils_IsAPICallCompleted(byref(self), hSteamAPICall, pbFailed) # type: ignore

    def GetAPICallFailureReason(self, hSteamAPICall):
        return ISteamUtils_GetAPICallFailureReason(byref(self), hSteamAPICall) # type: ignore

    def GetAPICallResult(self, hSteamAPICall, pCallback, cubCallback, iCallbackExpected, pbFailed):
        return ISteamUtils_GetAPICallResult(byref(self), hSteamAPICall, pCallback, cubCallback, iCallbackExpected, pbFailed) # type: ignore

    def GetIPCCallCount(self, ):
        return ISteamUtils_GetIPCCallCount(byref(self), ) # type: ignore

    def SetWarningMessageHook(self, pFunction):
        return ISteamUtils_SetWarningMessageHook(byref(self), pFunction) # type: ignore

    def IsOverlayEnabled(self, ):
        return ISteamUtils_IsOverlayEnabled(byref(self), ) # type: ignore

    def BOverlayNeedsPresent(self, ):
        return ISteamUtils_BOverlayNeedsPresent(byref(self), ) # type: ignore

    def CheckFileSignature(self, szFileName):
        return ISteamUtils_CheckFileSignature(byref(self), szFileName) # type: ignore

    def ShowGamepadTextInput(self, eInputMode, eLineInputMode, pchDescription, unCharMax, pchExistingText):
        return ISteamUtils_ShowGamepadTextInput(byref(self), eInputMode, eLineInputMode, pchDescription, unCharMax, pchExistingText) # type: ignore

    def GetEnteredGamepadTextLength(self, ):
        return ISteamUtils_GetEnteredGamepadTextLength(byref(self), ) # type: ignore

    def GetEnteredGamepadTextInput(self, pchText, cchText):
        return ISteamUtils_GetEnteredGamepadTextInput(byref(self), pchText, cchText) # type: ignore

    def GetSteamUILanguage(self, ):
        return ISteamUtils_GetSteamUILanguage(byref(self), ) # type: ignore

    def IsSteamRunningInVR(self, ):
        return ISteamUtils_IsSteamRunningInVR(byref(self), ) # type: ignore

    def SetOverlayNotificationInset(self, nHorizontalInset, nVerticalInset):
        return ISteamUtils_SetOverlayNotificationInset(byref(self), nHorizontalInset, nVerticalInset) # type: ignore

    def IsSteamInBigPictureMode(self, ):
        return ISteamUtils_IsSteamInBigPictureMode(byref(self), ) # type: ignore

    def StartVRDashboard(self, ):
        return ISteamUtils_StartVRDashboard(byref(self), ) # type: ignore

    def IsVRHeadsetStreamingEnabled(self, ):
        return ISteamUtils_IsVRHeadsetStreamingEnabled(byref(self), ) # type: ignore

    def SetVRHeadsetStreamingEnabled(self, bEnabled):
        return ISteamUtils_SetVRHeadsetStreamingEnabled(byref(self), bEnabled) # type: ignore

    def IsSteamChinaLauncher(self, ):
        return ISteamUtils_IsSteamChinaLauncher(byref(self), ) # type: ignore

    def InitFilterText(self, unFilterOptions):
        return ISteamUtils_InitFilterText(byref(self), unFilterOptions) # type: ignore

    def FilterText(self, eContext, sourceSteamID, pchInputMessage, pchOutFilteredText, nByteSizeOutFilteredText):
        return ISteamUtils_FilterText(byref(self), eContext, sourceSteamID, pchInputMessage, pchOutFilteredText, nByteSizeOutFilteredText) # type: ignore

    def GetIPv6ConnectivityState(self, eProtocol):
        return ISteamUtils_GetIPv6ConnectivityState(byref(self), eProtocol) # type: ignore

    def IsSteamRunningOnSteamDeck(self, ):
        return ISteamUtils_IsSteamRunningOnSteamDeck(byref(self), ) # type: ignore

    def ShowFloatingGamepadTextInput(self, eKeyboardMode, nTextFieldXPosition, nTextFieldYPosition, nTextFieldWidth, nTextFieldHeight):
        return ISteamUtils_ShowFloatingGamepadTextInput(byref(self), eKeyboardMode, nTextFieldXPosition, nTextFieldYPosition, nTextFieldWidth, nTextFieldHeight) # type: ignore

    def SetGameLauncherMode(self, bLauncherMode):
        return ISteamUtils_SetGameLauncherMode(byref(self), bLauncherMode) # type: ignore

    def DismissFloatingGamepadTextInput(self, ):
        return ISteamUtils_DismissFloatingGamepadTextInput(byref(self), ) # type: ignore

class ISteamMatchmaking(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetFavoriteGameCount(self, ):
        return ISteamMatchmaking_GetFavoriteGameCount(byref(self), ) # type: ignore

    def GetFavoriteGame(self, iGame, pnAppID, pnIP, pnConnPort, pnQueryPort, punFlags, pRTime32LastPlayedOnServer):
        return ISteamMatchmaking_GetFavoriteGame(byref(self), iGame, pnAppID, pnIP, pnConnPort, pnQueryPort, punFlags, pRTime32LastPlayedOnServer) # type: ignore

    def AddFavoriteGame(self, nAppID, nIP, nConnPort, nQueryPort, unFlags, rTime32LastPlayedOnServer):
        return ISteamMatchmaking_AddFavoriteGame(byref(self), nAppID, nIP, nConnPort, nQueryPort, unFlags, rTime32LastPlayedOnServer) # type: ignore

    def RemoveFavoriteGame(self, nAppID, nIP, nConnPort, nQueryPort, unFlags):
        return ISteamMatchmaking_RemoveFavoriteGame(byref(self), nAppID, nIP, nConnPort, nQueryPort, unFlags) # type: ignore

    def RequestLobbyList(self, ):
        return ISteamMatchmaking_RequestLobbyList(byref(self), ) # type: ignore

    def AddRequestLobbyListStringFilter(self, pchKeyToMatch, pchValueToMatch, eComparisonType):
        return ISteamMatchmaking_AddRequestLobbyListStringFilter(byref(self), pchKeyToMatch, pchValueToMatch, eComparisonType) # type: ignore

    def AddRequestLobbyListNumericalFilter(self, pchKeyToMatch, nValueToMatch, eComparisonType):
        return ISteamMatchmaking_AddRequestLobbyListNumericalFilter(byref(self), pchKeyToMatch, nValueToMatch, eComparisonType) # type: ignore

    def AddRequestLobbyListNearValueFilter(self, pchKeyToMatch, nValueToBeCloseTo):
        return ISteamMatchmaking_AddRequestLobbyListNearValueFilter(byref(self), pchKeyToMatch, nValueToBeCloseTo) # type: ignore

    def AddRequestLobbyListFilterSlotsAvailable(self, nSlotsAvailable):
        return ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable(byref(self), nSlotsAvailable) # type: ignore

    def AddRequestLobbyListDistanceFilter(self, eLobbyDistanceFilter):
        return ISteamMatchmaking_AddRequestLobbyListDistanceFilter(byref(self), eLobbyDistanceFilter) # type: ignore

    def AddRequestLobbyListResultCountFilter(self, cMaxResults):
        return ISteamMatchmaking_AddRequestLobbyListResultCountFilter(byref(self), cMaxResults) # type: ignore

    def AddRequestLobbyListCompatibleMembersFilter(self, steamIDLobby):
        return ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter(byref(self), steamIDLobby) # type: ignore

    def GetLobbyByIndex(self, iLobby):
        return ISteamMatchmaking_GetLobbyByIndex(byref(self), iLobby) # type: ignore

    def CreateLobby(self, eLobbyType, cMaxMembers):
        return ISteamMatchmaking_CreateLobby(byref(self), eLobbyType, cMaxMembers) # type: ignore

    def JoinLobby(self, steamIDLobby):
        return ISteamMatchmaking_JoinLobby(byref(self), steamIDLobby) # type: ignore

    def LeaveLobby(self, steamIDLobby):
        return ISteamMatchmaking_LeaveLobby(byref(self), steamIDLobby) # type: ignore

    def InviteUserToLobby(self, steamIDLobby, steamIDInvitee):
        return ISteamMatchmaking_InviteUserToLobby(byref(self), steamIDLobby, steamIDInvitee) # type: ignore

    def GetNumLobbyMembers(self, steamIDLobby):
        return ISteamMatchmaking_GetNumLobbyMembers(byref(self), steamIDLobby) # type: ignore

    def GetLobbyMemberByIndex(self, steamIDLobby, iMember):
        return ISteamMatchmaking_GetLobbyMemberByIndex(byref(self), steamIDLobby, iMember) # type: ignore

    def GetLobbyData(self, steamIDLobby, pchKey):
        return ISteamMatchmaking_GetLobbyData(byref(self), steamIDLobby, pchKey) # type: ignore

    def SetLobbyData(self, steamIDLobby, pchKey, pchValue):
        return ISteamMatchmaking_SetLobbyData(byref(self), steamIDLobby, pchKey, pchValue) # type: ignore

    def GetLobbyDataCount(self, steamIDLobby):
        return ISteamMatchmaking_GetLobbyDataCount(byref(self), steamIDLobby) # type: ignore

    def GetLobbyDataByIndex(self, steamIDLobby, iLobbyData, pchKey, cchKeyBufferSize, pchValue, cchValueBufferSize):
        return ISteamMatchmaking_GetLobbyDataByIndex(byref(self), steamIDLobby, iLobbyData, pchKey, cchKeyBufferSize, pchValue, cchValueBufferSize) # type: ignore

    def DeleteLobbyData(self, steamIDLobby, pchKey):
        return ISteamMatchmaking_DeleteLobbyData(byref(self), steamIDLobby, pchKey) # type: ignore

    def GetLobbyMemberData(self, steamIDLobby, steamIDUser, pchKey):
        return ISteamMatchmaking_GetLobbyMemberData(byref(self), steamIDLobby, steamIDUser, pchKey) # type: ignore

    def SetLobbyMemberData(self, steamIDLobby, pchKey, pchValue):
        return ISteamMatchmaking_SetLobbyMemberData(byref(self), steamIDLobby, pchKey, pchValue) # type: ignore

    def SendLobbyChatMsg(self, steamIDLobby, pvMsgBody, cubMsgBody):
        return ISteamMatchmaking_SendLobbyChatMsg(byref(self), steamIDLobby, pvMsgBody, cubMsgBody) # type: ignore

    def GetLobbyChatEntry(self, steamIDLobby, iChatID, pSteamIDUser, pvData, cubData, peChatEntryType):
        return ISteamMatchmaking_GetLobbyChatEntry(byref(self), steamIDLobby, iChatID, pSteamIDUser, pvData, cubData, peChatEntryType) # type: ignore

    def RequestLobbyData(self, steamIDLobby):
        return ISteamMatchmaking_RequestLobbyData(byref(self), steamIDLobby) # type: ignore

    def SetLobbyGameServer(self, steamIDLobby, unGameServerIP, unGameServerPort, steamIDGameServer):
        return ISteamMatchmaking_SetLobbyGameServer(byref(self), steamIDLobby, unGameServerIP, unGameServerPort, steamIDGameServer) # type: ignore

    def GetLobbyGameServer(self, steamIDLobby, punGameServerIP, punGameServerPort, psteamIDGameServer):
        return ISteamMatchmaking_GetLobbyGameServer(byref(self), steamIDLobby, punGameServerIP, punGameServerPort, psteamIDGameServer) # type: ignore

    def SetLobbyMemberLimit(self, steamIDLobby, cMaxMembers):
        return ISteamMatchmaking_SetLobbyMemberLimit(byref(self), steamIDLobby, cMaxMembers) # type: ignore

    def GetLobbyMemberLimit(self, steamIDLobby):
        return ISteamMatchmaking_GetLobbyMemberLimit(byref(self), steamIDLobby) # type: ignore

    def SetLobbyType(self, steamIDLobby, eLobbyType):
        return ISteamMatchmaking_SetLobbyType(byref(self), steamIDLobby, eLobbyType) # type: ignore

    def SetLobbyJoinable(self, steamIDLobby, bLobbyJoinable):
        return ISteamMatchmaking_SetLobbyJoinable(byref(self), steamIDLobby, bLobbyJoinable) # type: ignore

    def GetLobbyOwner(self, steamIDLobby):
        return ISteamMatchmaking_GetLobbyOwner(byref(self), steamIDLobby) # type: ignore

    def SetLobbyOwner(self, steamIDLobby, steamIDNewOwner):
        return ISteamMatchmaking_SetLobbyOwner(byref(self), steamIDLobby, steamIDNewOwner) # type: ignore

    def SetLinkedLobby(self, steamIDLobby, steamIDLobbyDependent):
        return ISteamMatchmaking_SetLinkedLobby(byref(self), steamIDLobby, steamIDLobbyDependent) # type: ignore

class ISteamMatchmakingServerListResponse(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def ServerResponded(self, hRequest, iServer):
        return ISteamMatchmakingServerListResponse_ServerResponded(byref(self), hRequest, iServer) # type: ignore

    def ServerFailedToRespond(self, hRequest, iServer):
        return ISteamMatchmakingServerListResponse_ServerFailedToRespond(byref(self), hRequest, iServer) # type: ignore

    def RefreshComplete(self, hRequest, response):
        return ISteamMatchmakingServerListResponse_RefreshComplete(byref(self), hRequest, response) # type: ignore

class ISteamMatchmakingPingResponse(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def ServerResponded(self, server):
        return ISteamMatchmakingPingResponse_ServerResponded(byref(self), server) # type: ignore

    def ServerFailedToRespond(self, ):
        return ISteamMatchmakingPingResponse_ServerFailedToRespond(byref(self), ) # type: ignore

class ISteamMatchmakingPlayersResponse(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def AddPlayerToList(self, pchName, nScore, flTimePlayed):
        return ISteamMatchmakingPlayersResponse_AddPlayerToList(byref(self), pchName, nScore, flTimePlayed) # type: ignore

    def PlayersFailedToRespond(self, ):
        return ISteamMatchmakingPlayersResponse_PlayersFailedToRespond(byref(self), ) # type: ignore

    def PlayersRefreshComplete(self, ):
        return ISteamMatchmakingPlayersResponse_PlayersRefreshComplete(byref(self), ) # type: ignore

class ISteamMatchmakingRulesResponse(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def RulesResponded(self, pchRule, pchValue):
        return ISteamMatchmakingRulesResponse_RulesResponded(byref(self), pchRule, pchValue) # type: ignore

    def RulesFailedToRespond(self, ):
        return ISteamMatchmakingRulesResponse_RulesFailedToRespond(byref(self), ) # type: ignore

    def RulesRefreshComplete(self, ):
        return ISteamMatchmakingRulesResponse_RulesRefreshComplete(byref(self), ) # type: ignore

class ISteamMatchmakingServers(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def RequestInternetServerList(self, iApp, ppchFilters, nFilters, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestInternetServerList(byref(self), iApp, ppchFilters, nFilters, pRequestServersResponse) # type: ignore

    def RequestLANServerList(self, iApp, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestLANServerList(byref(self), iApp, pRequestServersResponse) # type: ignore

    def RequestFriendsServerList(self, iApp, ppchFilters, nFilters, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestFriendsServerList(byref(self), iApp, ppchFilters, nFilters, pRequestServersResponse) # type: ignore

    def RequestFavoritesServerList(self, iApp, ppchFilters, nFilters, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestFavoritesServerList(byref(self), iApp, ppchFilters, nFilters, pRequestServersResponse) # type: ignore

    def RequestHistoryServerList(self, iApp, ppchFilters, nFilters, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestHistoryServerList(byref(self), iApp, ppchFilters, nFilters, pRequestServersResponse) # type: ignore

    def RequestSpectatorServerList(self, iApp, ppchFilters, nFilters, pRequestServersResponse):
        return ISteamMatchmakingServers_RequestSpectatorServerList(byref(self), iApp, ppchFilters, nFilters, pRequestServersResponse) # type: ignore

    def ReleaseRequest(self, hServerListRequest):
        return ISteamMatchmakingServers_ReleaseRequest(byref(self), hServerListRequest) # type: ignore

    def GetServerDetails(self, hRequest, iServer):
        return ISteamMatchmakingServers_GetServerDetails(byref(self), hRequest, iServer) # type: ignore

    def CancelQuery(self, hRequest):
        return ISteamMatchmakingServers_CancelQuery(byref(self), hRequest) # type: ignore

    def RefreshQuery(self, hRequest):
        return ISteamMatchmakingServers_RefreshQuery(byref(self), hRequest) # type: ignore

    def IsRefreshing(self, hRequest):
        return ISteamMatchmakingServers_IsRefreshing(byref(self), hRequest) # type: ignore

    def GetServerCount(self, hRequest):
        return ISteamMatchmakingServers_GetServerCount(byref(self), hRequest) # type: ignore

    def RefreshServer(self, hRequest, iServer):
        return ISteamMatchmakingServers_RefreshServer(byref(self), hRequest, iServer) # type: ignore

    def PingServer(self, unIP, usPort, pRequestServersResponse):
        return ISteamMatchmakingServers_PingServer(byref(self), unIP, usPort, pRequestServersResponse) # type: ignore

    def PlayerDetails(self, unIP, usPort, pRequestServersResponse):
        return ISteamMatchmakingServers_PlayerDetails(byref(self), unIP, usPort, pRequestServersResponse) # type: ignore

    def ServerRules(self, unIP, usPort, pRequestServersResponse):
        return ISteamMatchmakingServers_ServerRules(byref(self), unIP, usPort, pRequestServersResponse) # type: ignore

    def CancelServerQuery(self, hServerQuery):
        return ISteamMatchmakingServers_CancelServerQuery(byref(self), hServerQuery) # type: ignore

class ISteamGameSearch(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def AddGameSearchParams(self, pchKeyToFind, pchValuesToFind):
        return ISteamGameSearch_AddGameSearchParams(byref(self), pchKeyToFind, pchValuesToFind) # type: ignore

    def SearchForGameWithLobby(self, steamIDLobby, nPlayerMin, nPlayerMax):
        return ISteamGameSearch_SearchForGameWithLobby(byref(self), steamIDLobby, nPlayerMin, nPlayerMax) # type: ignore

    def SearchForGameSolo(self, nPlayerMin, nPlayerMax):
        return ISteamGameSearch_SearchForGameSolo(byref(self), nPlayerMin, nPlayerMax) # type: ignore

    def AcceptGame(self, ):
        return ISteamGameSearch_AcceptGame(byref(self), ) # type: ignore

    def DeclineGame(self, ):
        return ISteamGameSearch_DeclineGame(byref(self), ) # type: ignore

    def RetrieveConnectionDetails(self, steamIDHost, pchConnectionDetails, cubConnectionDetails):
        return ISteamGameSearch_RetrieveConnectionDetails(byref(self), steamIDHost, pchConnectionDetails, cubConnectionDetails) # type: ignore

    def EndGameSearch(self, ):
        return ISteamGameSearch_EndGameSearch(byref(self), ) # type: ignore

    def SetGameHostParams(self, pchKey, pchValue):
        return ISteamGameSearch_SetGameHostParams(byref(self), pchKey, pchValue) # type: ignore

    def SetConnectionDetails(self, pchConnectionDetails, cubConnectionDetails):
        return ISteamGameSearch_SetConnectionDetails(byref(self), pchConnectionDetails, cubConnectionDetails) # type: ignore

    def RequestPlayersForGame(self, nPlayerMin, nPlayerMax, nMaxTeamSize):
        return ISteamGameSearch_RequestPlayersForGame(byref(self), nPlayerMin, nPlayerMax, nMaxTeamSize) # type: ignore

    def HostConfirmGameStart(self, ullUniqueGameID):
        return ISteamGameSearch_HostConfirmGameStart(byref(self), ullUniqueGameID) # type: ignore

    def CancelRequestPlayersForGame(self, ):
        return ISteamGameSearch_CancelRequestPlayersForGame(byref(self), ) # type: ignore

    def SubmitPlayerResult(self, ullUniqueGameID, steamIDPlayer, EPlayerResult):
        return ISteamGameSearch_SubmitPlayerResult(byref(self), ullUniqueGameID, steamIDPlayer, EPlayerResult) # type: ignore

    def EndGame(self, ullUniqueGameID):
        return ISteamGameSearch_EndGame(byref(self), ullUniqueGameID) # type: ignore

class ISteamParties(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetNumActiveBeacons(self, ):
        return ISteamParties_GetNumActiveBeacons(byref(self), ) # type: ignore

    def GetBeaconByIndex(self, unIndex):
        return ISteamParties_GetBeaconByIndex(byref(self), unIndex) # type: ignore

    def GetBeaconDetails(self, ulBeaconID, pSteamIDBeaconOwner, pLocation, pchMetadata, cchMetadata):
        return ISteamParties_GetBeaconDetails(byref(self), ulBeaconID, pSteamIDBeaconOwner, pLocation, pchMetadata, cchMetadata) # type: ignore

    def JoinParty(self, ulBeaconID):
        return ISteamParties_JoinParty(byref(self), ulBeaconID) # type: ignore

    def GetNumAvailableBeaconLocations(self, puNumLocations):
        return ISteamParties_GetNumAvailableBeaconLocations(byref(self), puNumLocations) # type: ignore

    def GetAvailableBeaconLocations(self, pLocationList, uMaxNumLocations):
        return ISteamParties_GetAvailableBeaconLocations(byref(self), pLocationList, uMaxNumLocations) # type: ignore

    def CreateBeacon(self, unOpenSlots, pBeaconLocation, pchConnectString, pchMetadata):
        return ISteamParties_CreateBeacon(byref(self), unOpenSlots, pBeaconLocation, pchConnectString, pchMetadata) # type: ignore

    def OnReservationCompleted(self, ulBeacon, steamIDUser):
        return ISteamParties_OnReservationCompleted(byref(self), ulBeacon, steamIDUser) # type: ignore

    def CancelReservation(self, ulBeacon, steamIDUser):
        return ISteamParties_CancelReservation(byref(self), ulBeacon, steamIDUser) # type: ignore

    def ChangeNumOpenSlots(self, ulBeacon, unOpenSlots):
        return ISteamParties_ChangeNumOpenSlots(byref(self), ulBeacon, unOpenSlots) # type: ignore

    def DestroyBeacon(self, ulBeacon):
        return ISteamParties_DestroyBeacon(byref(self), ulBeacon) # type: ignore

    def GetBeaconLocationData(self, BeaconLocation, eData, pchDataStringOut, cchDataStringOut):
        return ISteamParties_GetBeaconLocationData(byref(self), BeaconLocation, eData, pchDataStringOut, cchDataStringOut) # type: ignore

class ISteamRemoteStorage(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def FileWrite(self, pchFile, pvData, cubData):
        return ISteamRemoteStorage_FileWrite(byref(self), pchFile, pvData, cubData) # type: ignore

    def FileRead(self, pchFile, pvData, cubDataToRead):
        return ISteamRemoteStorage_FileRead(byref(self), pchFile, pvData, cubDataToRead) # type: ignore

    def FileWriteAsync(self, pchFile, pvData, cubData):
        return ISteamRemoteStorage_FileWriteAsync(byref(self), pchFile, pvData, cubData) # type: ignore

    def FileReadAsync(self, pchFile, nOffset, cubToRead):
        return ISteamRemoteStorage_FileReadAsync(byref(self), pchFile, nOffset, cubToRead) # type: ignore

    def FileReadAsyncComplete(self, hReadCall, pvBuffer, cubToRead):
        return ISteamRemoteStorage_FileReadAsyncComplete(byref(self), hReadCall, pvBuffer, cubToRead) # type: ignore

    def FileForget(self, pchFile):
        return ISteamRemoteStorage_FileForget(byref(self), pchFile) # type: ignore

    def FileDelete(self, pchFile):
        return ISteamRemoteStorage_FileDelete(byref(self), pchFile) # type: ignore

    def FileShare(self, pchFile):
        return ISteamRemoteStorage_FileShare(byref(self), pchFile) # type: ignore

    def SetSyncPlatforms(self, pchFile, eRemoteStoragePlatform):
        return ISteamRemoteStorage_SetSyncPlatforms(byref(self), pchFile, eRemoteStoragePlatform) # type: ignore

    def FileWriteStreamOpen(self, pchFile):
        return ISteamRemoteStorage_FileWriteStreamOpen(byref(self), pchFile) # type: ignore

    def FileWriteStreamWriteChunk(self, writeHandle, pvData, cubData):
        return ISteamRemoteStorage_FileWriteStreamWriteChunk(byref(self), writeHandle, pvData, cubData) # type: ignore

    def FileWriteStreamClose(self, writeHandle):
        return ISteamRemoteStorage_FileWriteStreamClose(byref(self), writeHandle) # type: ignore

    def FileWriteStreamCancel(self, writeHandle):
        return ISteamRemoteStorage_FileWriteStreamCancel(byref(self), writeHandle) # type: ignore

    def FileExists(self, pchFile):
        return ISteamRemoteStorage_FileExists(byref(self), pchFile) # type: ignore

    def FilePersisted(self, pchFile):
        return ISteamRemoteStorage_FilePersisted(byref(self), pchFile) # type: ignore

    def GetFileSize(self, pchFile):
        return ISteamRemoteStorage_GetFileSize(byref(self), pchFile) # type: ignore

    def GetFileTimestamp(self, pchFile):
        return ISteamRemoteStorage_GetFileTimestamp(byref(self), pchFile) # type: ignore

    def GetSyncPlatforms(self, pchFile):
        return ISteamRemoteStorage_GetSyncPlatforms(byref(self), pchFile) # type: ignore

    def GetFileCount(self, ):
        return ISteamRemoteStorage_GetFileCount(byref(self), ) # type: ignore

    def GetFileNameAndSize(self, iFile, pnFileSizeInBytes):
        return ISteamRemoteStorage_GetFileNameAndSize(byref(self), iFile, pnFileSizeInBytes) # type: ignore

    def GetQuota(self, pnTotalBytes, puAvailableBytes):
        return ISteamRemoteStorage_GetQuota(byref(self), pnTotalBytes, puAvailableBytes) # type: ignore

    def IsCloudEnabledForAccount(self, ):
        return ISteamRemoteStorage_IsCloudEnabledForAccount(byref(self), ) # type: ignore

    def IsCloudEnabledForApp(self, ):
        return ISteamRemoteStorage_IsCloudEnabledForApp(byref(self), ) # type: ignore

    def SetCloudEnabledForApp(self, bEnabled):
        return ISteamRemoteStorage_SetCloudEnabledForApp(byref(self), bEnabled) # type: ignore

    def UGCDownload(self, hContent, unPriority):
        return ISteamRemoteStorage_UGCDownload(byref(self), hContent, unPriority) # type: ignore

    def GetUGCDownloadProgress(self, hContent, pnBytesDownloaded, pnBytesExpected):
        return ISteamRemoteStorage_GetUGCDownloadProgress(byref(self), hContent, pnBytesDownloaded, pnBytesExpected) # type: ignore

    def GetUGCDetails(self, hContent, pnAppID, ppchName, pnFileSizeInBytes, pSteamIDOwner):
        return ISteamRemoteStorage_GetUGCDetails(byref(self), hContent, pnAppID, ppchName, pnFileSizeInBytes, pSteamIDOwner) # type: ignore

    def UGCRead(self, hContent, pvData, cubDataToRead, cOffset, eAction):
        return ISteamRemoteStorage_UGCRead(byref(self), hContent, pvData, cubDataToRead, cOffset, eAction) # type: ignore

    def GetCachedUGCCount(self, ):
        return ISteamRemoteStorage_GetCachedUGCCount(byref(self), ) # type: ignore

    def GetCachedUGCHandle(self, iCachedContent):
        return ISteamRemoteStorage_GetCachedUGCHandle(byref(self), iCachedContent) # type: ignore

    def PublishWorkshopFile(self, pchFile, pchPreviewFile, nConsumerAppId, pchTitle, pchDescription, eVisibility, pTags, eWorkshopFileType):
        return ISteamRemoteStorage_PublishWorkshopFile(byref(self), pchFile, pchPreviewFile, nConsumerAppId, pchTitle, pchDescription, eVisibility, pTags, eWorkshopFileType) # type: ignore

    def CreatePublishedFileUpdateRequest(self, unPublishedFileId):
        return ISteamRemoteStorage_CreatePublishedFileUpdateRequest(byref(self), unPublishedFileId) # type: ignore

    def UpdatePublishedFileFile(self, updateHandle, pchFile):
        return ISteamRemoteStorage_UpdatePublishedFileFile(byref(self), updateHandle, pchFile) # type: ignore

    def UpdatePublishedFilePreviewFile(self, updateHandle, pchPreviewFile):
        return ISteamRemoteStorage_UpdatePublishedFilePreviewFile(byref(self), updateHandle, pchPreviewFile) # type: ignore

    def UpdatePublishedFileTitle(self, updateHandle, pchTitle):
        return ISteamRemoteStorage_UpdatePublishedFileTitle(byref(self), updateHandle, pchTitle) # type: ignore

    def UpdatePublishedFileDescription(self, updateHandle, pchDescription):
        return ISteamRemoteStorage_UpdatePublishedFileDescription(byref(self), updateHandle, pchDescription) # type: ignore

    def UpdatePublishedFileVisibility(self, updateHandle, eVisibility):
        return ISteamRemoteStorage_UpdatePublishedFileVisibility(byref(self), updateHandle, eVisibility) # type: ignore

    def UpdatePublishedFileTags(self, updateHandle, pTags):
        return ISteamRemoteStorage_UpdatePublishedFileTags(byref(self), updateHandle, pTags) # type: ignore

    def CommitPublishedFileUpdate(self, updateHandle):
        return ISteamRemoteStorage_CommitPublishedFileUpdate(byref(self), updateHandle) # type: ignore

    def GetPublishedFileDetails(self, unPublishedFileId, unMaxSecondsOld):
        return ISteamRemoteStorage_GetPublishedFileDetails(byref(self), unPublishedFileId, unMaxSecondsOld) # type: ignore

    def DeletePublishedFile(self, unPublishedFileId):
        return ISteamRemoteStorage_DeletePublishedFile(byref(self), unPublishedFileId) # type: ignore

    def EnumerateUserPublishedFiles(self, unStartIndex):
        return ISteamRemoteStorage_EnumerateUserPublishedFiles(byref(self), unStartIndex) # type: ignore

    def SubscribePublishedFile(self, unPublishedFileId):
        return ISteamRemoteStorage_SubscribePublishedFile(byref(self), unPublishedFileId) # type: ignore

    def EnumerateUserSubscribedFiles(self, unStartIndex):
        return ISteamRemoteStorage_EnumerateUserSubscribedFiles(byref(self), unStartIndex) # type: ignore

    def UnsubscribePublishedFile(self, unPublishedFileId):
        return ISteamRemoteStorage_UnsubscribePublishedFile(byref(self), unPublishedFileId) # type: ignore

    def UpdatePublishedFileSetChangeDescription(self, updateHandle, pchChangeDescription):
        return ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription(byref(self), updateHandle, pchChangeDescription) # type: ignore

    def GetPublishedItemVoteDetails(self, unPublishedFileId):
        return ISteamRemoteStorage_GetPublishedItemVoteDetails(byref(self), unPublishedFileId) # type: ignore

    def UpdateUserPublishedItemVote(self, unPublishedFileId, bVoteUp):
        return ISteamRemoteStorage_UpdateUserPublishedItemVote(byref(self), unPublishedFileId, bVoteUp) # type: ignore

    def GetUserPublishedItemVoteDetails(self, unPublishedFileId):
        return ISteamRemoteStorage_GetUserPublishedItemVoteDetails(byref(self), unPublishedFileId) # type: ignore

    def EnumerateUserSharedWorkshopFiles(self, steamId, unStartIndex, pRequiredTags, pExcludedTags):
        return ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles(byref(self), steamId, unStartIndex, pRequiredTags, pExcludedTags) # type: ignore

    def PublishVideo(self, eVideoProvider, pchVideoAccount, pchVideoIdentifier, pchPreviewFile, nConsumerAppId, pchTitle, pchDescription, eVisibility, pTags):
        return ISteamRemoteStorage_PublishVideo(byref(self), eVideoProvider, pchVideoAccount, pchVideoIdentifier, pchPreviewFile, nConsumerAppId, pchTitle, pchDescription, eVisibility, pTags) # type: ignore

    def SetUserPublishedFileAction(self, unPublishedFileId, eAction):
        return ISteamRemoteStorage_SetUserPublishedFileAction(byref(self), unPublishedFileId, eAction) # type: ignore

    def EnumeratePublishedFilesByUserAction(self, eAction, unStartIndex):
        return ISteamRemoteStorage_EnumeratePublishedFilesByUserAction(byref(self), eAction, unStartIndex) # type: ignore

    def EnumeratePublishedWorkshopFiles(self, eEnumerationType, unStartIndex, unCount, unDays, pTags, pUserTags):
        return ISteamRemoteStorage_EnumeratePublishedWorkshopFiles(byref(self), eEnumerationType, unStartIndex, unCount, unDays, pTags, pUserTags) # type: ignore

    def UGCDownloadToLocation(self, hContent, pchLocation, unPriority):
        return ISteamRemoteStorage_UGCDownloadToLocation(byref(self), hContent, pchLocation, unPriority) # type: ignore

    def GetLocalFileChangeCount(self, ):
        return ISteamRemoteStorage_GetLocalFileChangeCount(byref(self), ) # type: ignore

    def GetLocalFileChange(self, iFile, pEChangeType, pEFilePathType):
        return ISteamRemoteStorage_GetLocalFileChange(byref(self), iFile, pEChangeType, pEFilePathType) # type: ignore

    def BeginFileWriteBatch(self, ):
        return ISteamRemoteStorage_BeginFileWriteBatch(byref(self), ) # type: ignore

    def EndFileWriteBatch(self, ):
        return ISteamRemoteStorage_EndFileWriteBatch(byref(self), ) # type: ignore

class ISteamUserStats(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def RequestCurrentStats(self, ):
        return ISteamUserStats_RequestCurrentStats(byref(self), ) # type: ignore

    def GetStatInt32(self, pchName, pData):
        return ISteamUserStats_GetStatInt32(byref(self), pchName, pData) # type: ignore

    def GetStatFloat(self, pchName, pData):
        return ISteamUserStats_GetStatFloat(byref(self), pchName, pData) # type: ignore

    def SetStatInt32(self, pchName, nData):
        return ISteamUserStats_SetStatInt32(byref(self), pchName, nData) # type: ignore

    def SetStatFloat(self, pchName, fData):
        return ISteamUserStats_SetStatFloat(byref(self), pchName, fData) # type: ignore

    def UpdateAvgRateStat(self, pchName, flCountThisSession, dSessionLength):
        return ISteamUserStats_UpdateAvgRateStat(byref(self), pchName, flCountThisSession, dSessionLength) # type: ignore

    def GetAchievement(self, pchName, pbAchieved):
        return ISteamUserStats_GetAchievement(byref(self), pchName, pbAchieved) # type: ignore

    def SetAchievement(self, pchName):
        return ISteamUserStats_SetAchievement(byref(self), pchName) # type: ignore

    def ClearAchievement(self, pchName):
        return ISteamUserStats_ClearAchievement(byref(self), pchName) # type: ignore

    def GetAchievementAndUnlockTime(self, pchName, pbAchieved, punUnlockTime):
        return ISteamUserStats_GetAchievementAndUnlockTime(byref(self), pchName, pbAchieved, punUnlockTime) # type: ignore

    def StoreStats(self, ):
        return ISteamUserStats_StoreStats(byref(self), ) # type: ignore

    def GetAchievementIcon(self, pchName):
        return ISteamUserStats_GetAchievementIcon(byref(self), pchName) # type: ignore

    def GetAchievementDisplayAttribute(self, pchName, pchKey):
        return ISteamUserStats_GetAchievementDisplayAttribute(byref(self), pchName, pchKey) # type: ignore

    def IndicateAchievementProgress(self, pchName, nCurProgress, nMaxProgress):
        return ISteamUserStats_IndicateAchievementProgress(byref(self), pchName, nCurProgress, nMaxProgress) # type: ignore

    def GetNumAchievements(self, ):
        return ISteamUserStats_GetNumAchievements(byref(self), ) # type: ignore

    def GetAchievementName(self, iAchievement):
        return ISteamUserStats_GetAchievementName(byref(self), iAchievement) # type: ignore

    def RequestUserStats(self, steamIDUser):
        return ISteamUserStats_RequestUserStats(byref(self), steamIDUser) # type: ignore

    def GetUserStatInt32(self, steamIDUser, pchName, pData):
        return ISteamUserStats_GetUserStatInt32(byref(self), steamIDUser, pchName, pData) # type: ignore

    def GetUserStatFloat(self, steamIDUser, pchName, pData):
        return ISteamUserStats_GetUserStatFloat(byref(self), steamIDUser, pchName, pData) # type: ignore

    def GetUserAchievement(self, steamIDUser, pchName, pbAchieved):
        return ISteamUserStats_GetUserAchievement(byref(self), steamIDUser, pchName, pbAchieved) # type: ignore

    def GetUserAchievementAndUnlockTime(self, steamIDUser, pchName, pbAchieved, punUnlockTime):
        return ISteamUserStats_GetUserAchievementAndUnlockTime(byref(self), steamIDUser, pchName, pbAchieved, punUnlockTime) # type: ignore

    def ResetAllStats(self, bAchievementsToo):
        return ISteamUserStats_ResetAllStats(byref(self), bAchievementsToo) # type: ignore

    def FindOrCreateLeaderboard(self, pchLeaderboardName, eLeaderboardSortMethod, eLeaderboardDisplayType):
        return ISteamUserStats_FindOrCreateLeaderboard(byref(self), pchLeaderboardName, eLeaderboardSortMethod, eLeaderboardDisplayType) # type: ignore

    def FindLeaderboard(self, pchLeaderboardName):
        return ISteamUserStats_FindLeaderboard(byref(self), pchLeaderboardName) # type: ignore

    def GetLeaderboardName(self, hSteamLeaderboard):
        return ISteamUserStats_GetLeaderboardName(byref(self), hSteamLeaderboard) # type: ignore

    def GetLeaderboardEntryCount(self, hSteamLeaderboard):
        return ISteamUserStats_GetLeaderboardEntryCount(byref(self), hSteamLeaderboard) # type: ignore

    def GetLeaderboardSortMethod(self, hSteamLeaderboard):
        return ISteamUserStats_GetLeaderboardSortMethod(byref(self), hSteamLeaderboard) # type: ignore

    def GetLeaderboardDisplayType(self, hSteamLeaderboard):
        return ISteamUserStats_GetLeaderboardDisplayType(byref(self), hSteamLeaderboard) # type: ignore

    def DownloadLeaderboardEntries(self, hSteamLeaderboard, eLeaderboardDataRequest, nRangeStart, nRangeEnd):
        return ISteamUserStats_DownloadLeaderboardEntries(byref(self), hSteamLeaderboard, eLeaderboardDataRequest, nRangeStart, nRangeEnd) # type: ignore

    def DownloadLeaderboardEntriesForUsers(self, hSteamLeaderboard, prgUsers, cUsers):
        return ISteamUserStats_DownloadLeaderboardEntriesForUsers(byref(self), hSteamLeaderboard, prgUsers, cUsers) # type: ignore

    def GetDownloadedLeaderboardEntry(self, hSteamLeaderboardEntries, index, pLeaderboardEntry, pDetails, cDetailsMax):
        return ISteamUserStats_GetDownloadedLeaderboardEntry(byref(self), hSteamLeaderboardEntries, index, pLeaderboardEntry, pDetails, cDetailsMax) # type: ignore

    def UploadLeaderboardScore(self, hSteamLeaderboard, eLeaderboardUploadScoreMethod, nScore, pScoreDetails, cScoreDetailsCount):
        return ISteamUserStats_UploadLeaderboardScore(byref(self), hSteamLeaderboard, eLeaderboardUploadScoreMethod, nScore, pScoreDetails, cScoreDetailsCount) # type: ignore

    def AttachLeaderboardUGC(self, hSteamLeaderboard, hUGC):
        return ISteamUserStats_AttachLeaderboardUGC(byref(self), hSteamLeaderboard, hUGC) # type: ignore

    def GetNumberOfCurrentPlayers(self, ):
        return ISteamUserStats_GetNumberOfCurrentPlayers(byref(self), ) # type: ignore

    def RequestGlobalAchievementPercentages(self, ):
        return ISteamUserStats_RequestGlobalAchievementPercentages(byref(self), ) # type: ignore

    def GetMostAchievedAchievementInfo(self, pchName, unNameBufLen, pflPercent, pbAchieved):
        return ISteamUserStats_GetMostAchievedAchievementInfo(byref(self), pchName, unNameBufLen, pflPercent, pbAchieved) # type: ignore

    def GetNextMostAchievedAchievementInfo(self, iIteratorPrevious, pchName, unNameBufLen, pflPercent, pbAchieved):
        return ISteamUserStats_GetNextMostAchievedAchievementInfo(byref(self), iIteratorPrevious, pchName, unNameBufLen, pflPercent, pbAchieved) # type: ignore

    def GetAchievementAchievedPercent(self, pchName, pflPercent):
        return ISteamUserStats_GetAchievementAchievedPercent(byref(self), pchName, pflPercent) # type: ignore

    def RequestGlobalStats(self, nHistoryDays):
        return ISteamUserStats_RequestGlobalStats(byref(self), nHistoryDays) # type: ignore

    def GetGlobalStatInt64(self, pchStatName, pData):
        return ISteamUserStats_GetGlobalStatInt64(byref(self), pchStatName, pData) # type: ignore

    def GetGlobalStatDouble(self, pchStatName, pData):
        return ISteamUserStats_GetGlobalStatDouble(byref(self), pchStatName, pData) # type: ignore

    def GetGlobalStatHistoryInt64(self, pchStatName, pData, cubData):
        return ISteamUserStats_GetGlobalStatHistoryInt64(byref(self), pchStatName, pData, cubData) # type: ignore

    def GetGlobalStatHistoryDouble(self, pchStatName, pData, cubData):
        return ISteamUserStats_GetGlobalStatHistoryDouble(byref(self), pchStatName, pData, cubData) # type: ignore

    def GetAchievementProgressLimitsInt32(self, pchName, pnMinProgress, pnMaxProgress):
        return ISteamUserStats_GetAchievementProgressLimitsInt32(byref(self), pchName, pnMinProgress, pnMaxProgress) # type: ignore

    def GetAchievementProgressLimitsFloat(self, pchName, pfMinProgress, pfMaxProgress):
        return ISteamUserStats_GetAchievementProgressLimitsFloat(byref(self), pchName, pfMinProgress, pfMaxProgress) # type: ignore

class ISteamApps(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def BIsSubscribed(self, ):
        return ISteamApps_BIsSubscribed(byref(self), ) # type: ignore

    def BIsLowViolence(self, ):
        return ISteamApps_BIsLowViolence(byref(self), ) # type: ignore

    def BIsCybercafe(self, ):
        return ISteamApps_BIsCybercafe(byref(self), ) # type: ignore

    def BIsVACBanned(self, ):
        return ISteamApps_BIsVACBanned(byref(self), ) # type: ignore

    def GetCurrentGameLanguage(self, ):
        return ISteamApps_GetCurrentGameLanguage(byref(self), ) # type: ignore

    def GetAvailableGameLanguages(self, ):
        return ISteamApps_GetAvailableGameLanguages(byref(self), ) # type: ignore

    def BIsSubscribedApp(self, appID):
        return ISteamApps_BIsSubscribedApp(byref(self), appID) # type: ignore

    def BIsDlcInstalled(self, appID):
        return ISteamApps_BIsDlcInstalled(byref(self), appID) # type: ignore

    def GetEarliestPurchaseUnixTime(self, nAppID):
        return ISteamApps_GetEarliestPurchaseUnixTime(byref(self), nAppID) # type: ignore

    def BIsSubscribedFromFreeWeekend(self, ):
        return ISteamApps_BIsSubscribedFromFreeWeekend(byref(self), ) # type: ignore

    def GetDLCCount(self, ):
        return ISteamApps_GetDLCCount(byref(self), ) # type: ignore

    def BGetDLCDataByIndex(self, iDLC, pAppID, pbAvailable, pchName, cchNameBufferSize):
        return ISteamApps_BGetDLCDataByIndex(byref(self), iDLC, pAppID, pbAvailable, pchName, cchNameBufferSize) # type: ignore

    def InstallDLC(self, nAppID):
        return ISteamApps_InstallDLC(byref(self), nAppID) # type: ignore

    def UninstallDLC(self, nAppID):
        return ISteamApps_UninstallDLC(byref(self), nAppID) # type: ignore

    def RequestAppProofOfPurchaseKey(self, nAppID):
        return ISteamApps_RequestAppProofOfPurchaseKey(byref(self), nAppID) # type: ignore

    def GetCurrentBetaName(self, pchName, cchNameBufferSize):
        return ISteamApps_GetCurrentBetaName(byref(self), pchName, cchNameBufferSize) # type: ignore

    def MarkContentCorrupt(self, bMissingFilesOnly):
        return ISteamApps_MarkContentCorrupt(byref(self), bMissingFilesOnly) # type: ignore

    def GetInstalledDepots(self, appID, pvecDepots, cMaxDepots):
        return ISteamApps_GetInstalledDepots(byref(self), appID, pvecDepots, cMaxDepots) # type: ignore

    def GetAppInstallDir(self, appID, pchFolder, cchFolderBufferSize):
        return ISteamApps_GetAppInstallDir(byref(self), appID, pchFolder, cchFolderBufferSize) # type: ignore

    def BIsAppInstalled(self, appID):
        return ISteamApps_BIsAppInstalled(byref(self), appID) # type: ignore

    def GetAppOwner(self, ):
        return ISteamApps_GetAppOwner(byref(self), ) # type: ignore

    def GetLaunchQueryParam(self, pchKey):
        return ISteamApps_GetLaunchQueryParam(byref(self), pchKey) # type: ignore

    def GetDlcDownloadProgress(self, nAppID, punBytesDownloaded, punBytesTotal):
        return ISteamApps_GetDlcDownloadProgress(byref(self), nAppID, punBytesDownloaded, punBytesTotal) # type: ignore

    def GetAppBuildId(self, ):
        return ISteamApps_GetAppBuildId(byref(self), ) # type: ignore

    def RequestAllProofOfPurchaseKeys(self, ):
        return ISteamApps_RequestAllProofOfPurchaseKeys(byref(self), ) # type: ignore

    def GetFileDetails(self, pszFileName):
        return ISteamApps_GetFileDetails(byref(self), pszFileName) # type: ignore

    def GetLaunchCommandLine(self, pszCommandLine, cubCommandLine):
        return ISteamApps_GetLaunchCommandLine(byref(self), pszCommandLine, cubCommandLine) # type: ignore

    def BIsSubscribedFromFamilySharing(self, ):
        return ISteamApps_BIsSubscribedFromFamilySharing(byref(self), ) # type: ignore

    def BIsTimedTrial(self, punSecondsAllowed, punSecondsPlayed):
        return ISteamApps_BIsTimedTrial(byref(self), punSecondsAllowed, punSecondsPlayed) # type: ignore

class ISteamNetworking(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def SendP2PPacket(self, steamIDRemote, pubData, cubData, eP2PSendType, nChannel):
        return ISteamNetworking_SendP2PPacket(byref(self), steamIDRemote, pubData, cubData, eP2PSendType, nChannel) # type: ignore

    def IsP2PPacketAvailable(self, pcubMsgSize, nChannel):
        return ISteamNetworking_IsP2PPacketAvailable(byref(self), pcubMsgSize, nChannel) # type: ignore

    def ReadP2PPacket(self, pubDest, cubDest, pcubMsgSize, psteamIDRemote, nChannel):
        return ISteamNetworking_ReadP2PPacket(byref(self), pubDest, cubDest, pcubMsgSize, psteamIDRemote, nChannel) # type: ignore

    def AcceptP2PSessionWithUser(self, steamIDRemote):
        return ISteamNetworking_AcceptP2PSessionWithUser(byref(self), steamIDRemote) # type: ignore

    def CloseP2PSessionWithUser(self, steamIDRemote):
        return ISteamNetworking_CloseP2PSessionWithUser(byref(self), steamIDRemote) # type: ignore

    def CloseP2PChannelWithUser(self, steamIDRemote, nChannel):
        return ISteamNetworking_CloseP2PChannelWithUser(byref(self), steamIDRemote, nChannel) # type: ignore

    def GetP2PSessionState(self, steamIDRemote, pConnectionState):
        return ISteamNetworking_GetP2PSessionState(byref(self), steamIDRemote, pConnectionState) # type: ignore

    def AllowP2PPacketRelay(self, bAllow):
        return ISteamNetworking_AllowP2PPacketRelay(byref(self), bAllow) # type: ignore

    def CreateListenSocket(self, nVirtualP2PPort, nIP, nPort, bAllowUseOfPacketRelay):
        return ISteamNetworking_CreateListenSocket(byref(self), nVirtualP2PPort, nIP, nPort, bAllowUseOfPacketRelay) # type: ignore

    def CreateP2PConnectionSocket(self, steamIDTarget, nVirtualPort, nTimeoutSec, bAllowUseOfPacketRelay):
        return ISteamNetworking_CreateP2PConnectionSocket(byref(self), steamIDTarget, nVirtualPort, nTimeoutSec, bAllowUseOfPacketRelay) # type: ignore

    def CreateConnectionSocket(self, nIP, nPort, nTimeoutSec):
        return ISteamNetworking_CreateConnectionSocket(byref(self), nIP, nPort, nTimeoutSec) # type: ignore

    def DestroySocket(self, hSocket, bNotifyRemoteEnd):
        return ISteamNetworking_DestroySocket(byref(self), hSocket, bNotifyRemoteEnd) # type: ignore

    def DestroyListenSocket(self, hSocket, bNotifyRemoteEnd):
        return ISteamNetworking_DestroyListenSocket(byref(self), hSocket, bNotifyRemoteEnd) # type: ignore

    def SendDataOnSocket(self, hSocket, pubData, cubData, bReliable):
        return ISteamNetworking_SendDataOnSocket(byref(self), hSocket, pubData, cubData, bReliable) # type: ignore

    def IsDataAvailableOnSocket(self, hSocket, pcubMsgSize):
        return ISteamNetworking_IsDataAvailableOnSocket(byref(self), hSocket, pcubMsgSize) # type: ignore

    def RetrieveDataFromSocket(self, hSocket, pubDest, cubDest, pcubMsgSize):
        return ISteamNetworking_RetrieveDataFromSocket(byref(self), hSocket, pubDest, cubDest, pcubMsgSize) # type: ignore

    def IsDataAvailable(self, hListenSocket, pcubMsgSize, phSocket):
        return ISteamNetworking_IsDataAvailable(byref(self), hListenSocket, pcubMsgSize, phSocket) # type: ignore

    def RetrieveData(self, hListenSocket, pubDest, cubDest, pcubMsgSize, phSocket):
        return ISteamNetworking_RetrieveData(byref(self), hListenSocket, pubDest, cubDest, pcubMsgSize, phSocket) # type: ignore

    def GetSocketInfo(self, hSocket, pSteamIDRemote, peSocketStatus, punIPRemote, punPortRemote):
        return ISteamNetworking_GetSocketInfo(byref(self), hSocket, pSteamIDRemote, peSocketStatus, punIPRemote, punPortRemote) # type: ignore

    def GetListenSocketInfo(self, hListenSocket, pnIP, pnPort):
        return ISteamNetworking_GetListenSocketInfo(byref(self), hListenSocket, pnIP, pnPort) # type: ignore

    def GetSocketConnectionType(self, hSocket):
        return ISteamNetworking_GetSocketConnectionType(byref(self), hSocket) # type: ignore

    def GetMaxPacketSize(self, hSocket):
        return ISteamNetworking_GetMaxPacketSize(byref(self), hSocket) # type: ignore

class ISteamScreenshots(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def WriteScreenshot(self, pubRGB, cubRGB, nWidth, nHeight):
        return ISteamScreenshots_WriteScreenshot(byref(self), pubRGB, cubRGB, nWidth, nHeight) # type: ignore

    def AddScreenshotToLibrary(self, pchFilename, pchThumbnailFilename, nWidth, nHeight):
        return ISteamScreenshots_AddScreenshotToLibrary(byref(self), pchFilename, pchThumbnailFilename, nWidth, nHeight) # type: ignore

    def TriggerScreenshot(self, ):
        return ISteamScreenshots_TriggerScreenshot(byref(self), ) # type: ignore

    def HookScreenshots(self, bHook):
        return ISteamScreenshots_HookScreenshots(byref(self), bHook) # type: ignore

    def SetLocation(self, hScreenshot, pchLocation):
        return ISteamScreenshots_SetLocation(byref(self), hScreenshot, pchLocation) # type: ignore

    def TagUser(self, hScreenshot, steamID):
        return ISteamScreenshots_TagUser(byref(self), hScreenshot, steamID) # type: ignore

    def TagPublishedFile(self, hScreenshot, unPublishedFileID):
        return ISteamScreenshots_TagPublishedFile(byref(self), hScreenshot, unPublishedFileID) # type: ignore

    def IsScreenshotsHooked(self, ):
        return ISteamScreenshots_IsScreenshotsHooked(byref(self), ) # type: ignore

    def AddVRScreenshotToLibrary(self, eType, pchFilename, pchVRFilename):
        return ISteamScreenshots_AddVRScreenshotToLibrary(byref(self), eType, pchFilename, pchVRFilename) # type: ignore

class ISteamMusic(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def BIsEnabled(self, ):
        return ISteamMusic_BIsEnabled(byref(self), ) # type: ignore

    def BIsPlaying(self, ):
        return ISteamMusic_BIsPlaying(byref(self), ) # type: ignore

    def GetPlaybackStatus(self, ):
        return ISteamMusic_GetPlaybackStatus(byref(self), ) # type: ignore

    def Play(self, ):
        return ISteamMusic_Play(byref(self), ) # type: ignore

    def Pause(self, ):
        return ISteamMusic_Pause(byref(self), ) # type: ignore

    def PlayPrevious(self, ):
        return ISteamMusic_PlayPrevious(byref(self), ) # type: ignore

    def PlayNext(self, ):
        return ISteamMusic_PlayNext(byref(self), ) # type: ignore

    def SetVolume(self, flVolume):
        return ISteamMusic_SetVolume(byref(self), flVolume) # type: ignore

    def GetVolume(self, ):
        return ISteamMusic_GetVolume(byref(self), ) # type: ignore

class ISteamMusicRemote(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def RegisterSteamMusicRemote(self, pchName):
        return ISteamMusicRemote_RegisterSteamMusicRemote(byref(self), pchName) # type: ignore

    def DeregisterSteamMusicRemote(self, ):
        return ISteamMusicRemote_DeregisterSteamMusicRemote(byref(self), ) # type: ignore

    def BIsCurrentMusicRemote(self, ):
        return ISteamMusicRemote_BIsCurrentMusicRemote(byref(self), ) # type: ignore

    def BActivationSuccess(self, bValue):
        return ISteamMusicRemote_BActivationSuccess(byref(self), bValue) # type: ignore

    def SetDisplayName(self, pchDisplayName):
        return ISteamMusicRemote_SetDisplayName(byref(self), pchDisplayName) # type: ignore

    def SetPNGIcon_64x64(self, pvBuffer, cbBufferLength):
        return ISteamMusicRemote_SetPNGIcon_64x64(byref(self), pvBuffer, cbBufferLength) # type: ignore

    def EnablePlayPrevious(self, bValue):
        return ISteamMusicRemote_EnablePlayPrevious(byref(self), bValue) # type: ignore

    def EnablePlayNext(self, bValue):
        return ISteamMusicRemote_EnablePlayNext(byref(self), bValue) # type: ignore

    def EnableShuffled(self, bValue):
        return ISteamMusicRemote_EnableShuffled(byref(self), bValue) # type: ignore

    def EnableLooped(self, bValue):
        return ISteamMusicRemote_EnableLooped(byref(self), bValue) # type: ignore

    def EnableQueue(self, bValue):
        return ISteamMusicRemote_EnableQueue(byref(self), bValue) # type: ignore

    def EnablePlaylists(self, bValue):
        return ISteamMusicRemote_EnablePlaylists(byref(self), bValue) # type: ignore

    def UpdatePlaybackStatus(self, nStatus):
        return ISteamMusicRemote_UpdatePlaybackStatus(byref(self), nStatus) # type: ignore

    def UpdateShuffled(self, bValue):
        return ISteamMusicRemote_UpdateShuffled(byref(self), bValue) # type: ignore

    def UpdateLooped(self, bValue):
        return ISteamMusicRemote_UpdateLooped(byref(self), bValue) # type: ignore

    def UpdateVolume(self, flValue):
        return ISteamMusicRemote_UpdateVolume(byref(self), flValue) # type: ignore

    def CurrentEntryWillChange(self, ):
        return ISteamMusicRemote_CurrentEntryWillChange(byref(self), ) # type: ignore

    def CurrentEntryIsAvailable(self, bAvailable):
        return ISteamMusicRemote_CurrentEntryIsAvailable(byref(self), bAvailable) # type: ignore

    def UpdateCurrentEntryText(self, pchText):
        return ISteamMusicRemote_UpdateCurrentEntryText(byref(self), pchText) # type: ignore

    def UpdateCurrentEntryElapsedSeconds(self, nValue):
        return ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds(byref(self), nValue) # type: ignore

    def UpdateCurrentEntryCoverArt(self, pvBuffer, cbBufferLength):
        return ISteamMusicRemote_UpdateCurrentEntryCoverArt(byref(self), pvBuffer, cbBufferLength) # type: ignore

    def CurrentEntryDidChange(self, ):
        return ISteamMusicRemote_CurrentEntryDidChange(byref(self), ) # type: ignore

    def QueueWillChange(self, ):
        return ISteamMusicRemote_QueueWillChange(byref(self), ) # type: ignore

    def ResetQueueEntries(self, ):
        return ISteamMusicRemote_ResetQueueEntries(byref(self), ) # type: ignore

    def SetQueueEntry(self, nID, nPosition, pchEntryText):
        return ISteamMusicRemote_SetQueueEntry(byref(self), nID, nPosition, pchEntryText) # type: ignore

    def SetCurrentQueueEntry(self, nID):
        return ISteamMusicRemote_SetCurrentQueueEntry(byref(self), nID) # type: ignore

    def QueueDidChange(self, ):
        return ISteamMusicRemote_QueueDidChange(byref(self), ) # type: ignore

    def PlaylistWillChange(self, ):
        return ISteamMusicRemote_PlaylistWillChange(byref(self), ) # type: ignore

    def ResetPlaylistEntries(self, ):
        return ISteamMusicRemote_ResetPlaylistEntries(byref(self), ) # type: ignore

    def SetPlaylistEntry(self, nID, nPosition, pchEntryText):
        return ISteamMusicRemote_SetPlaylistEntry(byref(self), nID, nPosition, pchEntryText) # type: ignore

    def SetCurrentPlaylistEntry(self, nID):
        return ISteamMusicRemote_SetCurrentPlaylistEntry(byref(self), nID) # type: ignore

    def PlaylistDidChange(self, ):
        return ISteamMusicRemote_PlaylistDidChange(byref(self), ) # type: ignore

class ISteamHTTP(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def CreateHTTPRequest(self, eHTTPRequestMethod, pchAbsoluteURL):
        return ISteamHTTP_CreateHTTPRequest(byref(self), eHTTPRequestMethod, pchAbsoluteURL) # type: ignore

    def SetHTTPRequestContextValue(self, hRequest, ulContextValue):
        return ISteamHTTP_SetHTTPRequestContextValue(byref(self), hRequest, ulContextValue) # type: ignore

    def SetHTTPRequestNetworkActivityTimeout(self, hRequest, unTimeoutSeconds):
        return ISteamHTTP_SetHTTPRequestNetworkActivityTimeout(byref(self), hRequest, unTimeoutSeconds) # type: ignore

    def SetHTTPRequestHeaderValue(self, hRequest, pchHeaderName, pchHeaderValue):
        return ISteamHTTP_SetHTTPRequestHeaderValue(byref(self), hRequest, pchHeaderName, pchHeaderValue) # type: ignore

    def SetHTTPRequestGetOrPostParameter(self, hRequest, pchParamName, pchParamValue):
        return ISteamHTTP_SetHTTPRequestGetOrPostParameter(byref(self), hRequest, pchParamName, pchParamValue) # type: ignore

    def SendHTTPRequest(self, hRequest, pCallHandle):
        return ISteamHTTP_SendHTTPRequest(byref(self), hRequest, pCallHandle) # type: ignore

    def SendHTTPRequestAndStreamResponse(self, hRequest, pCallHandle):
        return ISteamHTTP_SendHTTPRequestAndStreamResponse(byref(self), hRequest, pCallHandle) # type: ignore

    def DeferHTTPRequest(self, hRequest):
        return ISteamHTTP_DeferHTTPRequest(byref(self), hRequest) # type: ignore

    def PrioritizeHTTPRequest(self, hRequest):
        return ISteamHTTP_PrioritizeHTTPRequest(byref(self), hRequest) # type: ignore

    def GetHTTPResponseHeaderSize(self, hRequest, pchHeaderName, unResponseHeaderSize):
        return ISteamHTTP_GetHTTPResponseHeaderSize(byref(self), hRequest, pchHeaderName, unResponseHeaderSize) # type: ignore

    def GetHTTPResponseHeaderValue(self, hRequest, pchHeaderName, pHeaderValueBuffer, unBufferSize):
        return ISteamHTTP_GetHTTPResponseHeaderValue(byref(self), hRequest, pchHeaderName, pHeaderValueBuffer, unBufferSize) # type: ignore

    def GetHTTPResponseBodySize(self, hRequest, unBodySize):
        return ISteamHTTP_GetHTTPResponseBodySize(byref(self), hRequest, unBodySize) # type: ignore

    def GetHTTPResponseBodyData(self, hRequest, pBodyDataBuffer, unBufferSize):
        return ISteamHTTP_GetHTTPResponseBodyData(byref(self), hRequest, pBodyDataBuffer, unBufferSize) # type: ignore

    def GetHTTPStreamingResponseBodyData(self, hRequest, cOffset, pBodyDataBuffer, unBufferSize):
        return ISteamHTTP_GetHTTPStreamingResponseBodyData(byref(self), hRequest, cOffset, pBodyDataBuffer, unBufferSize) # type: ignore

    def ReleaseHTTPRequest(self, hRequest):
        return ISteamHTTP_ReleaseHTTPRequest(byref(self), hRequest) # type: ignore

    def GetHTTPDownloadProgressPct(self, hRequest, pflPercentOut):
        return ISteamHTTP_GetHTTPDownloadProgressPct(byref(self), hRequest, pflPercentOut) # type: ignore

    def SetHTTPRequestRawPostBody(self, hRequest, pchContentType, pubBody, unBodyLen):
        return ISteamHTTP_SetHTTPRequestRawPostBody(byref(self), hRequest, pchContentType, pubBody, unBodyLen) # type: ignore

    def CreateCookieContainer(self, bAllowResponsesToModify):
        return ISteamHTTP_CreateCookieContainer(byref(self), bAllowResponsesToModify) # type: ignore

    def ReleaseCookieContainer(self, hCookieContainer):
        return ISteamHTTP_ReleaseCookieContainer(byref(self), hCookieContainer) # type: ignore

    def SetCookie(self, hCookieContainer, pchHost, pchUrl, pchCookie):
        return ISteamHTTP_SetCookie(byref(self), hCookieContainer, pchHost, pchUrl, pchCookie) # type: ignore

    def SetHTTPRequestCookieContainer(self, hRequest, hCookieContainer):
        return ISteamHTTP_SetHTTPRequestCookieContainer(byref(self), hRequest, hCookieContainer) # type: ignore

    def SetHTTPRequestUserAgentInfo(self, hRequest, pchUserAgentInfo):
        return ISteamHTTP_SetHTTPRequestUserAgentInfo(byref(self), hRequest, pchUserAgentInfo) # type: ignore

    def SetHTTPRequestRequiresVerifiedCertificate(self, hRequest, bRequireVerifiedCertificate):
        return ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate(byref(self), hRequest, bRequireVerifiedCertificate) # type: ignore

    def SetHTTPRequestAbsoluteTimeoutMS(self, hRequest, unMilliseconds):
        return ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS(byref(self), hRequest, unMilliseconds) # type: ignore

    def GetHTTPRequestWasTimedOut(self, hRequest, pbWasTimedOut):
        return ISteamHTTP_GetHTTPRequestWasTimedOut(byref(self), hRequest, pbWasTimedOut) # type: ignore

class ISteamInput(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def Init(self, bExplicitlyCallRunFrame):
        return ISteamInput_Init(byref(self), bExplicitlyCallRunFrame) # type: ignore

    def Shutdown(self, ):
        return ISteamInput_Shutdown(byref(self), ) # type: ignore

    def SetInputActionManifestFilePath(self, pchInputActionManifestAbsolutePath):
        return ISteamInput_SetInputActionManifestFilePath(byref(self), pchInputActionManifestAbsolutePath) # type: ignore

    def RunFrame(self, bReservedValue):
        return ISteamInput_RunFrame(byref(self), bReservedValue) # type: ignore

    def BWaitForData(self, bWaitForever, unTimeout):
        return ISteamInput_BWaitForData(byref(self), bWaitForever, unTimeout) # type: ignore

    def BNewDataAvailable(self, ):
        return ISteamInput_BNewDataAvailable(byref(self), ) # type: ignore

    def GetConnectedControllers(self, handlesOut):
        return ISteamInput_GetConnectedControllers(byref(self), handlesOut) # type: ignore

    def EnableDeviceCallbacks(self, ):
        return ISteamInput_EnableDeviceCallbacks(byref(self), ) # type: ignore

    def EnableActionEventCallbacks(self, pCallback):
        return ISteamInput_EnableActionEventCallbacks(byref(self), pCallback) # type: ignore

    def GetActionSetHandle(self, pszActionSetName):
        return ISteamInput_GetActionSetHandle(byref(self), pszActionSetName) # type: ignore

    def ActivateActionSet(self, inputHandle, actionSetHandle):
        return ISteamInput_ActivateActionSet(byref(self), inputHandle, actionSetHandle) # type: ignore

    def GetCurrentActionSet(self, inputHandle):
        return ISteamInput_GetCurrentActionSet(byref(self), inputHandle) # type: ignore

    def ActivateActionSetLayer(self, inputHandle, actionSetLayerHandle):
        return ISteamInput_ActivateActionSetLayer(byref(self), inputHandle, actionSetLayerHandle) # type: ignore

    def DeactivateActionSetLayer(self, inputHandle, actionSetLayerHandle):
        return ISteamInput_DeactivateActionSetLayer(byref(self), inputHandle, actionSetLayerHandle) # type: ignore

    def DeactivateAllActionSetLayers(self, inputHandle):
        return ISteamInput_DeactivateAllActionSetLayers(byref(self), inputHandle) # type: ignore

    def GetActiveActionSetLayers(self, inputHandle, handlesOut):
        return ISteamInput_GetActiveActionSetLayers(byref(self), inputHandle, handlesOut) # type: ignore

    def GetDigitalActionHandle(self, pszActionName):
        return ISteamInput_GetDigitalActionHandle(byref(self), pszActionName) # type: ignore

    def GetDigitalActionData(self, inputHandle, digitalActionHandle):
        return ISteamInput_GetDigitalActionData(byref(self), inputHandle, digitalActionHandle) # type: ignore

    def GetDigitalActionOrigins(self, inputHandle, actionSetHandle, digitalActionHandle, originsOut):
        return ISteamInput_GetDigitalActionOrigins(byref(self), inputHandle, actionSetHandle, digitalActionHandle, originsOut) # type: ignore

    def GetStringForDigitalActionName(self, eActionHandle):
        return ISteamInput_GetStringForDigitalActionName(byref(self), eActionHandle) # type: ignore

    def GetAnalogActionHandle(self, pszActionName):
        return ISteamInput_GetAnalogActionHandle(byref(self), pszActionName) # type: ignore

    def GetAnalogActionData(self, inputHandle, analogActionHandle):
        return ISteamInput_GetAnalogActionData(byref(self), inputHandle, analogActionHandle) # type: ignore

    def GetAnalogActionOrigins(self, inputHandle, actionSetHandle, analogActionHandle, originsOut):
        return ISteamInput_GetAnalogActionOrigins(byref(self), inputHandle, actionSetHandle, analogActionHandle, originsOut) # type: ignore

    def GetGlyphPNGForActionOrigin(self, eOrigin, eSize, unFlags):
        return ISteamInput_GetGlyphPNGForActionOrigin(byref(self), eOrigin, eSize, unFlags) # type: ignore

    def GetGlyphSVGForActionOrigin(self, eOrigin, unFlags):
        return ISteamInput_GetGlyphSVGForActionOrigin(byref(self), eOrigin, unFlags) # type: ignore

    def GetGlyphForActionOrigin_Legacy(self, eOrigin):
        return ISteamInput_GetGlyphForActionOrigin_Legacy(byref(self), eOrigin) # type: ignore

    def GetStringForActionOrigin(self, eOrigin):
        return ISteamInput_GetStringForActionOrigin(byref(self), eOrigin) # type: ignore

    def GetStringForAnalogActionName(self, eActionHandle):
        return ISteamInput_GetStringForAnalogActionName(byref(self), eActionHandle) # type: ignore

    def StopAnalogActionMomentum(self, inputHandle, eAction):
        return ISteamInput_StopAnalogActionMomentum(byref(self), inputHandle, eAction) # type: ignore

    def GetMotionData(self, inputHandle):
        return ISteamInput_GetMotionData(byref(self), inputHandle) # type: ignore

    def TriggerVibration(self, inputHandle, usLeftSpeed, usRightSpeed):
        return ISteamInput_TriggerVibration(byref(self), inputHandle, usLeftSpeed, usRightSpeed) # type: ignore

    def TriggerVibrationExtended(self, inputHandle, usLeftSpeed, usRightSpeed, usLeftTriggerSpeed, usRightTriggerSpeed):
        return ISteamInput_TriggerVibrationExtended(byref(self), inputHandle, usLeftSpeed, usRightSpeed, usLeftTriggerSpeed, usRightTriggerSpeed) # type: ignore

    def TriggerSimpleHapticEvent(self, inputHandle, eHapticLocation, nIntensity, nGainDB, nOtherIntensity, nOtherGainDB):
        return ISteamInput_TriggerSimpleHapticEvent(byref(self), inputHandle, eHapticLocation, nIntensity, nGainDB, nOtherIntensity, nOtherGainDB) # type: ignore

    def SetLEDColor(self, inputHandle, nColorR, nColorG, nColorB, nFlags):
        return ISteamInput_SetLEDColor(byref(self), inputHandle, nColorR, nColorG, nColorB, nFlags) # type: ignore

    def Legacy_TriggerHapticPulse(self, inputHandle, eTargetPad, usDurationMicroSec):
        return ISteamInput_Legacy_TriggerHapticPulse(byref(self), inputHandle, eTargetPad, usDurationMicroSec) # type: ignore

    def Legacy_TriggerRepeatedHapticPulse(self, inputHandle, eTargetPad, usDurationMicroSec, usOffMicroSec, unRepeat, nFlags):
        return ISteamInput_Legacy_TriggerRepeatedHapticPulse(byref(self), inputHandle, eTargetPad, usDurationMicroSec, usOffMicroSec, unRepeat, nFlags) # type: ignore

    def ShowBindingPanel(self, inputHandle):
        return ISteamInput_ShowBindingPanel(byref(self), inputHandle) # type: ignore

    def GetInputTypeForHandle(self, inputHandle):
        return ISteamInput_GetInputTypeForHandle(byref(self), inputHandle) # type: ignore

    def GetControllerForGamepadIndex(self, nIndex):
        return ISteamInput_GetControllerForGamepadIndex(byref(self), nIndex) # type: ignore

    def GetGamepadIndexForController(self, ulinputHandle):
        return ISteamInput_GetGamepadIndexForController(byref(self), ulinputHandle) # type: ignore

    def GetStringForXboxOrigin(self, eOrigin):
        return ISteamInput_GetStringForXboxOrigin(byref(self), eOrigin) # type: ignore

    def GetGlyphForXboxOrigin(self, eOrigin):
        return ISteamInput_GetGlyphForXboxOrigin(byref(self), eOrigin) # type: ignore

    def GetActionOriginFromXboxOrigin(self, inputHandle, eOrigin):
        return ISteamInput_GetActionOriginFromXboxOrigin(byref(self), inputHandle, eOrigin) # type: ignore

    def TranslateActionOrigin(self, eDestinationInputType, eSourceOrigin):
        return ISteamInput_TranslateActionOrigin(byref(self), eDestinationInputType, eSourceOrigin) # type: ignore

    def GetDeviceBindingRevision(self, inputHandle, pMajor, pMinor):
        return ISteamInput_GetDeviceBindingRevision(byref(self), inputHandle, pMajor, pMinor) # type: ignore

    def GetRemotePlaySessionID(self, inputHandle):
        return ISteamInput_GetRemotePlaySessionID(byref(self), inputHandle) # type: ignore

    def GetSessionInputConfigurationSettings(self, ):
        return ISteamInput_GetSessionInputConfigurationSettings(byref(self), ) # type: ignore

class ISteamController(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def Init(self, ):
        return ISteamController_Init(byref(self), ) # type: ignore

    def Shutdown(self, ):
        return ISteamController_Shutdown(byref(self), ) # type: ignore

    def RunFrame(self, ):
        return ISteamController_RunFrame(byref(self), ) # type: ignore

    def GetConnectedControllers(self, handlesOut):
        return ISteamController_GetConnectedControllers(byref(self), handlesOut) # type: ignore

    def GetActionSetHandle(self, pszActionSetName):
        return ISteamController_GetActionSetHandle(byref(self), pszActionSetName) # type: ignore

    def ActivateActionSet(self, controllerHandle, actionSetHandle):
        return ISteamController_ActivateActionSet(byref(self), controllerHandle, actionSetHandle) # type: ignore

    def GetCurrentActionSet(self, controllerHandle):
        return ISteamController_GetCurrentActionSet(byref(self), controllerHandle) # type: ignore

    def ActivateActionSetLayer(self, controllerHandle, actionSetLayerHandle):
        return ISteamController_ActivateActionSetLayer(byref(self), controllerHandle, actionSetLayerHandle) # type: ignore

    def DeactivateActionSetLayer(self, controllerHandle, actionSetLayerHandle):
        return ISteamController_DeactivateActionSetLayer(byref(self), controllerHandle, actionSetLayerHandle) # type: ignore

    def DeactivateAllActionSetLayers(self, controllerHandle):
        return ISteamController_DeactivateAllActionSetLayers(byref(self), controllerHandle) # type: ignore

    def GetActiveActionSetLayers(self, controllerHandle, handlesOut):
        return ISteamController_GetActiveActionSetLayers(byref(self), controllerHandle, handlesOut) # type: ignore

    def GetDigitalActionHandle(self, pszActionName):
        return ISteamController_GetDigitalActionHandle(byref(self), pszActionName) # type: ignore

    def GetDigitalActionData(self, controllerHandle, digitalActionHandle):
        return ISteamController_GetDigitalActionData(byref(self), controllerHandle, digitalActionHandle) # type: ignore

    def GetDigitalActionOrigins(self, controllerHandle, actionSetHandle, digitalActionHandle, originsOut):
        return ISteamController_GetDigitalActionOrigins(byref(self), controllerHandle, actionSetHandle, digitalActionHandle, originsOut) # type: ignore

    def GetAnalogActionHandle(self, pszActionName):
        return ISteamController_GetAnalogActionHandle(byref(self), pszActionName) # type: ignore

    def GetAnalogActionData(self, controllerHandle, analogActionHandle):
        return ISteamController_GetAnalogActionData(byref(self), controllerHandle, analogActionHandle) # type: ignore

    def GetAnalogActionOrigins(self, controllerHandle, actionSetHandle, analogActionHandle, originsOut):
        return ISteamController_GetAnalogActionOrigins(byref(self), controllerHandle, actionSetHandle, analogActionHandle, originsOut) # type: ignore

    def GetGlyphForActionOrigin(self, eOrigin):
        return ISteamController_GetGlyphForActionOrigin(byref(self), eOrigin) # type: ignore

    def GetStringForActionOrigin(self, eOrigin):
        return ISteamController_GetStringForActionOrigin(byref(self), eOrigin) # type: ignore

    def StopAnalogActionMomentum(self, controllerHandle, eAction):
        return ISteamController_StopAnalogActionMomentum(byref(self), controllerHandle, eAction) # type: ignore

    def GetMotionData(self, controllerHandle):
        return ISteamController_GetMotionData(byref(self), controllerHandle) # type: ignore

    def TriggerHapticPulse(self, controllerHandle, eTargetPad, usDurationMicroSec):
        return ISteamController_TriggerHapticPulse(byref(self), controllerHandle, eTargetPad, usDurationMicroSec) # type: ignore

    def TriggerRepeatedHapticPulse(self, controllerHandle, eTargetPad, usDurationMicroSec, usOffMicroSec, unRepeat, nFlags):
        return ISteamController_TriggerRepeatedHapticPulse(byref(self), controllerHandle, eTargetPad, usDurationMicroSec, usOffMicroSec, unRepeat, nFlags) # type: ignore

    def TriggerVibration(self, controllerHandle, usLeftSpeed, usRightSpeed):
        return ISteamController_TriggerVibration(byref(self), controllerHandle, usLeftSpeed, usRightSpeed) # type: ignore

    def SetLEDColor(self, controllerHandle, nColorR, nColorG, nColorB, nFlags):
        return ISteamController_SetLEDColor(byref(self), controllerHandle, nColorR, nColorG, nColorB, nFlags) # type: ignore

    def ShowBindingPanel(self, controllerHandle):
        return ISteamController_ShowBindingPanel(byref(self), controllerHandle) # type: ignore

    def GetInputTypeForHandle(self, controllerHandle):
        return ISteamController_GetInputTypeForHandle(byref(self), controllerHandle) # type: ignore

    def GetControllerForGamepadIndex(self, nIndex):
        return ISteamController_GetControllerForGamepadIndex(byref(self), nIndex) # type: ignore

    def GetGamepadIndexForController(self, ulControllerHandle):
        return ISteamController_GetGamepadIndexForController(byref(self), ulControllerHandle) # type: ignore

    def GetStringForXboxOrigin(self, eOrigin):
        return ISteamController_GetStringForXboxOrigin(byref(self), eOrigin) # type: ignore

    def GetGlyphForXboxOrigin(self, eOrigin):
        return ISteamController_GetGlyphForXboxOrigin(byref(self), eOrigin) # type: ignore

    def GetActionOriginFromXboxOrigin(self, controllerHandle, eOrigin):
        return ISteamController_GetActionOriginFromXboxOrigin(byref(self), controllerHandle, eOrigin) # type: ignore

    def TranslateActionOrigin(self, eDestinationInputType, eSourceOrigin):
        return ISteamController_TranslateActionOrigin(byref(self), eDestinationInputType, eSourceOrigin) # type: ignore

    def GetControllerBindingRevision(self, controllerHandle, pMajor, pMinor):
        return ISteamController_GetControllerBindingRevision(byref(self), controllerHandle, pMajor, pMinor) # type: ignore

class ISteamUGC(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def CreateQueryUserUGCRequest(self, unAccountID, eListType, eMatchingUGCType, eSortOrder, nCreatorAppID, nConsumerAppID, unPage):
        return ISteamUGC_CreateQueryUserUGCRequest(byref(self), unAccountID, eListType, eMatchingUGCType, eSortOrder, nCreatorAppID, nConsumerAppID, unPage) # type: ignore

    def CreateQueryAllUGCRequestPage(self, eQueryType, eMatchingeMatchingUGCTypeFileType, nCreatorAppID, nConsumerAppID, unPage):
        return ISteamUGC_CreateQueryAllUGCRequestPage(byref(self), eQueryType, eMatchingeMatchingUGCTypeFileType, nCreatorAppID, nConsumerAppID, unPage) # type: ignore

    def CreateQueryAllUGCRequestCursor(self, eQueryType, eMatchingeMatchingUGCTypeFileType, nCreatorAppID, nConsumerAppID, pchCursor):
        return ISteamUGC_CreateQueryAllUGCRequestCursor(byref(self), eQueryType, eMatchingeMatchingUGCTypeFileType, nCreatorAppID, nConsumerAppID, pchCursor) # type: ignore

    def CreateQueryUGCDetailsRequest(self, pvecPublishedFileID, unNumPublishedFileIDs):
        return ISteamUGC_CreateQueryUGCDetailsRequest(byref(self), pvecPublishedFileID, unNumPublishedFileIDs) # type: ignore

    def SendQueryUGCRequest(self, handle):
        return ISteamUGC_SendQueryUGCRequest(byref(self), handle) # type: ignore

    def GetQueryUGCResult(self, handle, index, pDetails):
        return ISteamUGC_GetQueryUGCResult(byref(self), handle, index, pDetails) # type: ignore

    def GetQueryUGCNumTags(self, handle, index):
        return ISteamUGC_GetQueryUGCNumTags(byref(self), handle, index) # type: ignore

    def GetQueryUGCTag(self, handle, index, indexTag, pchValue, cchValueSize):
        return ISteamUGC_GetQueryUGCTag(byref(self), handle, index, indexTag, pchValue, cchValueSize) # type: ignore

    def GetQueryUGCTagDisplayName(self, handle, index, indexTag, pchValue, cchValueSize):
        return ISteamUGC_GetQueryUGCTagDisplayName(byref(self), handle, index, indexTag, pchValue, cchValueSize) # type: ignore

    def GetQueryUGCPreviewURL(self, handle, index, pchURL, cchURLSize):
        return ISteamUGC_GetQueryUGCPreviewURL(byref(self), handle, index, pchURL, cchURLSize) # type: ignore

    def GetQueryUGCMetadata(self, handle, index, pchMetadata, cchMetadatasize):
        return ISteamUGC_GetQueryUGCMetadata(byref(self), handle, index, pchMetadata, cchMetadatasize) # type: ignore

    def GetQueryUGCChildren(self, handle, index, pvecPublishedFileID, cMaxEntries):
        return ISteamUGC_GetQueryUGCChildren(byref(self), handle, index, pvecPublishedFileID, cMaxEntries) # type: ignore

    def GetQueryUGCStatistic(self, handle, index, eStatType, pStatValue):
        return ISteamUGC_GetQueryUGCStatistic(byref(self), handle, index, eStatType, pStatValue) # type: ignore

    def GetQueryUGCNumAdditionalPreviews(self, handle, index):
        return ISteamUGC_GetQueryUGCNumAdditionalPreviews(byref(self), handle, index) # type: ignore

    def GetQueryUGCAdditionalPreview(self, handle, index, previewIndex, pchURLOrVideoID, cchURLSize, pchOriginalFileName, cchOriginalFileNameSize, pPreviewType):
        return ISteamUGC_GetQueryUGCAdditionalPreview(byref(self), handle, index, previewIndex, pchURLOrVideoID, cchURLSize, pchOriginalFileName, cchOriginalFileNameSize, pPreviewType) # type: ignore

    def GetQueryUGCNumKeyValueTags(self, handle, index):
        return ISteamUGC_GetQueryUGCNumKeyValueTags(byref(self), handle, index) # type: ignore

    def GetQueryUGCKeyValueTag(self, handle, index, keyValueTagIndex, pchKey, cchKeySize, pchValue, cchValueSize):
        return ISteamUGC_GetQueryUGCKeyValueTag(byref(self), handle, index, keyValueTagIndex, pchKey, cchKeySize, pchValue, cchValueSize) # type: ignore

    def GetQueryFirstUGCKeyValueTag(self, handle, index, pchKey, pchValue, cchValueSize):
        return ISteamUGC_GetQueryFirstUGCKeyValueTag(byref(self), handle, index, pchKey, pchValue, cchValueSize) # type: ignore

    def ReleaseQueryUGCRequest(self, handle):
        return ISteamUGC_ReleaseQueryUGCRequest(byref(self), handle) # type: ignore

    def AddRequiredTag(self, handle, pTagName):
        return ISteamUGC_AddRequiredTag(byref(self), handle, pTagName) # type: ignore

    def AddRequiredTagGroup(self, handle, pTagGroups):
        return ISteamUGC_AddRequiredTagGroup(byref(self), handle, pTagGroups) # type: ignore

    def AddExcludedTag(self, handle, pTagName):
        return ISteamUGC_AddExcludedTag(byref(self), handle, pTagName) # type: ignore

    def SetReturnOnlyIDs(self, handle, bReturnOnlyIDs):
        return ISteamUGC_SetReturnOnlyIDs(byref(self), handle, bReturnOnlyIDs) # type: ignore

    def SetReturnKeyValueTags(self, handle, bReturnKeyValueTags):
        return ISteamUGC_SetReturnKeyValueTags(byref(self), handle, bReturnKeyValueTags) # type: ignore

    def SetReturnLongDescription(self, handle, bReturnLongDescription):
        return ISteamUGC_SetReturnLongDescription(byref(self), handle, bReturnLongDescription) # type: ignore

    def SetReturnMetadata(self, handle, bReturnMetadata):
        return ISteamUGC_SetReturnMetadata(byref(self), handle, bReturnMetadata) # type: ignore

    def SetReturnChildren(self, handle, bReturnChildren):
        return ISteamUGC_SetReturnChildren(byref(self), handle, bReturnChildren) # type: ignore

    def SetReturnAdditionalPreviews(self, handle, bReturnAdditionalPreviews):
        return ISteamUGC_SetReturnAdditionalPreviews(byref(self), handle, bReturnAdditionalPreviews) # type: ignore

    def SetReturnTotalOnly(self, handle, bReturnTotalOnly):
        return ISteamUGC_SetReturnTotalOnly(byref(self), handle, bReturnTotalOnly) # type: ignore

    def SetReturnPlaytimeStats(self, handle, unDays):
        return ISteamUGC_SetReturnPlaytimeStats(byref(self), handle, unDays) # type: ignore

    def SetLanguage(self, handle, pchLanguage):
        return ISteamUGC_SetLanguage(byref(self), handle, pchLanguage) # type: ignore

    def SetAllowCachedResponse(self, handle, unMaxAgeSeconds):
        return ISteamUGC_SetAllowCachedResponse(byref(self), handle, unMaxAgeSeconds) # type: ignore

    def SetCloudFileNameFilter(self, handle, pMatchCloudFileName):
        return ISteamUGC_SetCloudFileNameFilter(byref(self), handle, pMatchCloudFileName) # type: ignore

    def SetMatchAnyTag(self, handle, bMatchAnyTag):
        return ISteamUGC_SetMatchAnyTag(byref(self), handle, bMatchAnyTag) # type: ignore

    def SetSearchText(self, handle, pSearchText):
        return ISteamUGC_SetSearchText(byref(self), handle, pSearchText) # type: ignore

    def SetRankedByTrendDays(self, handle, unDays):
        return ISteamUGC_SetRankedByTrendDays(byref(self), handle, unDays) # type: ignore

    def SetTimeCreatedDateRange(self, handle, rtStart, rtEnd):
        return ISteamUGC_SetTimeCreatedDateRange(byref(self), handle, rtStart, rtEnd) # type: ignore

    def SetTimeUpdatedDateRange(self, handle, rtStart, rtEnd):
        return ISteamUGC_SetTimeUpdatedDateRange(byref(self), handle, rtStart, rtEnd) # type: ignore

    def AddRequiredKeyValueTag(self, handle, pKey, pValue):
        return ISteamUGC_AddRequiredKeyValueTag(byref(self), handle, pKey, pValue) # type: ignore

    def RequestUGCDetails(self, nPublishedFileID, unMaxAgeSeconds):
        return ISteamUGC_RequestUGCDetails(byref(self), nPublishedFileID, unMaxAgeSeconds) # type: ignore

    def CreateItem(self, nConsumerAppId, eFileType):
        return ISteamUGC_CreateItem(byref(self), nConsumerAppId, eFileType) # type: ignore

    def StartItemUpdate(self, nConsumerAppId, nPublishedFileID):
        return ISteamUGC_StartItemUpdate(byref(self), nConsumerAppId, nPublishedFileID) # type: ignore

    def SetItemTitle(self, handle, pchTitle):
        return ISteamUGC_SetItemTitle(byref(self), handle, pchTitle) # type: ignore

    def SetItemDescription(self, handle, pchDescription):
        return ISteamUGC_SetItemDescription(byref(self), handle, pchDescription) # type: ignore

    def SetItemUpdateLanguage(self, handle, pchLanguage):
        return ISteamUGC_SetItemUpdateLanguage(byref(self), handle, pchLanguage) # type: ignore

    def SetItemMetadata(self, handle, pchMetaData):
        return ISteamUGC_SetItemMetadata(byref(self), handle, pchMetaData) # type: ignore

    def SetItemVisibility(self, handle, eVisibility):
        return ISteamUGC_SetItemVisibility(byref(self), handle, eVisibility) # type: ignore

    def SetItemTags(self, updateHandle, pTags):
        return ISteamUGC_SetItemTags(byref(self), updateHandle, pTags) # type: ignore

    def SetItemContent(self, handle, pszContentFolder):
        return ISteamUGC_SetItemContent(byref(self), handle, pszContentFolder) # type: ignore

    def SetItemPreview(self, handle, pszPreviewFile):
        return ISteamUGC_SetItemPreview(byref(self), handle, pszPreviewFile) # type: ignore

    def SetAllowLegacyUpload(self, handle, bAllowLegacyUpload):
        return ISteamUGC_SetAllowLegacyUpload(byref(self), handle, bAllowLegacyUpload) # type: ignore

    def RemoveAllItemKeyValueTags(self, handle):
        return ISteamUGC_RemoveAllItemKeyValueTags(byref(self), handle) # type: ignore

    def RemoveItemKeyValueTags(self, handle, pchKey):
        return ISteamUGC_RemoveItemKeyValueTags(byref(self), handle, pchKey) # type: ignore

    def AddItemKeyValueTag(self, handle, pchKey, pchValue):
        return ISteamUGC_AddItemKeyValueTag(byref(self), handle, pchKey, pchValue) # type: ignore

    def AddItemPreviewFile(self, handle, pszPreviewFile, type):
        return ISteamUGC_AddItemPreviewFile(byref(self), handle, pszPreviewFile, type) # type: ignore

    def AddItemPreviewVideo(self, handle, pszVideoID):
        return ISteamUGC_AddItemPreviewVideo(byref(self), handle, pszVideoID) # type: ignore

    def UpdateItemPreviewFile(self, handle, index, pszPreviewFile):
        return ISteamUGC_UpdateItemPreviewFile(byref(self), handle, index, pszPreviewFile) # type: ignore

    def UpdateItemPreviewVideo(self, handle, index, pszVideoID):
        return ISteamUGC_UpdateItemPreviewVideo(byref(self), handle, index, pszVideoID) # type: ignore

    def RemoveItemPreview(self, handle, index):
        return ISteamUGC_RemoveItemPreview(byref(self), handle, index) # type: ignore

    def SubmitItemUpdate(self, handle, pchChangeNote):
        return ISteamUGC_SubmitItemUpdate(byref(self), handle, pchChangeNote) # type: ignore

    def GetItemUpdateProgress(self, handle, punBytesProcessed, punBytesTotal):
        return ISteamUGC_GetItemUpdateProgress(byref(self), handle, punBytesProcessed, punBytesTotal) # type: ignore

    def SetUserItemVote(self, nPublishedFileID, bVoteUp):
        return ISteamUGC_SetUserItemVote(byref(self), nPublishedFileID, bVoteUp) # type: ignore

    def GetUserItemVote(self, nPublishedFileID):
        return ISteamUGC_GetUserItemVote(byref(self), nPublishedFileID) # type: ignore

    def AddItemToFavorites(self, nAppId, nPublishedFileID):
        return ISteamUGC_AddItemToFavorites(byref(self), nAppId, nPublishedFileID) # type: ignore

    def RemoveItemFromFavorites(self, nAppId, nPublishedFileID):
        return ISteamUGC_RemoveItemFromFavorites(byref(self), nAppId, nPublishedFileID) # type: ignore

    def SubscribeItem(self, nPublishedFileID):
        return ISteamUGC_SubscribeItem(byref(self), nPublishedFileID) # type: ignore

    def UnsubscribeItem(self, nPublishedFileID):
        return ISteamUGC_UnsubscribeItem(byref(self), nPublishedFileID) # type: ignore

    def GetNumSubscribedItems(self, ):
        return ISteamUGC_GetNumSubscribedItems(byref(self), ) # type: ignore

    def GetSubscribedItems(self, pvecPublishedFileID, cMaxEntries):
        return ISteamUGC_GetSubscribedItems(byref(self), pvecPublishedFileID, cMaxEntries) # type: ignore

    def GetItemState(self, nPublishedFileID):
        return ISteamUGC_GetItemState(byref(self), nPublishedFileID) # type: ignore

    def GetItemInstallInfo(self, nPublishedFileID, punSizeOnDisk, pchFolder, cchFolderSize, punTimeStamp):
        return ISteamUGC_GetItemInstallInfo(byref(self), nPublishedFileID, punSizeOnDisk, pchFolder, cchFolderSize, punTimeStamp) # type: ignore

    def GetItemDownloadInfo(self, nPublishedFileID, punBytesDownloaded, punBytesTotal):
        return ISteamUGC_GetItemDownloadInfo(byref(self), nPublishedFileID, punBytesDownloaded, punBytesTotal) # type: ignore

    def DownloadItem(self, nPublishedFileID, bHighPriority):
        return ISteamUGC_DownloadItem(byref(self), nPublishedFileID, bHighPriority) # type: ignore

    def BInitWorkshopForGameServer(self, unWorkshopDepotID, pszFolder):
        return ISteamUGC_BInitWorkshopForGameServer(byref(self), unWorkshopDepotID, pszFolder) # type: ignore

    def SuspendDownloads(self, bSuspend):
        return ISteamUGC_SuspendDownloads(byref(self), bSuspend) # type: ignore

    def StartPlaytimeTracking(self, pvecPublishedFileID, unNumPublishedFileIDs):
        return ISteamUGC_StartPlaytimeTracking(byref(self), pvecPublishedFileID, unNumPublishedFileIDs) # type: ignore

    def StopPlaytimeTracking(self, pvecPublishedFileID, unNumPublishedFileIDs):
        return ISteamUGC_StopPlaytimeTracking(byref(self), pvecPublishedFileID, unNumPublishedFileIDs) # type: ignore

    def StopPlaytimeTrackingForAllItems(self, ):
        return ISteamUGC_StopPlaytimeTrackingForAllItems(byref(self), ) # type: ignore

    def AddDependency(self, nParentPublishedFileID, nChildPublishedFileID):
        return ISteamUGC_AddDependency(byref(self), nParentPublishedFileID, nChildPublishedFileID) # type: ignore

    def RemoveDependency(self, nParentPublishedFileID, nChildPublishedFileID):
        return ISteamUGC_RemoveDependency(byref(self), nParentPublishedFileID, nChildPublishedFileID) # type: ignore

    def AddAppDependency(self, nPublishedFileID, nAppID):
        return ISteamUGC_AddAppDependency(byref(self), nPublishedFileID, nAppID) # type: ignore

    def RemoveAppDependency(self, nPublishedFileID, nAppID):
        return ISteamUGC_RemoveAppDependency(byref(self), nPublishedFileID, nAppID) # type: ignore

    def GetAppDependencies(self, nPublishedFileID):
        return ISteamUGC_GetAppDependencies(byref(self), nPublishedFileID) # type: ignore

    def DeleteItem(self, nPublishedFileID):
        return ISteamUGC_DeleteItem(byref(self), nPublishedFileID) # type: ignore

    def ShowWorkshopEULA(self, ):
        return ISteamUGC_ShowWorkshopEULA(byref(self), ) # type: ignore

    def GetWorkshopEULAStatus(self, ):
        return ISteamUGC_GetWorkshopEULAStatus(byref(self), ) # type: ignore

class ISteamAppList(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetNumInstalledApps(self, ):
        return ISteamAppList_GetNumInstalledApps(byref(self), ) # type: ignore

    def GetInstalledApps(self, pvecAppID, unMaxAppIDs):
        return ISteamAppList_GetInstalledApps(byref(self), pvecAppID, unMaxAppIDs) # type: ignore

    def GetAppName(self, nAppID, pchName, cchNameMax):
        return ISteamAppList_GetAppName(byref(self), nAppID, pchName, cchNameMax) # type: ignore

    def GetAppInstallDir(self, nAppID, pchDirectory, cchNameMax):
        return ISteamAppList_GetAppInstallDir(byref(self), nAppID, pchDirectory, cchNameMax) # type: ignore

    def GetAppBuildId(self, nAppID):
        return ISteamAppList_GetAppBuildId(byref(self), nAppID) # type: ignore

class ISteamHTMLSurface(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def Init(self, ):
        return ISteamHTMLSurface_Init(byref(self), ) # type: ignore

    def Shutdown(self, ):
        return ISteamHTMLSurface_Shutdown(byref(self), ) # type: ignore

    def CreateBrowser(self, pchUserAgent, pchUserCSS):
        return ISteamHTMLSurface_CreateBrowser(byref(self), pchUserAgent, pchUserCSS) # type: ignore

    def RemoveBrowser(self, unBrowserHandle):
        return ISteamHTMLSurface_RemoveBrowser(byref(self), unBrowserHandle) # type: ignore

    def LoadURL(self, unBrowserHandle, pchURL, pchPostData):
        return ISteamHTMLSurface_LoadURL(byref(self), unBrowserHandle, pchURL, pchPostData) # type: ignore

    def SetSize(self, unBrowserHandle, unWidth, unHeight):
        return ISteamHTMLSurface_SetSize(byref(self), unBrowserHandle, unWidth, unHeight) # type: ignore

    def StopLoad(self, unBrowserHandle):
        return ISteamHTMLSurface_StopLoad(byref(self), unBrowserHandle) # type: ignore

    def Reload(self, unBrowserHandle):
        return ISteamHTMLSurface_Reload(byref(self), unBrowserHandle) # type: ignore

    def GoBack(self, unBrowserHandle):
        return ISteamHTMLSurface_GoBack(byref(self), unBrowserHandle) # type: ignore

    def GoForward(self, unBrowserHandle):
        return ISteamHTMLSurface_GoForward(byref(self), unBrowserHandle) # type: ignore

    def AddHeader(self, unBrowserHandle, pchKey, pchValue):
        return ISteamHTMLSurface_AddHeader(byref(self), unBrowserHandle, pchKey, pchValue) # type: ignore

    def ExecuteJavascript(self, unBrowserHandle, pchScript):
        return ISteamHTMLSurface_ExecuteJavascript(byref(self), unBrowserHandle, pchScript) # type: ignore

    def MouseUp(self, unBrowserHandle, eMouseButton):
        return ISteamHTMLSurface_MouseUp(byref(self), unBrowserHandle, eMouseButton) # type: ignore

    def MouseDown(self, unBrowserHandle, eMouseButton):
        return ISteamHTMLSurface_MouseDown(byref(self), unBrowserHandle, eMouseButton) # type: ignore

    def MouseDoubleClick(self, unBrowserHandle, eMouseButton):
        return ISteamHTMLSurface_MouseDoubleClick(byref(self), unBrowserHandle, eMouseButton) # type: ignore

    def MouseMove(self, unBrowserHandle, x, y):
        return ISteamHTMLSurface_MouseMove(byref(self), unBrowserHandle, x, y) # type: ignore

    def MouseWheel(self, unBrowserHandle, nDelta):
        return ISteamHTMLSurface_MouseWheel(byref(self), unBrowserHandle, nDelta) # type: ignore

    def KeyDown(self, unBrowserHandle, nNativeKeyCode, eHTMLKeyModifiers, bIsSystemKey):
        return ISteamHTMLSurface_KeyDown(byref(self), unBrowserHandle, nNativeKeyCode, eHTMLKeyModifiers, bIsSystemKey) # type: ignore

    def KeyUp(self, unBrowserHandle, nNativeKeyCode, eHTMLKeyModifiers):
        return ISteamHTMLSurface_KeyUp(byref(self), unBrowserHandle, nNativeKeyCode, eHTMLKeyModifiers) # type: ignore

    def KeyChar(self, unBrowserHandle, cUnicodeChar, eHTMLKeyModifiers):
        return ISteamHTMLSurface_KeyChar(byref(self), unBrowserHandle, cUnicodeChar, eHTMLKeyModifiers) # type: ignore

    def SetHorizontalScroll(self, unBrowserHandle, nAbsolutePixelScroll):
        return ISteamHTMLSurface_SetHorizontalScroll(byref(self), unBrowserHandle, nAbsolutePixelScroll) # type: ignore

    def SetVerticalScroll(self, unBrowserHandle, nAbsolutePixelScroll):
        return ISteamHTMLSurface_SetVerticalScroll(byref(self), unBrowserHandle, nAbsolutePixelScroll) # type: ignore

    def SetKeyFocus(self, unBrowserHandle, bHasKeyFocus):
        return ISteamHTMLSurface_SetKeyFocus(byref(self), unBrowserHandle, bHasKeyFocus) # type: ignore

    def ViewSource(self, unBrowserHandle):
        return ISteamHTMLSurface_ViewSource(byref(self), unBrowserHandle) # type: ignore

    def CopyToClipboard(self, unBrowserHandle):
        return ISteamHTMLSurface_CopyToClipboard(byref(self), unBrowserHandle) # type: ignore

    def PasteFromClipboard(self, unBrowserHandle):
        return ISteamHTMLSurface_PasteFromClipboard(byref(self), unBrowserHandle) # type: ignore

    def Find(self, unBrowserHandle, pchSearchStr, bCurrentlyInFind, bReverse):
        return ISteamHTMLSurface_Find(byref(self), unBrowserHandle, pchSearchStr, bCurrentlyInFind, bReverse) # type: ignore

    def StopFind(self, unBrowserHandle):
        return ISteamHTMLSurface_StopFind(byref(self), unBrowserHandle) # type: ignore

    def GetLinkAtPosition(self, unBrowserHandle, x, y):
        return ISteamHTMLSurface_GetLinkAtPosition(byref(self), unBrowserHandle, x, y) # type: ignore

    def SetCookie(self, pchHostname, pchKey, pchValue, pchPath, nExpires, bSecure, bHTTPOnly):
        return ISteamHTMLSurface_SetCookie(byref(self), pchHostname, pchKey, pchValue, pchPath, nExpires, bSecure, bHTTPOnly) # type: ignore

    def SetPageScaleFactor(self, unBrowserHandle, flZoom, nPointX, nPointY):
        return ISteamHTMLSurface_SetPageScaleFactor(byref(self), unBrowserHandle, flZoom, nPointX, nPointY) # type: ignore

    def SetBackgroundMode(self, unBrowserHandle, bBackgroundMode):
        return ISteamHTMLSurface_SetBackgroundMode(byref(self), unBrowserHandle, bBackgroundMode) # type: ignore

    def SetDPIScalingFactor(self, unBrowserHandle, flDPIScaling):
        return ISteamHTMLSurface_SetDPIScalingFactor(byref(self), unBrowserHandle, flDPIScaling) # type: ignore

    def OpenDeveloperTools(self, unBrowserHandle):
        return ISteamHTMLSurface_OpenDeveloperTools(byref(self), unBrowserHandle) # type: ignore

    def AllowStartRequest(self, unBrowserHandle, bAllowed):
        return ISteamHTMLSurface_AllowStartRequest(byref(self), unBrowserHandle, bAllowed) # type: ignore

    def JSDialogResponse(self, unBrowserHandle, bResult):
        return ISteamHTMLSurface_JSDialogResponse(byref(self), unBrowserHandle, bResult) # type: ignore

    def FileLoadDialogResponse(self, unBrowserHandle, pchSelectedFiles):
        return ISteamHTMLSurface_FileLoadDialogResponse(byref(self), unBrowserHandle, pchSelectedFiles) # type: ignore

class ISteamInventory(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetResultStatus(self, resultHandle):
        return ISteamInventory_GetResultStatus(byref(self), resultHandle) # type: ignore

    def GetResultItems(self, resultHandle, pOutItemsArray, punOutItemsArraySize):
        return ISteamInventory_GetResultItems(byref(self), resultHandle, pOutItemsArray, punOutItemsArraySize) # type: ignore

    def GetResultItemProperty(self, resultHandle, unItemIndex, pchPropertyName, pchValueBuffer, punValueBufferSizeOut):
        return ISteamInventory_GetResultItemProperty(byref(self), resultHandle, unItemIndex, pchPropertyName, pchValueBuffer, punValueBufferSizeOut) # type: ignore

    def GetResultTimestamp(self, resultHandle):
        return ISteamInventory_GetResultTimestamp(byref(self), resultHandle) # type: ignore

    def CheckResultSteamID(self, resultHandle, steamIDExpected):
        return ISteamInventory_CheckResultSteamID(byref(self), resultHandle, steamIDExpected) # type: ignore

    def DestroyResult(self, resultHandle):
        return ISteamInventory_DestroyResult(byref(self), resultHandle) # type: ignore

    def GetAllItems(self, pResultHandle):
        return ISteamInventory_GetAllItems(byref(self), pResultHandle) # type: ignore

    def GetItemsByID(self, pResultHandle, pInstanceIDs, unCountInstanceIDs):
        return ISteamInventory_GetItemsByID(byref(self), pResultHandle, pInstanceIDs, unCountInstanceIDs) # type: ignore

    def SerializeResult(self, resultHandle, pOutBuffer, punOutBufferSize):
        return ISteamInventory_SerializeResult(byref(self), resultHandle, pOutBuffer, punOutBufferSize) # type: ignore

    def DeserializeResult(self, pOutResultHandle, pBuffer, unBufferSize, bRESERVED_MUST_BE_FALSE):
        return ISteamInventory_DeserializeResult(byref(self), pOutResultHandle, pBuffer, unBufferSize, bRESERVED_MUST_BE_FALSE) # type: ignore

    def GenerateItems(self, pResultHandle, pArrayItemDefs, punArrayQuantity, unArrayLength):
        return ISteamInventory_GenerateItems(byref(self), pResultHandle, pArrayItemDefs, punArrayQuantity, unArrayLength) # type: ignore

    def GrantPromoItems(self, pResultHandle):
        return ISteamInventory_GrantPromoItems(byref(self), pResultHandle) # type: ignore

    def AddPromoItem(self, pResultHandle, itemDef):
        return ISteamInventory_AddPromoItem(byref(self), pResultHandle, itemDef) # type: ignore

    def AddPromoItems(self, pResultHandle, pArrayItemDefs, unArrayLength):
        return ISteamInventory_AddPromoItems(byref(self), pResultHandle, pArrayItemDefs, unArrayLength) # type: ignore

    def ConsumeItem(self, pResultHandle, itemConsume, unQuantity):
        return ISteamInventory_ConsumeItem(byref(self), pResultHandle, itemConsume, unQuantity) # type: ignore

    def ExchangeItems(self, pResultHandle, pArrayGenerate, punArrayGenerateQuantity, unArrayGenerateLength, pArrayDestroy, punArrayDestroyQuantity, unArrayDestroyLength):
        return ISteamInventory_ExchangeItems(byref(self), pResultHandle, pArrayGenerate, punArrayGenerateQuantity, unArrayGenerateLength, pArrayDestroy, punArrayDestroyQuantity, unArrayDestroyLength) # type: ignore

    def TransferItemQuantity(self, pResultHandle, itemIdSource, unQuantity, itemIdDest):
        return ISteamInventory_TransferItemQuantity(byref(self), pResultHandle, itemIdSource, unQuantity, itemIdDest) # type: ignore

    def SendItemDropHeartbeat(self, ):
        return ISteamInventory_SendItemDropHeartbeat(byref(self), ) # type: ignore

    def TriggerItemDrop(self, pResultHandle, dropListDefinition):
        return ISteamInventory_TriggerItemDrop(byref(self), pResultHandle, dropListDefinition) # type: ignore

    def TradeItems(self, pResultHandle, steamIDTradePartner, pArrayGive, pArrayGiveQuantity, nArrayGiveLength, pArrayGet, pArrayGetQuantity, nArrayGetLength):
        return ISteamInventory_TradeItems(byref(self), pResultHandle, steamIDTradePartner, pArrayGive, pArrayGiveQuantity, nArrayGiveLength, pArrayGet, pArrayGetQuantity, nArrayGetLength) # type: ignore

    def LoadItemDefinitions(self, ):
        return ISteamInventory_LoadItemDefinitions(byref(self), ) # type: ignore

    def GetItemDefinitionIDs(self, pItemDefIDs, punItemDefIDsArraySize):
        return ISteamInventory_GetItemDefinitionIDs(byref(self), pItemDefIDs, punItemDefIDsArraySize) # type: ignore

    def GetItemDefinitionProperty(self, iDefinition, pchPropertyName, pchValueBuffer, punValueBufferSizeOut):
        return ISteamInventory_GetItemDefinitionProperty(byref(self), iDefinition, pchPropertyName, pchValueBuffer, punValueBufferSizeOut) # type: ignore

    def RequestEligiblePromoItemDefinitionsIDs(self, steamID):
        return ISteamInventory_RequestEligiblePromoItemDefinitionsIDs(byref(self), steamID) # type: ignore

    def GetEligiblePromoItemDefinitionIDs(self, steamID, pItemDefIDs, punItemDefIDsArraySize):
        return ISteamInventory_GetEligiblePromoItemDefinitionIDs(byref(self), steamID, pItemDefIDs, punItemDefIDsArraySize) # type: ignore

    def StartPurchase(self, pArrayItemDefs, punArrayQuantity, unArrayLength):
        return ISteamInventory_StartPurchase(byref(self), pArrayItemDefs, punArrayQuantity, unArrayLength) # type: ignore

    def RequestPrices(self, ):
        return ISteamInventory_RequestPrices(byref(self), ) # type: ignore

    def GetNumItemsWithPrices(self, ):
        return ISteamInventory_GetNumItemsWithPrices(byref(self), ) # type: ignore

    def GetItemsWithPrices(self, pArrayItemDefs, pCurrentPrices, pBasePrices, unArrayLength):
        return ISteamInventory_GetItemsWithPrices(byref(self), pArrayItemDefs, pCurrentPrices, pBasePrices, unArrayLength) # type: ignore

    def GetItemPrice(self, iDefinition, pCurrentPrice, pBasePrice):
        return ISteamInventory_GetItemPrice(byref(self), iDefinition, pCurrentPrice, pBasePrice) # type: ignore

    def StartUpdateProperties(self, ):
        return ISteamInventory_StartUpdateProperties(byref(self), ) # type: ignore

    def RemoveProperty(self, handle, nItemID, pchPropertyName):
        return ISteamInventory_RemoveProperty(byref(self), handle, nItemID, pchPropertyName) # type: ignore

    def SetPropertyString(self, handle, nItemID, pchPropertyName, pchPropertyValue):
        return ISteamInventory_SetPropertyString(byref(self), handle, nItemID, pchPropertyName, pchPropertyValue) # type: ignore

    def SetPropertyBool(self, handle, nItemID, pchPropertyName, bValue):
        return ISteamInventory_SetPropertyBool(byref(self), handle, nItemID, pchPropertyName, bValue) # type: ignore

    def SetPropertyInt64(self, handle, nItemID, pchPropertyName, nValue):
        return ISteamInventory_SetPropertyInt64(byref(self), handle, nItemID, pchPropertyName, nValue) # type: ignore

    def SetPropertyFloat(self, handle, nItemID, pchPropertyName, flValue):
        return ISteamInventory_SetPropertyFloat(byref(self), handle, nItemID, pchPropertyName, flValue) # type: ignore

    def SubmitUpdateProperties(self, handle, pResultHandle):
        return ISteamInventory_SubmitUpdateProperties(byref(self), handle, pResultHandle) # type: ignore

    def InspectItem(self, pResultHandle, pchItemToken):
        return ISteamInventory_InspectItem(byref(self), pResultHandle, pchItemToken) # type: ignore

class ISteamVideo(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetVideoURL(self, unVideoAppID):
        return ISteamVideo_GetVideoURL(byref(self), unVideoAppID) # type: ignore

    def IsBroadcasting(self, pnNumViewers):
        return ISteamVideo_IsBroadcasting(byref(self), pnNumViewers) # type: ignore

    def GetOPFSettings(self, unVideoAppID):
        return ISteamVideo_GetOPFSettings(byref(self), unVideoAppID) # type: ignore

    def GetOPFStringForApp(self, unVideoAppID, pchBuffer, pnBufferSize):
        return ISteamVideo_GetOPFStringForApp(byref(self), unVideoAppID, pchBuffer, pnBufferSize) # type: ignore

class ISteamParentalSettings(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def BIsParentalLockEnabled(self, ):
        return ISteamParentalSettings_BIsParentalLockEnabled(byref(self), ) # type: ignore

    def BIsParentalLockLocked(self, ):
        return ISteamParentalSettings_BIsParentalLockLocked(byref(self), ) # type: ignore

    def BIsAppBlocked(self, nAppID):
        return ISteamParentalSettings_BIsAppBlocked(byref(self), nAppID) # type: ignore

    def BIsAppInBlockList(self, nAppID):
        return ISteamParentalSettings_BIsAppInBlockList(byref(self), nAppID) # type: ignore

    def BIsFeatureBlocked(self, eFeature):
        return ISteamParentalSettings_BIsFeatureBlocked(byref(self), eFeature) # type: ignore

    def BIsFeatureInBlockList(self, eFeature):
        return ISteamParentalSettings_BIsFeatureInBlockList(byref(self), eFeature) # type: ignore

class ISteamRemotePlay(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def GetSessionCount(self, ):
        return ISteamRemotePlay_GetSessionCount(byref(self), ) # type: ignore

    def GetSessionID(self, iSessionIndex):
        return ISteamRemotePlay_GetSessionID(byref(self), iSessionIndex) # type: ignore

    def GetSessionSteamID(self, unSessionID):
        return ISteamRemotePlay_GetSessionSteamID(byref(self), unSessionID) # type: ignore

    def GetSessionClientName(self, unSessionID):
        return ISteamRemotePlay_GetSessionClientName(byref(self), unSessionID) # type: ignore

    def GetSessionClientFormFactor(self, unSessionID):
        return ISteamRemotePlay_GetSessionClientFormFactor(byref(self), unSessionID) # type: ignore

    def BGetSessionClientResolution(self, unSessionID, pnResolutionX, pnResolutionY):
        return ISteamRemotePlay_BGetSessionClientResolution(byref(self), unSessionID, pnResolutionX, pnResolutionY) # type: ignore

    def BSendRemotePlayTogetherInvite(self, steamIDFriend):
        return ISteamRemotePlay_BSendRemotePlayTogetherInvite(byref(self), steamIDFriend) # type: ignore

class ISteamNetworkingMessages(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def SendMessageToUser(self, identityRemote, pubData, cubData, nSendFlags, nRemoteChannel):
        return ISteamNetworkingMessages_SendMessageToUser(byref(self), identityRemote, pubData, cubData, nSendFlags, nRemoteChannel) # type: ignore

    def ReceiveMessagesOnChannel(self, nLocalChannel, ppOutMessages, nMaxMessages):
        return ISteamNetworkingMessages_ReceiveMessagesOnChannel(byref(self), nLocalChannel, ppOutMessages, nMaxMessages) # type: ignore

    def AcceptSessionWithUser(self, identityRemote):
        return ISteamNetworkingMessages_AcceptSessionWithUser(byref(self), identityRemote) # type: ignore

    def CloseSessionWithUser(self, identityRemote):
        return ISteamNetworkingMessages_CloseSessionWithUser(byref(self), identityRemote) # type: ignore

    def CloseChannelWithUser(self, identityRemote, nLocalChannel):
        return ISteamNetworkingMessages_CloseChannelWithUser(byref(self), identityRemote, nLocalChannel) # type: ignore

    def GetSessionConnectionInfo(self, identityRemote, pConnectionInfo, pQuickStatus):
        return ISteamNetworkingMessages_GetSessionConnectionInfo(byref(self), identityRemote, pConnectionInfo, pQuickStatus) # type: ignore

class ISteamNetworkingSockets(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def CreateListenSocketIP(self, localAddress, nOptions, pOptions):
        return ISteamNetworkingSockets_CreateListenSocketIP(byref(self), localAddress, nOptions, pOptions) # type: ignore

    def ConnectByIPAddress(self, address, nOptions, pOptions):
        return ISteamNetworkingSockets_ConnectByIPAddress(byref(self), address, nOptions, pOptions) # type: ignore

    def CreateListenSocketP2P(self, nLocalVirtualPort, nOptions, pOptions):
        return ISteamNetworkingSockets_CreateListenSocketP2P(byref(self), nLocalVirtualPort, nOptions, pOptions) # type: ignore

    def ConnectP2P(self, identityRemote, nRemoteVirtualPort, nOptions, pOptions):
        return ISteamNetworkingSockets_ConnectP2P(byref(self), identityRemote, nRemoteVirtualPort, nOptions, pOptions) # type: ignore

    def AcceptConnection(self, hConn):
        return ISteamNetworkingSockets_AcceptConnection(byref(self), hConn) # type: ignore

    def CloseConnection(self, hPeer, nReason, pszDebug, bEnableLinger):
        return ISteamNetworkingSockets_CloseConnection(byref(self), hPeer, nReason, pszDebug, bEnableLinger) # type: ignore

    def CloseListenSocket(self, hSocket):
        return ISteamNetworkingSockets_CloseListenSocket(byref(self), hSocket) # type: ignore

    def SetConnectionUserData(self, hPeer, nUserData):
        return ISteamNetworkingSockets_SetConnectionUserData(byref(self), hPeer, nUserData) # type: ignore

    def GetConnectionUserData(self, hPeer):
        return ISteamNetworkingSockets_GetConnectionUserData(byref(self), hPeer) # type: ignore

    def SetConnectionName(self, hPeer, pszName):
        return ISteamNetworkingSockets_SetConnectionName(byref(self), hPeer, pszName) # type: ignore

    def GetConnectionName(self, hPeer, pszName, nMaxLen):
        return ISteamNetworkingSockets_GetConnectionName(byref(self), hPeer, pszName, nMaxLen) # type: ignore

    def SendMessageToConnection(self, hConn, pData, cbData, nSendFlags, pOutMessageNumber):
        return ISteamNetworkingSockets_SendMessageToConnection(byref(self), hConn, pData, cbData, nSendFlags, pOutMessageNumber) # type: ignore

    def SendMessages(self, nMessages, pMessages, pOutMessageNumberOrResult):
        return ISteamNetworkingSockets_SendMessages(byref(self), nMessages, pMessages, pOutMessageNumberOrResult) # type: ignore

    def FlushMessagesOnConnection(self, hConn):
        return ISteamNetworkingSockets_FlushMessagesOnConnection(byref(self), hConn) # type: ignore

    def ReceiveMessagesOnConnection(self, hConn, ppOutMessages, nMaxMessages):
        return ISteamNetworkingSockets_ReceiveMessagesOnConnection(byref(self), hConn, ppOutMessages, nMaxMessages) # type: ignore

    def GetConnectionInfo(self, hConn, pInfo):
        return ISteamNetworkingSockets_GetConnectionInfo(byref(self), hConn, pInfo) # type: ignore

    def GetConnectionRealTimeStatus(self, hConn, pStatus, nLanes, pLanes):
        return ISteamNetworkingSockets_GetConnectionRealTimeStatus(byref(self), hConn, pStatus, nLanes, pLanes) # type: ignore

    def GetDetailedConnectionStatus(self, hConn, pszBuf, cbBuf):
        return ISteamNetworkingSockets_GetDetailedConnectionStatus(byref(self), hConn, pszBuf, cbBuf) # type: ignore

    def GetListenSocketAddress(self, hSocket, address):
        return ISteamNetworkingSockets_GetListenSocketAddress(byref(self), hSocket, address) # type: ignore

    def CreateSocketPair(self, pOutConnection1, pOutConnection2, bUseNetworkLoopback, pIdentity1, pIdentity2):
        return ISteamNetworkingSockets_CreateSocketPair(byref(self), pOutConnection1, pOutConnection2, bUseNetworkLoopback, pIdentity1, pIdentity2) # type: ignore

    def ConfigureConnectionLanes(self, hConn, nNumLanes, pLanePriorities, pLaneWeights):
        return ISteamNetworkingSockets_ConfigureConnectionLanes(byref(self), hConn, nNumLanes, pLanePriorities, pLaneWeights) # type: ignore

    def GetIdentity(self, pIdentity):
        return ISteamNetworkingSockets_GetIdentity(byref(self), pIdentity) # type: ignore

    def InitAuthentication(self, ):
        return ISteamNetworkingSockets_InitAuthentication(byref(self), ) # type: ignore

    def GetAuthenticationStatus(self, pDetails):
        return ISteamNetworkingSockets_GetAuthenticationStatus(byref(self), pDetails) # type: ignore

    def CreatePollGroup(self, ):
        return ISteamNetworkingSockets_CreatePollGroup(byref(self), ) # type: ignore

    def DestroyPollGroup(self, hPollGroup):
        return ISteamNetworkingSockets_DestroyPollGroup(byref(self), hPollGroup) # type: ignore

    def SetConnectionPollGroup(self, hConn, hPollGroup):
        return ISteamNetworkingSockets_SetConnectionPollGroup(byref(self), hConn, hPollGroup) # type: ignore

    def ReceiveMessagesOnPollGroup(self, hPollGroup, ppOutMessages, nMaxMessages):
        return ISteamNetworkingSockets_ReceiveMessagesOnPollGroup(byref(self), hPollGroup, ppOutMessages, nMaxMessages) # type: ignore

    def ReceivedRelayAuthTicket(self, pvTicket, cbTicket, pOutParsedTicket):
        return ISteamNetworkingSockets_ReceivedRelayAuthTicket(byref(self), pvTicket, cbTicket, pOutParsedTicket) # type: ignore

    def FindRelayAuthTicketForServer(self, identityGameServer, nRemoteVirtualPort, pOutParsedTicket):
        return ISteamNetworkingSockets_FindRelayAuthTicketForServer(byref(self), identityGameServer, nRemoteVirtualPort, pOutParsedTicket) # type: ignore

    def ConnectToHostedDedicatedServer(self, identityTarget, nRemoteVirtualPort, nOptions, pOptions):
        return ISteamNetworkingSockets_ConnectToHostedDedicatedServer(byref(self), identityTarget, nRemoteVirtualPort, nOptions, pOptions) # type: ignore

    def GetHostedDedicatedServerPort(self, ):
        return ISteamNetworkingSockets_GetHostedDedicatedServerPort(byref(self), ) # type: ignore

    def GetHostedDedicatedServerPOPID(self, ):
        return ISteamNetworkingSockets_GetHostedDedicatedServerPOPID(byref(self), ) # type: ignore

    def GetHostedDedicatedServerAddress(self, pRouting):
        return ISteamNetworkingSockets_GetHostedDedicatedServerAddress(byref(self), pRouting) # type: ignore

    def CreateHostedDedicatedServerListenSocket(self, nLocalVirtualPort, nOptions, pOptions):
        return ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket(byref(self), nLocalVirtualPort, nOptions, pOptions) # type: ignore

    def GetGameCoordinatorServerLogin(self, pLoginInfo, pcbSignedBlob, pBlob):
        return ISteamNetworkingSockets_GetGameCoordinatorServerLogin(byref(self), pLoginInfo, pcbSignedBlob, pBlob) # type: ignore

    def ConnectP2PCustomSignaling(self, pSignaling, pPeerIdentity, nRemoteVirtualPort, nOptions, pOptions):
        return ISteamNetworkingSockets_ConnectP2PCustomSignaling(byref(self), pSignaling, pPeerIdentity, nRemoteVirtualPort, nOptions, pOptions) # type: ignore

    def ReceivedP2PCustomSignal(self, pMsg, cbMsg, pContext):
        return ISteamNetworkingSockets_ReceivedP2PCustomSignal(byref(self), pMsg, cbMsg, pContext) # type: ignore

    def GetCertificateRequest(self, pcbBlob, pBlob, errMsg):
        return ISteamNetworkingSockets_GetCertificateRequest(byref(self), pcbBlob, pBlob, errMsg) # type: ignore

    def SetCertificate(self, pCertificate, cbCertificate, errMsg):
        return ISteamNetworkingSockets_SetCertificate(byref(self), pCertificate, cbCertificate, errMsg) # type: ignore

    def ResetIdentity(self, pIdentity):
        return ISteamNetworkingSockets_ResetIdentity(byref(self), pIdentity) # type: ignore

    def RunCallbacks(self, ):
        return ISteamNetworkingSockets_RunCallbacks(byref(self), ) # type: ignore

    def BeginAsyncRequestFakeIP(self, nNumPorts):
        return ISteamNetworkingSockets_BeginAsyncRequestFakeIP(byref(self), nNumPorts) # type: ignore

    def GetFakeIP(self, idxFirstPort, pInfo):
        return ISteamNetworkingSockets_GetFakeIP(byref(self), idxFirstPort, pInfo) # type: ignore

    def CreateListenSocketP2PFakeIP(self, idxFakePort, nOptions, pOptions):
        return ISteamNetworkingSockets_CreateListenSocketP2PFakeIP(byref(self), idxFakePort, nOptions, pOptions) # type: ignore

    def GetRemoteFakeIPForConnection(self, hConn, pOutAddr):
        return ISteamNetworkingSockets_GetRemoteFakeIPForConnection(byref(self), hConn, pOutAddr) # type: ignore

    def CreateFakeUDPPort(self, idxFakeServerPort):
        return ISteamNetworkingSockets_CreateFakeUDPPort(byref(self), idxFakeServerPort) # type: ignore

class ISteamNetworkingUtils(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def AllocateMessage(self, cbAllocateBuffer):
        return ISteamNetworkingUtils_AllocateMessage(byref(self), cbAllocateBuffer) # type: ignore

    def InitRelayNetworkAccess(self, ):
        return ISteamNetworkingUtils_InitRelayNetworkAccess(byref(self), ) # type: ignore

    def GetRelayNetworkStatus(self, pDetails):
        return ISteamNetworkingUtils_GetRelayNetworkStatus(byref(self), pDetails) # type: ignore

    def GetLocalPingLocation(self, result):
        return ISteamNetworkingUtils_GetLocalPingLocation(byref(self), result) # type: ignore

    def EstimatePingTimeBetweenTwoLocations(self, location1, location2):
        return ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations(byref(self), location1, location2) # type: ignore

    def EstimatePingTimeFromLocalHost(self, remoteLocation):
        return ISteamNetworkingUtils_EstimatePingTimeFromLocalHost(byref(self), remoteLocation) # type: ignore

    def ConvertPingLocationToString(self, location, pszBuf, cchBufSize):
        return ISteamNetworkingUtils_ConvertPingLocationToString(byref(self), location, pszBuf, cchBufSize) # type: ignore

    def ParsePingLocationString(self, pszString, result):
        return ISteamNetworkingUtils_ParsePingLocationString(byref(self), pszString, result) # type: ignore

    def CheckPingDataUpToDate(self, flMaxAgeSeconds):
        return ISteamNetworkingUtils_CheckPingDataUpToDate(byref(self), flMaxAgeSeconds) # type: ignore

    def GetPingToDataCenter(self, popID, pViaRelayPoP):
        return ISteamNetworkingUtils_GetPingToDataCenter(byref(self), popID, pViaRelayPoP) # type: ignore

    def GetDirectPingToPOP(self, popID):
        return ISteamNetworkingUtils_GetDirectPingToPOP(byref(self), popID) # type: ignore

    def GetPOPCount(self, ):
        return ISteamNetworkingUtils_GetPOPCount(byref(self), ) # type: ignore

    def GetPOPList(self, list, nListSz):
        return ISteamNetworkingUtils_GetPOPList(byref(self), list, nListSz) # type: ignore

    def GetLocalTimestamp(self, ):
        return ISteamNetworkingUtils_GetLocalTimestamp(byref(self), ) # type: ignore

    def SetDebugOutputFunction(self, eDetailLevel, pfnFunc):
        return ISteamNetworkingUtils_SetDebugOutputFunction(byref(self), eDetailLevel, pfnFunc) # type: ignore

    def IsFakeIPv4(self, nIPv4):
        return ISteamNetworkingUtils_IsFakeIPv4(byref(self), nIPv4) # type: ignore

    def GetIPv4FakeIPType(self, nIPv4):
        return ISteamNetworkingUtils_GetIPv4FakeIPType(byref(self), nIPv4) # type: ignore

    def GetRealIdentityForFakeIP(self, fakeIP, pOutRealIdentity):
        return ISteamNetworkingUtils_GetRealIdentityForFakeIP(byref(self), fakeIP, pOutRealIdentity) # type: ignore

    def SetGlobalConfigValueInt32(self, eValue, val):
        return ISteamNetworkingUtils_SetGlobalConfigValueInt32(byref(self), eValue, val) # type: ignore

    def SetGlobalConfigValueFloat(self, eValue, val):
        return ISteamNetworkingUtils_SetGlobalConfigValueFloat(byref(self), eValue, val) # type: ignore

    def SetGlobalConfigValueString(self, eValue, val):
        return ISteamNetworkingUtils_SetGlobalConfigValueString(byref(self), eValue, val) # type: ignore

    def SetGlobalConfigValuePtr(self, eValue, val):
        return ISteamNetworkingUtils_SetGlobalConfigValuePtr(byref(self), eValue, val) # type: ignore

    def SetConnectionConfigValueInt32(self, hConn, eValue, val):
        return ISteamNetworkingUtils_SetConnectionConfigValueInt32(byref(self), hConn, eValue, val) # type: ignore

    def SetConnectionConfigValueFloat(self, hConn, eValue, val):
        return ISteamNetworkingUtils_SetConnectionConfigValueFloat(byref(self), hConn, eValue, val) # type: ignore

    def SetConnectionConfigValueString(self, hConn, eValue, val):
        return ISteamNetworkingUtils_SetConnectionConfigValueString(byref(self), hConn, eValue, val) # type: ignore

    def SetGlobalCallback_SteamNetConnectionStatusChanged(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged(byref(self), fnCallback) # type: ignore

    def SetGlobalCallback_SteamNetAuthenticationStatusChanged(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged(byref(self), fnCallback) # type: ignore

    def SetGlobalCallback_SteamRelayNetworkStatusChanged(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged(byref(self), fnCallback) # type: ignore

    def SetGlobalCallback_FakeIPResult(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult(byref(self), fnCallback) # type: ignore

    def SetGlobalCallback_MessagesSessionRequest(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest(byref(self), fnCallback) # type: ignore

    def SetGlobalCallback_MessagesSessionFailed(self, fnCallback):
        return ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed(byref(self), fnCallback) # type: ignore

    def SetConfigValue(self, eValue, eScopeType, scopeObj, eDataType, pArg):
        return ISteamNetworkingUtils_SetConfigValue(byref(self), eValue, eScopeType, scopeObj, eDataType, pArg) # type: ignore

    def SetConfigValueStruct(self, opt, eScopeType, scopeObj):
        return ISteamNetworkingUtils_SetConfigValueStruct(byref(self), opt, eScopeType, scopeObj) # type: ignore

    def GetConfigValue(self, eValue, eScopeType, scopeObj, pOutDataType, pResult, cbResult):
        return ISteamNetworkingUtils_GetConfigValue(byref(self), eValue, eScopeType, scopeObj, pOutDataType, pResult, cbResult) # type: ignore

    def GetConfigValueInfo(self, eValue, pOutDataType, pOutScope):
        return ISteamNetworkingUtils_GetConfigValueInfo(byref(self), eValue, pOutDataType, pOutScope) # type: ignore

    def IterateGenericEditableConfigValues(self, eCurrent, bEnumerateDevVars):
        return ISteamNetworkingUtils_IterateGenericEditableConfigValues(byref(self), eCurrent, bEnumerateDevVars) # type: ignore

    def SteamNetworkingIPAddr_ToString(self, addr, buf, cbBuf, bWithPort):
        return ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString(byref(self), addr, buf, cbBuf, bWithPort) # type: ignore

    def SteamNetworkingIPAddr_ParseString(self, pAddr, pszStr):
        return ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString(byref(self), pAddr, pszStr) # type: ignore

    def SteamNetworkingIPAddr_GetFakeIPType(self, addr):
        return ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType(byref(self), addr) # type: ignore

    def SteamNetworkingIdentity_ToString(self, identity, buf, cbBuf):
        return ISteamNetworkingUtils_SteamNetworkingIdentity_ToString(byref(self), identity, buf, cbBuf) # type: ignore

    def SteamNetworkingIdentity_ParseString(self, pIdentity, pszStr):
        return ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString(byref(self), pIdentity, pszStr) # type: ignore

class ISteamGameServer(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def SetProduct(self, pszProduct):
        return ISteamGameServer_SetProduct(byref(self), pszProduct) # type: ignore

    def SetGameDescription(self, pszGameDescription):
        return ISteamGameServer_SetGameDescription(byref(self), pszGameDescription) # type: ignore

    def SetModDir(self, pszModDir):
        return ISteamGameServer_SetModDir(byref(self), pszModDir) # type: ignore

    def SetDedicatedServer(self, bDedicated):
        return ISteamGameServer_SetDedicatedServer(byref(self), bDedicated) # type: ignore

    def LogOn(self, pszToken):
        return ISteamGameServer_LogOn(byref(self), pszToken) # type: ignore

    def LogOnAnonymous(self, ):
        return ISteamGameServer_LogOnAnonymous(byref(self), ) # type: ignore

    def LogOff(self, ):
        return ISteamGameServer_LogOff(byref(self), ) # type: ignore

    def BLoggedOn(self, ):
        return ISteamGameServer_BLoggedOn(byref(self), ) # type: ignore

    def BSecure(self, ):
        return ISteamGameServer_BSecure(byref(self), ) # type: ignore

    def GetSteamID(self, ):
        return ISteamGameServer_GetSteamID(byref(self), ) # type: ignore

    def WasRestartRequested(self, ):
        return ISteamGameServer_WasRestartRequested(byref(self), ) # type: ignore

    def SetMaxPlayerCount(self, cPlayersMax):
        return ISteamGameServer_SetMaxPlayerCount(byref(self), cPlayersMax) # type: ignore

    def SetBotPlayerCount(self, cBotplayers):
        return ISteamGameServer_SetBotPlayerCount(byref(self), cBotplayers) # type: ignore

    def SetServerName(self, pszServerName):
        return ISteamGameServer_SetServerName(byref(self), pszServerName) # type: ignore

    def SetMapName(self, pszMapName):
        return ISteamGameServer_SetMapName(byref(self), pszMapName) # type: ignore

    def SetPasswordProtected(self, bPasswordProtected):
        return ISteamGameServer_SetPasswordProtected(byref(self), bPasswordProtected) # type: ignore

    def SetSpectatorPort(self, unSpectatorPort):
        return ISteamGameServer_SetSpectatorPort(byref(self), unSpectatorPort) # type: ignore

    def SetSpectatorServerName(self, pszSpectatorServerName):
        return ISteamGameServer_SetSpectatorServerName(byref(self), pszSpectatorServerName) # type: ignore

    def ClearAllKeyValues(self, ):
        return ISteamGameServer_ClearAllKeyValues(byref(self), ) # type: ignore

    def SetKeyValue(self, pKey, pValue):
        return ISteamGameServer_SetKeyValue(byref(self), pKey, pValue) # type: ignore

    def SetGameTags(self, pchGameTags):
        return ISteamGameServer_SetGameTags(byref(self), pchGameTags) # type: ignore

    def SetGameData(self, pchGameData):
        return ISteamGameServer_SetGameData(byref(self), pchGameData) # type: ignore

    def SetRegion(self, pszRegion):
        return ISteamGameServer_SetRegion(byref(self), pszRegion) # type: ignore

    def SetAdvertiseServerActive(self, bActive):
        return ISteamGameServer_SetAdvertiseServerActive(byref(self), bActive) # type: ignore

    def GetAuthSessionTicket(self, pTicket, cbMaxTicket, pcbTicket):
        return ISteamGameServer_GetAuthSessionTicket(byref(self), pTicket, cbMaxTicket, pcbTicket) # type: ignore

    def BeginAuthSession(self, pAuthTicket, cbAuthTicket, steamID):
        return ISteamGameServer_BeginAuthSession(byref(self), pAuthTicket, cbAuthTicket, steamID) # type: ignore

    def EndAuthSession(self, steamID):
        return ISteamGameServer_EndAuthSession(byref(self), steamID) # type: ignore

    def CancelAuthTicket(self, hAuthTicket):
        return ISteamGameServer_CancelAuthTicket(byref(self), hAuthTicket) # type: ignore

    def UserHasLicenseForApp(self, steamID, appID):
        return ISteamGameServer_UserHasLicenseForApp(byref(self), steamID, appID) # type: ignore

    def RequestUserGroupStatus(self, steamIDUser, steamIDGroup):
        return ISteamGameServer_RequestUserGroupStatus(byref(self), steamIDUser, steamIDGroup) # type: ignore

    def GetGameplayStats(self, ):
        return ISteamGameServer_GetGameplayStats(byref(self), ) # type: ignore

    def GetServerReputation(self, ):
        return ISteamGameServer_GetServerReputation(byref(self), ) # type: ignore

    def GetPublicIP(self, ):
        return ISteamGameServer_GetPublicIP(byref(self), ) # type: ignore

    def HandleIncomingPacket(self, pData, cbData, srcIP, srcPort):
        return ISteamGameServer_HandleIncomingPacket(byref(self), pData, cbData, srcIP, srcPort) # type: ignore

    def GetNextOutgoingPacket(self, pOut, cbMaxOut, pNetAdr, pPort):
        return ISteamGameServer_GetNextOutgoingPacket(byref(self), pOut, cbMaxOut, pNetAdr, pPort) # type: ignore

    def AssociateWithClan(self, steamIDClan):
        return ISteamGameServer_AssociateWithClan(byref(self), steamIDClan) # type: ignore

    def ComputeNewPlayerCompatibility(self, steamIDNewPlayer):
        return ISteamGameServer_ComputeNewPlayerCompatibility(byref(self), steamIDNewPlayer) # type: ignore

    def SendUserConnectAndAuthenticate_DEPRECATED(self, unIPClient, pvAuthBlob, cubAuthBlobSize, pSteamIDUser):
        return ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED(byref(self), unIPClient, pvAuthBlob, cubAuthBlobSize, pSteamIDUser) # type: ignore

    def CreateUnauthenticatedUserConnection(self, ):
        return ISteamGameServer_CreateUnauthenticatedUserConnection(byref(self), ) # type: ignore

    def SendUserDisconnect_DEPRECATED(self, steamIDUser):
        return ISteamGameServer_SendUserDisconnect_DEPRECATED(byref(self), steamIDUser) # type: ignore

    def BUpdateUserData(self, steamIDUser, pchPlayerName, uScore):
        return ISteamGameServer_BUpdateUserData(byref(self), steamIDUser, pchPlayerName, uScore) # type: ignore

class ISteamGameServerStats(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def RequestUserStats(self, steamIDUser):
        return ISteamGameServerStats_RequestUserStats(byref(self), steamIDUser) # type: ignore

    def GetUserStatInt32(self, steamIDUser, pchName, pData):
        return ISteamGameServerStats_GetUserStatInt32(byref(self), steamIDUser, pchName, pData) # type: ignore

    def GetUserStatFloat(self, steamIDUser, pchName, pData):
        return ISteamGameServerStats_GetUserStatFloat(byref(self), steamIDUser, pchName, pData) # type: ignore

    def GetUserAchievement(self, steamIDUser, pchName, pbAchieved):
        return ISteamGameServerStats_GetUserAchievement(byref(self), steamIDUser, pchName, pbAchieved) # type: ignore

    def SetUserStatInt32(self, steamIDUser, pchName, nData):
        return ISteamGameServerStats_SetUserStatInt32(byref(self), steamIDUser, pchName, nData) # type: ignore

    def SetUserStatFloat(self, steamIDUser, pchName, fData):
        return ISteamGameServerStats_SetUserStatFloat(byref(self), steamIDUser, pchName, fData) # type: ignore

    def UpdateUserAvgRateStat(self, steamIDUser, pchName, flCountThisSession, dSessionLength):
        return ISteamGameServerStats_UpdateUserAvgRateStat(byref(self), steamIDUser, pchName, flCountThisSession, dSessionLength) # type: ignore

    def SetUserAchievement(self, steamIDUser, pchName):
        return ISteamGameServerStats_SetUserAchievement(byref(self), steamIDUser, pchName) # type: ignore

    def ClearUserAchievement(self, steamIDUser, pchName):
        return ISteamGameServerStats_ClearUserAchievement(byref(self), steamIDUser, pchName) # type: ignore

    def StoreUserStats(self, steamIDUser):
        return ISteamGameServerStats_StoreUserStats(byref(self), steamIDUser) # type: ignore

class ISteamNetworkingFakeUDPPort(Structure):
    _pack_ = PACK
    _fields_ = [
    ]

    def DestroyFakeUDPPort(self, ):
        return ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort(byref(self), ) # type: ignore

    def SendMessageToFakeIP(self, remoteAddress, pData, cbData, nSendFlags):
        return ISteamNetworkingFakeUDPPort_SendMessageToFakeIP(byref(self), remoteAddress, pData, cbData, nSendFlags) # type: ignore

    def ReceiveMessages(self, ppOutMessages, nMaxMessages):
        return ISteamNetworkingFakeUDPPort_ReceiveMessages(byref(self), ppOutMessages, nMaxMessages) # type: ignore

    def ScheduleCleanup(self, remoteAddress):
        return ISteamNetworkingFakeUDPPort_ScheduleCleanup(byref(self), remoteAddress) # type: ignore
def load(dll):


    global SteamIPAddress_t_IsSet
    SteamIPAddress_t_IsSet = dll.SteamAPI_SteamIPAddress_t_IsSet
    SteamIPAddress_t_IsSet.argtypes = [ POINTER(SteamIPAddress_t),  ]
    SteamIPAddress_t_IsSet.restype = c_bool

    global MatchMakingKeyValuePair_t_Construct
    MatchMakingKeyValuePair_t_Construct = dll.SteamAPI_MatchMakingKeyValuePair_t_Construct
    MatchMakingKeyValuePair_t_Construct.argtypes = [ POINTER(MatchMakingKeyValuePair_t),  ]
    MatchMakingKeyValuePair_t_Construct.restype = None

    global servernetadr_t_Construct
    servernetadr_t_Construct = dll.SteamAPI_servernetadr_t_Construct
    servernetadr_t_Construct.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_Construct.restype = None

    global servernetadr_t_Init
    servernetadr_t_Init = dll.SteamAPI_servernetadr_t_Init
    servernetadr_t_Init.argtypes = [ POINTER(servernetadr_t), c_uint, c_ushort, c_ushort ]
    servernetadr_t_Init.restype = None

    global servernetadr_t_GetQueryPort
    servernetadr_t_GetQueryPort = dll.SteamAPI_servernetadr_t_GetQueryPort
    servernetadr_t_GetQueryPort.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_GetQueryPort.restype = c_ushort

    global servernetadr_t_SetQueryPort
    servernetadr_t_SetQueryPort = dll.SteamAPI_servernetadr_t_SetQueryPort
    servernetadr_t_SetQueryPort.argtypes = [ POINTER(servernetadr_t), c_ushort ]
    servernetadr_t_SetQueryPort.restype = None

    global servernetadr_t_GetConnectionPort
    servernetadr_t_GetConnectionPort = dll.SteamAPI_servernetadr_t_GetConnectionPort
    servernetadr_t_GetConnectionPort.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_GetConnectionPort.restype = c_ushort

    global servernetadr_t_SetConnectionPort
    servernetadr_t_SetConnectionPort = dll.SteamAPI_servernetadr_t_SetConnectionPort
    servernetadr_t_SetConnectionPort.argtypes = [ POINTER(servernetadr_t), c_ushort ]
    servernetadr_t_SetConnectionPort.restype = None

    global servernetadr_t_GetIP
    servernetadr_t_GetIP = dll.SteamAPI_servernetadr_t_GetIP
    servernetadr_t_GetIP.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_GetIP.restype = c_uint

    global servernetadr_t_SetIP
    servernetadr_t_SetIP = dll.SteamAPI_servernetadr_t_SetIP
    servernetadr_t_SetIP.argtypes = [ POINTER(servernetadr_t), c_uint ]
    servernetadr_t_SetIP.restype = None

    global servernetadr_t_GetConnectionAddressString
    servernetadr_t_GetConnectionAddressString = dll.SteamAPI_servernetadr_t_GetConnectionAddressString
    servernetadr_t_GetConnectionAddressString.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_GetConnectionAddressString.restype = c_char_p

    global servernetadr_t_GetQueryAddressString
    servernetadr_t_GetQueryAddressString = dll.SteamAPI_servernetadr_t_GetQueryAddressString
    servernetadr_t_GetQueryAddressString.argtypes = [ POINTER(servernetadr_t),  ]
    servernetadr_t_GetQueryAddressString.restype = c_char_p

    global servernetadr_t_IsLessThan
    servernetadr_t_IsLessThan = dll.SteamAPI_servernetadr_t_IsLessThan
    servernetadr_t_IsLessThan.argtypes = [ POINTER(servernetadr_t), POINTER(servernetadr_t) ]
    servernetadr_t_IsLessThan.restype = c_bool

    global servernetadr_t_Assign
    servernetadr_t_Assign = dll.SteamAPI_servernetadr_t_Assign
    servernetadr_t_Assign.argtypes = [ POINTER(servernetadr_t), POINTER(servernetadr_t) ]
    servernetadr_t_Assign.restype = None

    global gameserveritem_t_Construct
    gameserveritem_t_Construct = dll.SteamAPI_gameserveritem_t_Construct
    gameserveritem_t_Construct.argtypes = [ POINTER(gameserveritem_t),  ]
    gameserveritem_t_Construct.restype = None

    global gameserveritem_t_GetName
    gameserveritem_t_GetName = dll.SteamAPI_gameserveritem_t_GetName
    gameserveritem_t_GetName.argtypes = [ POINTER(gameserveritem_t),  ]
    gameserveritem_t_GetName.restype = c_char_p

    global gameserveritem_t_SetName
    gameserveritem_t_SetName = dll.SteamAPI_gameserveritem_t_SetName
    gameserveritem_t_SetName.argtypes = [ POINTER(gameserveritem_t), c_char_p ]
    gameserveritem_t_SetName.restype = None

    global SteamNetworkingIPAddr_Clear
    SteamNetworkingIPAddr_Clear = dll.SteamAPI_SteamNetworkingIPAddr_Clear
    SteamNetworkingIPAddr_Clear.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_Clear.restype = None

    global SteamNetworkingIPAddr_IsIPv6AllZeros
    SteamNetworkingIPAddr_IsIPv6AllZeros = dll.SteamAPI_SteamNetworkingIPAddr_IsIPv6AllZeros
    SteamNetworkingIPAddr_IsIPv6AllZeros.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_IsIPv6AllZeros.restype = c_bool

    global SteamNetworkingIPAddr_SetIPv6
    SteamNetworkingIPAddr_SetIPv6 = dll.SteamAPI_SteamNetworkingIPAddr_SetIPv6
    SteamNetworkingIPAddr_SetIPv6.argtypes = [ POINTER(SteamNetworkingIPAddr), POINTER(c_ubyte), c_ushort ]
    SteamNetworkingIPAddr_SetIPv6.restype = None

    global SteamNetworkingIPAddr_SetIPv4
    SteamNetworkingIPAddr_SetIPv4 = dll.SteamAPI_SteamNetworkingIPAddr_SetIPv4
    SteamNetworkingIPAddr_SetIPv4.argtypes = [ POINTER(SteamNetworkingIPAddr), c_uint, c_ushort ]
    SteamNetworkingIPAddr_SetIPv4.restype = None

    global SteamNetworkingIPAddr_IsIPv4
    SteamNetworkingIPAddr_IsIPv4 = dll.SteamAPI_SteamNetworkingIPAddr_IsIPv4
    SteamNetworkingIPAddr_IsIPv4.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_IsIPv4.restype = c_bool

    global SteamNetworkingIPAddr_GetIPv4
    SteamNetworkingIPAddr_GetIPv4 = dll.SteamAPI_SteamNetworkingIPAddr_GetIPv4
    SteamNetworkingIPAddr_GetIPv4.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_GetIPv4.restype = c_uint

    global SteamNetworkingIPAddr_SetIPv6LocalHost
    SteamNetworkingIPAddr_SetIPv6LocalHost = dll.SteamAPI_SteamNetworkingIPAddr_SetIPv6LocalHost
    SteamNetworkingIPAddr_SetIPv6LocalHost.argtypes = [ POINTER(SteamNetworkingIPAddr), c_ushort ]
    SteamNetworkingIPAddr_SetIPv6LocalHost.restype = None

    global SteamNetworkingIPAddr_IsLocalHost
    SteamNetworkingIPAddr_IsLocalHost = dll.SteamAPI_SteamNetworkingIPAddr_IsLocalHost
    SteamNetworkingIPAddr_IsLocalHost.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_IsLocalHost.restype = c_bool

    global SteamNetworkingIPAddr_ToString
    SteamNetworkingIPAddr_ToString = dll.SteamAPI_SteamNetworkingIPAddr_ToString
    SteamNetworkingIPAddr_ToString.argtypes = [ POINTER(SteamNetworkingIPAddr), c_char_p, c_uint, c_bool ]
    SteamNetworkingIPAddr_ToString.restype = None

    global SteamNetworkingIPAddr_ParseString
    SteamNetworkingIPAddr_ParseString = dll.SteamAPI_SteamNetworkingIPAddr_ParseString
    SteamNetworkingIPAddr_ParseString.argtypes = [ POINTER(SteamNetworkingIPAddr), c_char_p ]
    SteamNetworkingIPAddr_ParseString.restype = c_bool

    global SteamNetworkingIPAddr_IsEqualTo
    SteamNetworkingIPAddr_IsEqualTo = dll.SteamAPI_SteamNetworkingIPAddr_IsEqualTo
    SteamNetworkingIPAddr_IsEqualTo.argtypes = [ POINTER(SteamNetworkingIPAddr), POINTER(SteamNetworkingIPAddr) ]
    SteamNetworkingIPAddr_IsEqualTo.restype = c_bool

    global SteamNetworkingIPAddr_GetFakeIPType
    SteamNetworkingIPAddr_GetFakeIPType = dll.SteamAPI_SteamNetworkingIPAddr_GetFakeIPType
    SteamNetworkingIPAddr_GetFakeIPType.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_GetFakeIPType.restype = ESteamNetworkingFakeIPType

    global SteamNetworkingIPAddr_IsFakeIP
    SteamNetworkingIPAddr_IsFakeIP = dll.SteamAPI_SteamNetworkingIPAddr_IsFakeIP
    SteamNetworkingIPAddr_IsFakeIP.argtypes = [ POINTER(SteamNetworkingIPAddr),  ]
    SteamNetworkingIPAddr_IsFakeIP.restype = c_bool

    global SteamNetworkingIdentity_Clear
    SteamNetworkingIdentity_Clear = dll.SteamAPI_SteamNetworkingIdentity_Clear
    SteamNetworkingIdentity_Clear.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_Clear.restype = None

    global SteamNetworkingIdentity_IsInvalid
    SteamNetworkingIdentity_IsInvalid = dll.SteamAPI_SteamNetworkingIdentity_IsInvalid
    SteamNetworkingIdentity_IsInvalid.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_IsInvalid.restype = c_bool

    global SteamNetworkingIdentity_SetSteamID
    SteamNetworkingIdentity_SetSteamID = dll.SteamAPI_SteamNetworkingIdentity_SetSteamID
    SteamNetworkingIdentity_SetSteamID.argtypes = [ POINTER(SteamNetworkingIdentity), c_ulonglong ]
    SteamNetworkingIdentity_SetSteamID.restype = None

    global SteamNetworkingIdentity_GetSteamID
    SteamNetworkingIdentity_GetSteamID = dll.SteamAPI_SteamNetworkingIdentity_GetSteamID
    SteamNetworkingIdentity_GetSteamID.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetSteamID.restype = c_ulonglong

    global SteamNetworkingIdentity_SetSteamID64
    SteamNetworkingIdentity_SetSteamID64 = dll.SteamAPI_SteamNetworkingIdentity_SetSteamID64
    SteamNetworkingIdentity_SetSteamID64.argtypes = [ POINTER(SteamNetworkingIdentity), c_ulonglong ]
    SteamNetworkingIdentity_SetSteamID64.restype = None

    global SteamNetworkingIdentity_GetSteamID64
    SteamNetworkingIdentity_GetSteamID64 = dll.SteamAPI_SteamNetworkingIdentity_GetSteamID64
    SteamNetworkingIdentity_GetSteamID64.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetSteamID64.restype = c_ulonglong

    global SteamNetworkingIdentity_SetXboxPairwiseID
    SteamNetworkingIdentity_SetXboxPairwiseID = dll.SteamAPI_SteamNetworkingIdentity_SetXboxPairwiseID
    SteamNetworkingIdentity_SetXboxPairwiseID.argtypes = [ POINTER(SteamNetworkingIdentity), c_char_p ]
    SteamNetworkingIdentity_SetXboxPairwiseID.restype = c_bool

    global SteamNetworkingIdentity_GetXboxPairwiseID
    SteamNetworkingIdentity_GetXboxPairwiseID = dll.SteamAPI_SteamNetworkingIdentity_GetXboxPairwiseID
    SteamNetworkingIdentity_GetXboxPairwiseID.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetXboxPairwiseID.restype = c_char_p

    global SteamNetworkingIdentity_SetPSNID
    SteamNetworkingIdentity_SetPSNID = dll.SteamAPI_SteamNetworkingIdentity_SetPSNID
    SteamNetworkingIdentity_SetPSNID.argtypes = [ POINTER(SteamNetworkingIdentity), c_ulonglong ]
    SteamNetworkingIdentity_SetPSNID.restype = None

    global SteamNetworkingIdentity_GetPSNID
    SteamNetworkingIdentity_GetPSNID = dll.SteamAPI_SteamNetworkingIdentity_GetPSNID
    SteamNetworkingIdentity_GetPSNID.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetPSNID.restype = c_ulonglong

    global SteamNetworkingIdentity_SetStadiaID
    SteamNetworkingIdentity_SetStadiaID = dll.SteamAPI_SteamNetworkingIdentity_SetStadiaID
    SteamNetworkingIdentity_SetStadiaID.argtypes = [ POINTER(SteamNetworkingIdentity), c_ulonglong ]
    SteamNetworkingIdentity_SetStadiaID.restype = None

    global SteamNetworkingIdentity_GetStadiaID
    SteamNetworkingIdentity_GetStadiaID = dll.SteamAPI_SteamNetworkingIdentity_GetStadiaID
    SteamNetworkingIdentity_GetStadiaID.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetStadiaID.restype = c_ulonglong

    global SteamNetworkingIdentity_SetIPAddr
    SteamNetworkingIdentity_SetIPAddr = dll.SteamAPI_SteamNetworkingIdentity_SetIPAddr
    SteamNetworkingIdentity_SetIPAddr.argtypes = [ POINTER(SteamNetworkingIdentity), POINTER(SteamNetworkingIPAddr) ]
    SteamNetworkingIdentity_SetIPAddr.restype = None

    global SteamNetworkingIdentity_GetIPAddr
    SteamNetworkingIdentity_GetIPAddr = dll.SteamAPI_SteamNetworkingIdentity_GetIPAddr
    SteamNetworkingIdentity_GetIPAddr.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetIPAddr.restype = POINTER(SteamNetworkingIPAddr)

    global SteamNetworkingIdentity_SetIPv4Addr
    SteamNetworkingIdentity_SetIPv4Addr = dll.SteamAPI_SteamNetworkingIdentity_SetIPv4Addr
    SteamNetworkingIdentity_SetIPv4Addr.argtypes = [ POINTER(SteamNetworkingIdentity), c_uint, c_ushort ]
    SteamNetworkingIdentity_SetIPv4Addr.restype = None

    global SteamNetworkingIdentity_GetIPv4
    SteamNetworkingIdentity_GetIPv4 = dll.SteamAPI_SteamNetworkingIdentity_GetIPv4
    SteamNetworkingIdentity_GetIPv4.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetIPv4.restype = c_uint

    global SteamNetworkingIdentity_GetFakeIPType
    SteamNetworkingIdentity_GetFakeIPType = dll.SteamAPI_SteamNetworkingIdentity_GetFakeIPType
    SteamNetworkingIdentity_GetFakeIPType.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetFakeIPType.restype = ESteamNetworkingFakeIPType

    global SteamNetworkingIdentity_IsFakeIP
    SteamNetworkingIdentity_IsFakeIP = dll.SteamAPI_SteamNetworkingIdentity_IsFakeIP
    SteamNetworkingIdentity_IsFakeIP.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_IsFakeIP.restype = c_bool

    global SteamNetworkingIdentity_SetLocalHost
    SteamNetworkingIdentity_SetLocalHost = dll.SteamAPI_SteamNetworkingIdentity_SetLocalHost
    SteamNetworkingIdentity_SetLocalHost.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_SetLocalHost.restype = None

    global SteamNetworkingIdentity_IsLocalHost
    SteamNetworkingIdentity_IsLocalHost = dll.SteamAPI_SteamNetworkingIdentity_IsLocalHost
    SteamNetworkingIdentity_IsLocalHost.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_IsLocalHost.restype = c_bool

    global SteamNetworkingIdentity_SetGenericString
    SteamNetworkingIdentity_SetGenericString = dll.SteamAPI_SteamNetworkingIdentity_SetGenericString
    SteamNetworkingIdentity_SetGenericString.argtypes = [ POINTER(SteamNetworkingIdentity), c_char_p ]
    SteamNetworkingIdentity_SetGenericString.restype = c_bool

    global SteamNetworkingIdentity_GetGenericString
    SteamNetworkingIdentity_GetGenericString = dll.SteamAPI_SteamNetworkingIdentity_GetGenericString
    SteamNetworkingIdentity_GetGenericString.argtypes = [ POINTER(SteamNetworkingIdentity),  ]
    SteamNetworkingIdentity_GetGenericString.restype = c_char_p

    global SteamNetworkingIdentity_SetGenericBytes
    SteamNetworkingIdentity_SetGenericBytes = dll.SteamAPI_SteamNetworkingIdentity_SetGenericBytes
    SteamNetworkingIdentity_SetGenericBytes.argtypes = [ POINTER(SteamNetworkingIdentity), c_void_p, c_uint ]
    SteamNetworkingIdentity_SetGenericBytes.restype = c_bool

    global SteamNetworkingIdentity_GetGenericBytes
    SteamNetworkingIdentity_GetGenericBytes = dll.SteamAPI_SteamNetworkingIdentity_GetGenericBytes
    SteamNetworkingIdentity_GetGenericBytes.argtypes = [ POINTER(SteamNetworkingIdentity), POINTER(c_int) ]
    SteamNetworkingIdentity_GetGenericBytes.restype = POINTER(c_ubyte)

    global SteamNetworkingIdentity_IsEqualTo
    SteamNetworkingIdentity_IsEqualTo = dll.SteamAPI_SteamNetworkingIdentity_IsEqualTo
    SteamNetworkingIdentity_IsEqualTo.argtypes = [ POINTER(SteamNetworkingIdentity), POINTER(SteamNetworkingIdentity) ]
    SteamNetworkingIdentity_IsEqualTo.restype = c_bool

    global SteamNetworkingIdentity_ToString
    SteamNetworkingIdentity_ToString = dll.SteamAPI_SteamNetworkingIdentity_ToString
    SteamNetworkingIdentity_ToString.argtypes = [ POINTER(SteamNetworkingIdentity), c_char_p, c_uint ]
    SteamNetworkingIdentity_ToString.restype = None

    global SteamNetworkingIdentity_ParseString
    SteamNetworkingIdentity_ParseString = dll.SteamAPI_SteamNetworkingIdentity_ParseString
    SteamNetworkingIdentity_ParseString.argtypes = [ POINTER(SteamNetworkingIdentity), c_char_p ]
    SteamNetworkingIdentity_ParseString.restype = c_bool

    global SteamNetworkingMessage_t_Release
    SteamNetworkingMessage_t_Release = dll.SteamAPI_SteamNetworkingMessage_t_Release
    SteamNetworkingMessage_t_Release.argtypes = [ POINTER(SteamNetworkingMessage_t),  ]
    SteamNetworkingMessage_t_Release.restype = None

    global SteamNetworkingConfigValue_t_SetInt32
    SteamNetworkingConfigValue_t_SetInt32 = dll.SteamAPI_SteamNetworkingConfigValue_t_SetInt32
    SteamNetworkingConfigValue_t_SetInt32.argtypes = [ POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigValue, c_int ]
    SteamNetworkingConfigValue_t_SetInt32.restype = None

    global SteamNetworkingConfigValue_t_SetInt64
    SteamNetworkingConfigValue_t_SetInt64 = dll.SteamAPI_SteamNetworkingConfigValue_t_SetInt64
    SteamNetworkingConfigValue_t_SetInt64.argtypes = [ POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigValue, c_longlong ]
    SteamNetworkingConfigValue_t_SetInt64.restype = None

    global SteamNetworkingConfigValue_t_SetFloat
    SteamNetworkingConfigValue_t_SetFloat = dll.SteamAPI_SteamNetworkingConfigValue_t_SetFloat
    SteamNetworkingConfigValue_t_SetFloat.argtypes = [ POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigValue, c_float ]
    SteamNetworkingConfigValue_t_SetFloat.restype = None

    global SteamNetworkingConfigValue_t_SetPtr
    SteamNetworkingConfigValue_t_SetPtr = dll.SteamAPI_SteamNetworkingConfigValue_t_SetPtr
    SteamNetworkingConfigValue_t_SetPtr.argtypes = [ POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigValue, c_void_p ]
    SteamNetworkingConfigValue_t_SetPtr.restype = None

    global SteamNetworkingConfigValue_t_SetString
    SteamNetworkingConfigValue_t_SetString = dll.SteamAPI_SteamNetworkingConfigValue_t_SetString
    SteamNetworkingConfigValue_t_SetString.argtypes = [ POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigValue, c_char_p ]
    SteamNetworkingConfigValue_t_SetString.restype = None

    global SteamDatagramHostedAddress_Clear
    SteamDatagramHostedAddress_Clear = dll.SteamAPI_SteamDatagramHostedAddress_Clear
    SteamDatagramHostedAddress_Clear.argtypes = [ POINTER(SteamDatagramHostedAddress),  ]
    SteamDatagramHostedAddress_Clear.restype = None

    global SteamDatagramHostedAddress_GetPopID
    SteamDatagramHostedAddress_GetPopID = dll.SteamAPI_SteamDatagramHostedAddress_GetPopID
    SteamDatagramHostedAddress_GetPopID.argtypes = [ POINTER(SteamDatagramHostedAddress),  ]
    SteamDatagramHostedAddress_GetPopID.restype = c_uint

    global SteamDatagramHostedAddress_SetDevAddress
    SteamDatagramHostedAddress_SetDevAddress = dll.SteamAPI_SteamDatagramHostedAddress_SetDevAddress
    SteamDatagramHostedAddress_SetDevAddress.argtypes = [ POINTER(SteamDatagramHostedAddress), c_uint, c_ushort, c_uint ]
    SteamDatagramHostedAddress_SetDevAddress.restype = None

    global ISteamClient_CreateSteamPipe
    ISteamClient_CreateSteamPipe = dll.SteamAPI_ISteamClient_CreateSteamPipe
    ISteamClient_CreateSteamPipe.argtypes = [ POINTER(ISteamClient),  ]
    ISteamClient_CreateSteamPipe.restype = c_int

    global ISteamClient_BReleaseSteamPipe
    ISteamClient_BReleaseSteamPipe = dll.SteamAPI_ISteamClient_BReleaseSteamPipe
    ISteamClient_BReleaseSteamPipe.argtypes = [ POINTER(ISteamClient), c_int ]
    ISteamClient_BReleaseSteamPipe.restype = c_bool

    global ISteamClient_ConnectToGlobalUser
    ISteamClient_ConnectToGlobalUser = dll.SteamAPI_ISteamClient_ConnectToGlobalUser
    ISteamClient_ConnectToGlobalUser.argtypes = [ POINTER(ISteamClient), c_int ]
    ISteamClient_ConnectToGlobalUser.restype = c_int

    global ISteamClient_CreateLocalUser
    ISteamClient_CreateLocalUser = dll.SteamAPI_ISteamClient_CreateLocalUser
    ISteamClient_CreateLocalUser.argtypes = [ POINTER(ISteamClient), POINTER(c_int), EAccountType ]
    ISteamClient_CreateLocalUser.restype = c_int

    global ISteamClient_ReleaseUser
    ISteamClient_ReleaseUser = dll.SteamAPI_ISteamClient_ReleaseUser
    ISteamClient_ReleaseUser.argtypes = [ POINTER(ISteamClient), c_int, c_int ]
    ISteamClient_ReleaseUser.restype = None

    global ISteamClient_GetISteamUser
    ISteamClient_GetISteamUser = dll.SteamAPI_ISteamClient_GetISteamUser
    ISteamClient_GetISteamUser.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamUser.restype = POINTER(ISteamUser)

    global ISteamClient_GetISteamGameServer
    ISteamClient_GetISteamGameServer = dll.SteamAPI_ISteamClient_GetISteamGameServer
    ISteamClient_GetISteamGameServer.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamGameServer.restype = POINTER(ISteamGameServer)

    global ISteamClient_SetLocalIPBinding
    ISteamClient_SetLocalIPBinding = dll.SteamAPI_ISteamClient_SetLocalIPBinding
    ISteamClient_SetLocalIPBinding.argtypes = [ POINTER(ISteamClient), POINTER(SteamIPAddress_t), c_ushort ]
    ISteamClient_SetLocalIPBinding.restype = None

    global ISteamClient_GetISteamFriends
    ISteamClient_GetISteamFriends = dll.SteamAPI_ISteamClient_GetISteamFriends
    ISteamClient_GetISteamFriends.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamFriends.restype = POINTER(ISteamFriends)

    global ISteamClient_GetISteamUtils
    ISteamClient_GetISteamUtils = dll.SteamAPI_ISteamClient_GetISteamUtils
    ISteamClient_GetISteamUtils.argtypes = [ POINTER(ISteamClient), c_int, c_char_p ]
    ISteamClient_GetISteamUtils.restype = POINTER(ISteamUtils)

    global ISteamClient_GetISteamMatchmaking
    ISteamClient_GetISteamMatchmaking = dll.SteamAPI_ISteamClient_GetISteamMatchmaking
    ISteamClient_GetISteamMatchmaking.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamMatchmaking.restype = POINTER(ISteamMatchmaking)

    global ISteamClient_GetISteamMatchmakingServers
    ISteamClient_GetISteamMatchmakingServers = dll.SteamAPI_ISteamClient_GetISteamMatchmakingServers
    ISteamClient_GetISteamMatchmakingServers.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamMatchmakingServers.restype = POINTER(ISteamMatchmakingServers)

    global ISteamClient_GetISteamGenericInterface
    ISteamClient_GetISteamGenericInterface = dll.SteamAPI_ISteamClient_GetISteamGenericInterface
    ISteamClient_GetISteamGenericInterface.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamGenericInterface.restype = c_void_p

    global ISteamClient_GetISteamUserStats
    ISteamClient_GetISteamUserStats = dll.SteamAPI_ISteamClient_GetISteamUserStats
    ISteamClient_GetISteamUserStats.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamUserStats.restype = POINTER(ISteamUserStats)

    global ISteamClient_GetISteamGameServerStats
    ISteamClient_GetISteamGameServerStats = dll.SteamAPI_ISteamClient_GetISteamGameServerStats
    ISteamClient_GetISteamGameServerStats.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamGameServerStats.restype = POINTER(ISteamGameServerStats)

    global ISteamClient_GetISteamApps
    ISteamClient_GetISteamApps = dll.SteamAPI_ISteamClient_GetISteamApps
    ISteamClient_GetISteamApps.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamApps.restype = POINTER(ISteamApps)

    global ISteamClient_GetISteamNetworking
    ISteamClient_GetISteamNetworking = dll.SteamAPI_ISteamClient_GetISteamNetworking
    ISteamClient_GetISteamNetworking.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamNetworking.restype = POINTER(ISteamNetworking)

    global ISteamClient_GetISteamRemoteStorage
    ISteamClient_GetISteamRemoteStorage = dll.SteamAPI_ISteamClient_GetISteamRemoteStorage
    ISteamClient_GetISteamRemoteStorage.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamRemoteStorage.restype = POINTER(ISteamRemoteStorage)

    global ISteamClient_GetISteamScreenshots
    ISteamClient_GetISteamScreenshots = dll.SteamAPI_ISteamClient_GetISteamScreenshots
    ISteamClient_GetISteamScreenshots.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamScreenshots.restype = POINTER(ISteamScreenshots)

    global ISteamClient_GetISteamGameSearch
    ISteamClient_GetISteamGameSearch = dll.SteamAPI_ISteamClient_GetISteamGameSearch
    ISteamClient_GetISteamGameSearch.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamGameSearch.restype = POINTER(ISteamGameSearch)

    global ISteamClient_GetIPCCallCount
    ISteamClient_GetIPCCallCount = dll.SteamAPI_ISteamClient_GetIPCCallCount
    ISteamClient_GetIPCCallCount.argtypes = [ POINTER(ISteamClient),  ]
    ISteamClient_GetIPCCallCount.restype = c_uint

    global ISteamClient_SetWarningMessageHook
    ISteamClient_SetWarningMessageHook = dll.SteamAPI_ISteamClient_SetWarningMessageHook
    ISteamClient_SetWarningMessageHook.argtypes = [ POINTER(ISteamClient), c_void_p ]
    ISteamClient_SetWarningMessageHook.restype = None

    global ISteamClient_BShutdownIfAllPipesClosed
    ISteamClient_BShutdownIfAllPipesClosed = dll.SteamAPI_ISteamClient_BShutdownIfAllPipesClosed
    ISteamClient_BShutdownIfAllPipesClosed.argtypes = [ POINTER(ISteamClient),  ]
    ISteamClient_BShutdownIfAllPipesClosed.restype = c_bool

    global ISteamClient_GetISteamHTTP
    ISteamClient_GetISteamHTTP = dll.SteamAPI_ISteamClient_GetISteamHTTP
    ISteamClient_GetISteamHTTP.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamHTTP.restype = POINTER(ISteamHTTP)

    global ISteamClient_GetISteamController
    ISteamClient_GetISteamController = dll.SteamAPI_ISteamClient_GetISteamController
    ISteamClient_GetISteamController.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamController.restype = POINTER(ISteamController)

    global ISteamClient_GetISteamUGC
    ISteamClient_GetISteamUGC = dll.SteamAPI_ISteamClient_GetISteamUGC
    ISteamClient_GetISteamUGC.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamUGC.restype = POINTER(ISteamUGC)

    global ISteamClient_GetISteamAppList
    ISteamClient_GetISteamAppList = dll.SteamAPI_ISteamClient_GetISteamAppList
    ISteamClient_GetISteamAppList.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamAppList.restype = POINTER(ISteamAppList)

    global ISteamClient_GetISteamMusic
    ISteamClient_GetISteamMusic = dll.SteamAPI_ISteamClient_GetISteamMusic
    ISteamClient_GetISteamMusic.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamMusic.restype = POINTER(ISteamMusic)

    global ISteamClient_GetISteamMusicRemote
    ISteamClient_GetISteamMusicRemote = dll.SteamAPI_ISteamClient_GetISteamMusicRemote
    ISteamClient_GetISteamMusicRemote.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamMusicRemote.restype = POINTER(ISteamMusicRemote)

    global ISteamClient_GetISteamHTMLSurface
    ISteamClient_GetISteamHTMLSurface = dll.SteamAPI_ISteamClient_GetISteamHTMLSurface
    ISteamClient_GetISteamHTMLSurface.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamHTMLSurface.restype = POINTER(ISteamHTMLSurface)

    global ISteamClient_GetISteamInventory
    ISteamClient_GetISteamInventory = dll.SteamAPI_ISteamClient_GetISteamInventory
    ISteamClient_GetISteamInventory.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamInventory.restype = POINTER(ISteamInventory)

    global ISteamClient_GetISteamVideo
    ISteamClient_GetISteamVideo = dll.SteamAPI_ISteamClient_GetISteamVideo
    ISteamClient_GetISteamVideo.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamVideo.restype = POINTER(ISteamVideo)

    global ISteamClient_GetISteamParentalSettings
    ISteamClient_GetISteamParentalSettings = dll.SteamAPI_ISteamClient_GetISteamParentalSettings
    ISteamClient_GetISteamParentalSettings.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamParentalSettings.restype = POINTER(ISteamParentalSettings)

    global ISteamClient_GetISteamInput
    ISteamClient_GetISteamInput = dll.SteamAPI_ISteamClient_GetISteamInput
    ISteamClient_GetISteamInput.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamInput.restype = POINTER(ISteamInput)

    global ISteamClient_GetISteamParties
    ISteamClient_GetISteamParties = dll.SteamAPI_ISteamClient_GetISteamParties
    ISteamClient_GetISteamParties.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamParties.restype = POINTER(ISteamParties)

    global ISteamClient_GetISteamRemotePlay
    ISteamClient_GetISteamRemotePlay = dll.SteamAPI_ISteamClient_GetISteamRemotePlay
    ISteamClient_GetISteamRemotePlay.argtypes = [ POINTER(ISteamClient), c_int, c_int, c_char_p ]
    ISteamClient_GetISteamRemotePlay.restype = POINTER(ISteamRemotePlay)

    global ISteamUser_GetHSteamUser
    ISteamUser_GetHSteamUser = dll.SteamAPI_ISteamUser_GetHSteamUser
    ISteamUser_GetHSteamUser.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetHSteamUser.restype = c_int

    global ISteamUser_BLoggedOn
    ISteamUser_BLoggedOn = dll.SteamAPI_ISteamUser_BLoggedOn
    ISteamUser_BLoggedOn.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BLoggedOn.restype = c_bool

    global ISteamUser_GetSteamID
    ISteamUser_GetSteamID = dll.SteamAPI_ISteamUser_GetSteamID
    ISteamUser_GetSteamID.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetSteamID.restype = c_ulonglong

    global ISteamUser_InitiateGameConnection_DEPRECATED
    ISteamUser_InitiateGameConnection_DEPRECATED = dll.SteamAPI_ISteamUser_InitiateGameConnection_DEPRECATED
    ISteamUser_InitiateGameConnection_DEPRECATED.argtypes = [ POINTER(ISteamUser), c_void_p, c_int, c_ulonglong, c_uint, c_ushort, c_bool ]
    ISteamUser_InitiateGameConnection_DEPRECATED.restype = c_int

    global ISteamUser_TerminateGameConnection_DEPRECATED
    ISteamUser_TerminateGameConnection_DEPRECATED = dll.SteamAPI_ISteamUser_TerminateGameConnection_DEPRECATED
    ISteamUser_TerminateGameConnection_DEPRECATED.argtypes = [ POINTER(ISteamUser), c_uint, c_ushort ]
    ISteamUser_TerminateGameConnection_DEPRECATED.restype = None

    global ISteamUser_TrackAppUsageEvent
    ISteamUser_TrackAppUsageEvent = dll.SteamAPI_ISteamUser_TrackAppUsageEvent
    ISteamUser_TrackAppUsageEvent.argtypes = [ POINTER(ISteamUser), c_ulonglong, c_int, c_char_p ]
    ISteamUser_TrackAppUsageEvent.restype = None

    global ISteamUser_GetUserDataFolder
    ISteamUser_GetUserDataFolder = dll.SteamAPI_ISteamUser_GetUserDataFolder
    ISteamUser_GetUserDataFolder.argtypes = [ POINTER(ISteamUser), c_char_p, c_int ]
    ISteamUser_GetUserDataFolder.restype = c_bool

    global ISteamUser_StartVoiceRecording
    ISteamUser_StartVoiceRecording = dll.SteamAPI_ISteamUser_StartVoiceRecording
    ISteamUser_StartVoiceRecording.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_StartVoiceRecording.restype = None

    global ISteamUser_StopVoiceRecording
    ISteamUser_StopVoiceRecording = dll.SteamAPI_ISteamUser_StopVoiceRecording
    ISteamUser_StopVoiceRecording.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_StopVoiceRecording.restype = None

    global ISteamUser_GetAvailableVoice
    ISteamUser_GetAvailableVoice = dll.SteamAPI_ISteamUser_GetAvailableVoice
    ISteamUser_GetAvailableVoice.argtypes = [ POINTER(ISteamUser), POINTER(c_uint), POINTER(c_uint), c_uint ]
    ISteamUser_GetAvailableVoice.restype = EVoiceResult

    global ISteamUser_GetVoice
    ISteamUser_GetVoice = dll.SteamAPI_ISteamUser_GetVoice
    ISteamUser_GetVoice.argtypes = [ POINTER(ISteamUser), c_bool, c_void_p, c_uint, POINTER(c_uint), c_bool, c_void_p, c_uint, POINTER(c_uint), c_uint ]
    ISteamUser_GetVoice.restype = EVoiceResult

    global ISteamUser_DecompressVoice
    ISteamUser_DecompressVoice = dll.SteamAPI_ISteamUser_DecompressVoice
    ISteamUser_DecompressVoice.argtypes = [ POINTER(ISteamUser), c_void_p, c_uint, c_void_p, c_uint, POINTER(c_uint), c_uint ]
    ISteamUser_DecompressVoice.restype = EVoiceResult

    global ISteamUser_GetVoiceOptimalSampleRate
    ISteamUser_GetVoiceOptimalSampleRate = dll.SteamAPI_ISteamUser_GetVoiceOptimalSampleRate
    ISteamUser_GetVoiceOptimalSampleRate.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetVoiceOptimalSampleRate.restype = c_uint

    global ISteamUser_GetAuthSessionTicket
    ISteamUser_GetAuthSessionTicket = dll.SteamAPI_ISteamUser_GetAuthSessionTicket
    ISteamUser_GetAuthSessionTicket.argtypes = [ POINTER(ISteamUser), c_void_p, c_int, POINTER(c_uint) ]
    ISteamUser_GetAuthSessionTicket.restype = c_uint

    global ISteamUser_BeginAuthSession
    ISteamUser_BeginAuthSession = dll.SteamAPI_ISteamUser_BeginAuthSession
    ISteamUser_BeginAuthSession.argtypes = [ POINTER(ISteamUser), c_void_p, c_int, c_ulonglong ]
    ISteamUser_BeginAuthSession.restype = EBeginAuthSessionResult

    global ISteamUser_EndAuthSession
    ISteamUser_EndAuthSession = dll.SteamAPI_ISteamUser_EndAuthSession
    ISteamUser_EndAuthSession.argtypes = [ POINTER(ISteamUser), c_ulonglong ]
    ISteamUser_EndAuthSession.restype = None

    global ISteamUser_CancelAuthTicket
    ISteamUser_CancelAuthTicket = dll.SteamAPI_ISteamUser_CancelAuthTicket
    ISteamUser_CancelAuthTicket.argtypes = [ POINTER(ISteamUser), c_uint ]
    ISteamUser_CancelAuthTicket.restype = None

    global ISteamUser_UserHasLicenseForApp
    ISteamUser_UserHasLicenseForApp = dll.SteamAPI_ISteamUser_UserHasLicenseForApp
    ISteamUser_UserHasLicenseForApp.argtypes = [ POINTER(ISteamUser), c_ulonglong, c_uint ]
    ISteamUser_UserHasLicenseForApp.restype = EUserHasLicenseForAppResult

    global ISteamUser_BIsBehindNAT
    ISteamUser_BIsBehindNAT = dll.SteamAPI_ISteamUser_BIsBehindNAT
    ISteamUser_BIsBehindNAT.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BIsBehindNAT.restype = c_bool

    global ISteamUser_AdvertiseGame
    ISteamUser_AdvertiseGame = dll.SteamAPI_ISteamUser_AdvertiseGame
    ISteamUser_AdvertiseGame.argtypes = [ POINTER(ISteamUser), c_ulonglong, c_uint, c_ushort ]
    ISteamUser_AdvertiseGame.restype = None

    global ISteamUser_RequestEncryptedAppTicket
    ISteamUser_RequestEncryptedAppTicket = dll.SteamAPI_ISteamUser_RequestEncryptedAppTicket
    ISteamUser_RequestEncryptedAppTicket.argtypes = [ POINTER(ISteamUser), c_void_p, c_int ]
    ISteamUser_RequestEncryptedAppTicket.restype = c_ulonglong

    global ISteamUser_GetEncryptedAppTicket
    ISteamUser_GetEncryptedAppTicket = dll.SteamAPI_ISteamUser_GetEncryptedAppTicket
    ISteamUser_GetEncryptedAppTicket.argtypes = [ POINTER(ISteamUser), c_void_p, c_int, POINTER(c_uint) ]
    ISteamUser_GetEncryptedAppTicket.restype = c_bool

    global ISteamUser_GetGameBadgeLevel
    ISteamUser_GetGameBadgeLevel = dll.SteamAPI_ISteamUser_GetGameBadgeLevel
    ISteamUser_GetGameBadgeLevel.argtypes = [ POINTER(ISteamUser), c_int, c_bool ]
    ISteamUser_GetGameBadgeLevel.restype = c_int

    global ISteamUser_GetPlayerSteamLevel
    ISteamUser_GetPlayerSteamLevel = dll.SteamAPI_ISteamUser_GetPlayerSteamLevel
    ISteamUser_GetPlayerSteamLevel.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetPlayerSteamLevel.restype = c_int

    global ISteamUser_RequestStoreAuthURL
    ISteamUser_RequestStoreAuthURL = dll.SteamAPI_ISteamUser_RequestStoreAuthURL
    ISteamUser_RequestStoreAuthURL.argtypes = [ POINTER(ISteamUser), c_char_p ]
    ISteamUser_RequestStoreAuthURL.restype = c_ulonglong

    global ISteamUser_BIsPhoneVerified
    ISteamUser_BIsPhoneVerified = dll.SteamAPI_ISteamUser_BIsPhoneVerified
    ISteamUser_BIsPhoneVerified.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BIsPhoneVerified.restype = c_bool

    global ISteamUser_BIsTwoFactorEnabled
    ISteamUser_BIsTwoFactorEnabled = dll.SteamAPI_ISteamUser_BIsTwoFactorEnabled
    ISteamUser_BIsTwoFactorEnabled.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BIsTwoFactorEnabled.restype = c_bool

    global ISteamUser_BIsPhoneIdentifying
    ISteamUser_BIsPhoneIdentifying = dll.SteamAPI_ISteamUser_BIsPhoneIdentifying
    ISteamUser_BIsPhoneIdentifying.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BIsPhoneIdentifying.restype = c_bool

    global ISteamUser_BIsPhoneRequiringVerification
    ISteamUser_BIsPhoneRequiringVerification = dll.SteamAPI_ISteamUser_BIsPhoneRequiringVerification
    ISteamUser_BIsPhoneRequiringVerification.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_BIsPhoneRequiringVerification.restype = c_bool

    global ISteamUser_GetMarketEligibility
    ISteamUser_GetMarketEligibility = dll.SteamAPI_ISteamUser_GetMarketEligibility
    ISteamUser_GetMarketEligibility.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetMarketEligibility.restype = c_ulonglong

    global ISteamUser_GetDurationControl
    ISteamUser_GetDurationControl = dll.SteamAPI_ISteamUser_GetDurationControl
    ISteamUser_GetDurationControl.argtypes = [ POINTER(ISteamUser),  ]
    ISteamUser_GetDurationControl.restype = c_ulonglong

    global ISteamUser_BSetDurationControlOnlineState
    ISteamUser_BSetDurationControlOnlineState = dll.SteamAPI_ISteamUser_BSetDurationControlOnlineState
    ISteamUser_BSetDurationControlOnlineState.argtypes = [ POINTER(ISteamUser), EDurationControlOnlineState ]
    ISteamUser_BSetDurationControlOnlineState.restype = c_bool

    global SteamUser_v021
    SteamUser_v021 = dll.SteamAPI_SteamUser_v021
    SteamUser_v021.argtypes = [ ]
    SteamUser_v021.restype = POINTER(ISteamUser)

    global ISteamFriends_GetPersonaName
    ISteamFriends_GetPersonaName = dll.SteamAPI_ISteamFriends_GetPersonaName
    ISteamFriends_GetPersonaName.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetPersonaName.restype = c_char_p

    global ISteamFriends_SetPersonaName
    ISteamFriends_SetPersonaName = dll.SteamAPI_ISteamFriends_SetPersonaName
    ISteamFriends_SetPersonaName.argtypes = [ POINTER(ISteamFriends), c_char_p ]
    ISteamFriends_SetPersonaName.restype = c_ulonglong

    global ISteamFriends_GetPersonaState
    ISteamFriends_GetPersonaState = dll.SteamAPI_ISteamFriends_GetPersonaState
    ISteamFriends_GetPersonaState.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetPersonaState.restype = EPersonaState

    global ISteamFriends_GetFriendCount
    ISteamFriends_GetFriendCount = dll.SteamAPI_ISteamFriends_GetFriendCount
    ISteamFriends_GetFriendCount.argtypes = [ POINTER(ISteamFriends), c_int ]
    ISteamFriends_GetFriendCount.restype = c_int

    global ISteamFriends_GetFriendByIndex
    ISteamFriends_GetFriendByIndex = dll.SteamAPI_ISteamFriends_GetFriendByIndex
    ISteamFriends_GetFriendByIndex.argtypes = [ POINTER(ISteamFriends), c_int, c_int ]
    ISteamFriends_GetFriendByIndex.restype = c_ulonglong

    global ISteamFriends_GetFriendRelationship
    ISteamFriends_GetFriendRelationship = dll.SteamAPI_ISteamFriends_GetFriendRelationship
    ISteamFriends_GetFriendRelationship.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendRelationship.restype = EFriendRelationship

    global ISteamFriends_GetFriendPersonaState
    ISteamFriends_GetFriendPersonaState = dll.SteamAPI_ISteamFriends_GetFriendPersonaState
    ISteamFriends_GetFriendPersonaState.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendPersonaState.restype = EPersonaState

    global ISteamFriends_GetFriendPersonaName
    ISteamFriends_GetFriendPersonaName = dll.SteamAPI_ISteamFriends_GetFriendPersonaName
    ISteamFriends_GetFriendPersonaName.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendPersonaName.restype = c_char_p

    global ISteamFriends_GetFriendGamePlayed
    ISteamFriends_GetFriendGamePlayed = dll.SteamAPI_ISteamFriends_GetFriendGamePlayed
    ISteamFriends_GetFriendGamePlayed.argtypes = [ POINTER(ISteamFriends), c_ulonglong, POINTER(FriendGameInfo_t) ]
    ISteamFriends_GetFriendGamePlayed.restype = c_bool

    global ISteamFriends_GetFriendPersonaNameHistory
    ISteamFriends_GetFriendPersonaNameHistory = dll.SteamAPI_ISteamFriends_GetFriendPersonaNameHistory
    ISteamFriends_GetFriendPersonaNameHistory.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_GetFriendPersonaNameHistory.restype = c_char_p

    global ISteamFriends_GetFriendSteamLevel
    ISteamFriends_GetFriendSteamLevel = dll.SteamAPI_ISteamFriends_GetFriendSteamLevel
    ISteamFriends_GetFriendSteamLevel.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendSteamLevel.restype = c_int

    global ISteamFriends_GetPlayerNickname
    ISteamFriends_GetPlayerNickname = dll.SteamAPI_ISteamFriends_GetPlayerNickname
    ISteamFriends_GetPlayerNickname.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetPlayerNickname.restype = c_char_p

    global ISteamFriends_GetFriendsGroupCount
    ISteamFriends_GetFriendsGroupCount = dll.SteamAPI_ISteamFriends_GetFriendsGroupCount
    ISteamFriends_GetFriendsGroupCount.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetFriendsGroupCount.restype = c_int

    global ISteamFriends_GetFriendsGroupIDByIndex
    ISteamFriends_GetFriendsGroupIDByIndex = dll.SteamAPI_ISteamFriends_GetFriendsGroupIDByIndex
    ISteamFriends_GetFriendsGroupIDByIndex.argtypes = [ POINTER(ISteamFriends), c_int ]
    ISteamFriends_GetFriendsGroupIDByIndex.restype = c_short

    global ISteamFriends_GetFriendsGroupName
    ISteamFriends_GetFriendsGroupName = dll.SteamAPI_ISteamFriends_GetFriendsGroupName
    ISteamFriends_GetFriendsGroupName.argtypes = [ POINTER(ISteamFriends), c_short ]
    ISteamFriends_GetFriendsGroupName.restype = c_char_p

    global ISteamFriends_GetFriendsGroupMembersCount
    ISteamFriends_GetFriendsGroupMembersCount = dll.SteamAPI_ISteamFriends_GetFriendsGroupMembersCount
    ISteamFriends_GetFriendsGroupMembersCount.argtypes = [ POINTER(ISteamFriends), c_short ]
    ISteamFriends_GetFriendsGroupMembersCount.restype = c_int

    global ISteamFriends_GetFriendsGroupMembersList
    ISteamFriends_GetFriendsGroupMembersList = dll.SteamAPI_ISteamFriends_GetFriendsGroupMembersList
    ISteamFriends_GetFriendsGroupMembersList.argtypes = [ POINTER(ISteamFriends), c_short, POINTER(c_ulonglong), c_int ]
    ISteamFriends_GetFriendsGroupMembersList.restype = None

    global ISteamFriends_HasFriend
    ISteamFriends_HasFriend = dll.SteamAPI_ISteamFriends_HasFriend
    ISteamFriends_HasFriend.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_HasFriend.restype = c_bool

    global ISteamFriends_GetClanCount
    ISteamFriends_GetClanCount = dll.SteamAPI_ISteamFriends_GetClanCount
    ISteamFriends_GetClanCount.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetClanCount.restype = c_int

    global ISteamFriends_GetClanByIndex
    ISteamFriends_GetClanByIndex = dll.SteamAPI_ISteamFriends_GetClanByIndex
    ISteamFriends_GetClanByIndex.argtypes = [ POINTER(ISteamFriends), c_int ]
    ISteamFriends_GetClanByIndex.restype = c_ulonglong

    global ISteamFriends_GetClanName
    ISteamFriends_GetClanName = dll.SteamAPI_ISteamFriends_GetClanName
    ISteamFriends_GetClanName.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetClanName.restype = c_char_p

    global ISteamFriends_GetClanTag
    ISteamFriends_GetClanTag = dll.SteamAPI_ISteamFriends_GetClanTag
    ISteamFriends_GetClanTag.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetClanTag.restype = c_char_p

    global ISteamFriends_GetClanActivityCounts
    ISteamFriends_GetClanActivityCounts = dll.SteamAPI_ISteamFriends_GetClanActivityCounts
    ISteamFriends_GetClanActivityCounts.argtypes = [ POINTER(ISteamFriends), c_ulonglong, POINTER(c_int), POINTER(c_int), POINTER(c_int) ]
    ISteamFriends_GetClanActivityCounts.restype = c_bool

    global ISteamFriends_DownloadClanActivityCounts
    ISteamFriends_DownloadClanActivityCounts = dll.SteamAPI_ISteamFriends_DownloadClanActivityCounts
    ISteamFriends_DownloadClanActivityCounts.argtypes = [ POINTER(ISteamFriends), POINTER(c_ulonglong), c_int ]
    ISteamFriends_DownloadClanActivityCounts.restype = c_ulonglong

    global ISteamFriends_GetFriendCountFromSource
    ISteamFriends_GetFriendCountFromSource = dll.SteamAPI_ISteamFriends_GetFriendCountFromSource
    ISteamFriends_GetFriendCountFromSource.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendCountFromSource.restype = c_int

    global ISteamFriends_GetFriendFromSourceByIndex
    ISteamFriends_GetFriendFromSourceByIndex = dll.SteamAPI_ISteamFriends_GetFriendFromSourceByIndex
    ISteamFriends_GetFriendFromSourceByIndex.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_GetFriendFromSourceByIndex.restype = c_ulonglong

    global ISteamFriends_IsUserInSource
    ISteamFriends_IsUserInSource = dll.SteamAPI_ISteamFriends_IsUserInSource
    ISteamFriends_IsUserInSource.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_ulonglong ]
    ISteamFriends_IsUserInSource.restype = c_bool

    global ISteamFriends_SetInGameVoiceSpeaking
    ISteamFriends_SetInGameVoiceSpeaking = dll.SteamAPI_ISteamFriends_SetInGameVoiceSpeaking
    ISteamFriends_SetInGameVoiceSpeaking.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_bool ]
    ISteamFriends_SetInGameVoiceSpeaking.restype = None

    global ISteamFriends_ActivateGameOverlay
    ISteamFriends_ActivateGameOverlay = dll.SteamAPI_ISteamFriends_ActivateGameOverlay
    ISteamFriends_ActivateGameOverlay.argtypes = [ POINTER(ISteamFriends), c_char_p ]
    ISteamFriends_ActivateGameOverlay.restype = None

    global ISteamFriends_ActivateGameOverlayToUser
    ISteamFriends_ActivateGameOverlayToUser = dll.SteamAPI_ISteamFriends_ActivateGameOverlayToUser
    ISteamFriends_ActivateGameOverlayToUser.argtypes = [ POINTER(ISteamFriends), c_char_p, c_ulonglong ]
    ISteamFriends_ActivateGameOverlayToUser.restype = None

    global ISteamFriends_ActivateGameOverlayToWebPage
    ISteamFriends_ActivateGameOverlayToWebPage = dll.SteamAPI_ISteamFriends_ActivateGameOverlayToWebPage
    ISteamFriends_ActivateGameOverlayToWebPage.argtypes = [ POINTER(ISteamFriends), c_char_p, EActivateGameOverlayToWebPageMode ]
    ISteamFriends_ActivateGameOverlayToWebPage.restype = None

    global ISteamFriends_ActivateGameOverlayToStore
    ISteamFriends_ActivateGameOverlayToStore = dll.SteamAPI_ISteamFriends_ActivateGameOverlayToStore
    ISteamFriends_ActivateGameOverlayToStore.argtypes = [ POINTER(ISteamFriends), c_uint, EOverlayToStoreFlag ]
    ISteamFriends_ActivateGameOverlayToStore.restype = None

    global ISteamFriends_SetPlayedWith
    ISteamFriends_SetPlayedWith = dll.SteamAPI_ISteamFriends_SetPlayedWith
    ISteamFriends_SetPlayedWith.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_SetPlayedWith.restype = None

    global ISteamFriends_ActivateGameOverlayInviteDialog
    ISteamFriends_ActivateGameOverlayInviteDialog = dll.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialog
    ISteamFriends_ActivateGameOverlayInviteDialog.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_ActivateGameOverlayInviteDialog.restype = None

    global ISteamFriends_GetSmallFriendAvatar
    ISteamFriends_GetSmallFriendAvatar = dll.SteamAPI_ISteamFriends_GetSmallFriendAvatar
    ISteamFriends_GetSmallFriendAvatar.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetSmallFriendAvatar.restype = c_int

    global ISteamFriends_GetMediumFriendAvatar
    ISteamFriends_GetMediumFriendAvatar = dll.SteamAPI_ISteamFriends_GetMediumFriendAvatar
    ISteamFriends_GetMediumFriendAvatar.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetMediumFriendAvatar.restype = c_int

    global ISteamFriends_GetLargeFriendAvatar
    ISteamFriends_GetLargeFriendAvatar = dll.SteamAPI_ISteamFriends_GetLargeFriendAvatar
    ISteamFriends_GetLargeFriendAvatar.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetLargeFriendAvatar.restype = c_int

    global ISteamFriends_RequestUserInformation
    ISteamFriends_RequestUserInformation = dll.SteamAPI_ISteamFriends_RequestUserInformation
    ISteamFriends_RequestUserInformation.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_bool ]
    ISteamFriends_RequestUserInformation.restype = c_bool

    global ISteamFriends_RequestClanOfficerList
    ISteamFriends_RequestClanOfficerList = dll.SteamAPI_ISteamFriends_RequestClanOfficerList
    ISteamFriends_RequestClanOfficerList.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_RequestClanOfficerList.restype = c_ulonglong

    global ISteamFriends_GetClanOwner
    ISteamFriends_GetClanOwner = dll.SteamAPI_ISteamFriends_GetClanOwner
    ISteamFriends_GetClanOwner.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetClanOwner.restype = c_ulonglong

    global ISteamFriends_GetClanOfficerCount
    ISteamFriends_GetClanOfficerCount = dll.SteamAPI_ISteamFriends_GetClanOfficerCount
    ISteamFriends_GetClanOfficerCount.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetClanOfficerCount.restype = c_int

    global ISteamFriends_GetClanOfficerByIndex
    ISteamFriends_GetClanOfficerByIndex = dll.SteamAPI_ISteamFriends_GetClanOfficerByIndex
    ISteamFriends_GetClanOfficerByIndex.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_GetClanOfficerByIndex.restype = c_ulonglong

    global ISteamFriends_GetUserRestrictions
    ISteamFriends_GetUserRestrictions = dll.SteamAPI_ISteamFriends_GetUserRestrictions
    ISteamFriends_GetUserRestrictions.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetUserRestrictions.restype = c_uint

    global ISteamFriends_SetRichPresence
    ISteamFriends_SetRichPresence = dll.SteamAPI_ISteamFriends_SetRichPresence
    ISteamFriends_SetRichPresence.argtypes = [ POINTER(ISteamFriends), c_char_p, c_char_p ]
    ISteamFriends_SetRichPresence.restype = c_bool

    global ISteamFriends_ClearRichPresence
    ISteamFriends_ClearRichPresence = dll.SteamAPI_ISteamFriends_ClearRichPresence
    ISteamFriends_ClearRichPresence.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_ClearRichPresence.restype = None

    global ISteamFriends_GetFriendRichPresence
    ISteamFriends_GetFriendRichPresence = dll.SteamAPI_ISteamFriends_GetFriendRichPresence
    ISteamFriends_GetFriendRichPresence.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_char_p ]
    ISteamFriends_GetFriendRichPresence.restype = c_char_p

    global ISteamFriends_GetFriendRichPresenceKeyCount
    ISteamFriends_GetFriendRichPresenceKeyCount = dll.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyCount
    ISteamFriends_GetFriendRichPresenceKeyCount.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendRichPresenceKeyCount.restype = c_int

    global ISteamFriends_GetFriendRichPresenceKeyByIndex
    ISteamFriends_GetFriendRichPresenceKeyByIndex = dll.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyByIndex
    ISteamFriends_GetFriendRichPresenceKeyByIndex.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_GetFriendRichPresenceKeyByIndex.restype = c_char_p

    global ISteamFriends_RequestFriendRichPresence
    ISteamFriends_RequestFriendRichPresence = dll.SteamAPI_ISteamFriends_RequestFriendRichPresence
    ISteamFriends_RequestFriendRichPresence.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_RequestFriendRichPresence.restype = None

    global ISteamFriends_InviteUserToGame
    ISteamFriends_InviteUserToGame = dll.SteamAPI_ISteamFriends_InviteUserToGame
    ISteamFriends_InviteUserToGame.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_char_p ]
    ISteamFriends_InviteUserToGame.restype = c_bool

    global ISteamFriends_GetCoplayFriendCount
    ISteamFriends_GetCoplayFriendCount = dll.SteamAPI_ISteamFriends_GetCoplayFriendCount
    ISteamFriends_GetCoplayFriendCount.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetCoplayFriendCount.restype = c_int

    global ISteamFriends_GetCoplayFriend
    ISteamFriends_GetCoplayFriend = dll.SteamAPI_ISteamFriends_GetCoplayFriend
    ISteamFriends_GetCoplayFriend.argtypes = [ POINTER(ISteamFriends), c_int ]
    ISteamFriends_GetCoplayFriend.restype = c_ulonglong

    global ISteamFriends_GetFriendCoplayTime
    ISteamFriends_GetFriendCoplayTime = dll.SteamAPI_ISteamFriends_GetFriendCoplayTime
    ISteamFriends_GetFriendCoplayTime.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendCoplayTime.restype = c_int

    global ISteamFriends_GetFriendCoplayGame
    ISteamFriends_GetFriendCoplayGame = dll.SteamAPI_ISteamFriends_GetFriendCoplayGame
    ISteamFriends_GetFriendCoplayGame.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFriendCoplayGame.restype = c_uint

    global ISteamFriends_JoinClanChatRoom
    ISteamFriends_JoinClanChatRoom = dll.SteamAPI_ISteamFriends_JoinClanChatRoom
    ISteamFriends_JoinClanChatRoom.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_JoinClanChatRoom.restype = c_ulonglong

    global ISteamFriends_LeaveClanChatRoom
    ISteamFriends_LeaveClanChatRoom = dll.SteamAPI_ISteamFriends_LeaveClanChatRoom
    ISteamFriends_LeaveClanChatRoom.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_LeaveClanChatRoom.restype = c_bool

    global ISteamFriends_GetClanChatMemberCount
    ISteamFriends_GetClanChatMemberCount = dll.SteamAPI_ISteamFriends_GetClanChatMemberCount
    ISteamFriends_GetClanChatMemberCount.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetClanChatMemberCount.restype = c_int

    global ISteamFriends_GetChatMemberByIndex
    ISteamFriends_GetChatMemberByIndex = dll.SteamAPI_ISteamFriends_GetChatMemberByIndex
    ISteamFriends_GetChatMemberByIndex.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int ]
    ISteamFriends_GetChatMemberByIndex.restype = c_ulonglong

    global ISteamFriends_SendClanChatMessage
    ISteamFriends_SendClanChatMessage = dll.SteamAPI_ISteamFriends_SendClanChatMessage
    ISteamFriends_SendClanChatMessage.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_char_p ]
    ISteamFriends_SendClanChatMessage.restype = c_bool

    global ISteamFriends_GetClanChatMessage
    ISteamFriends_GetClanChatMessage = dll.SteamAPI_ISteamFriends_GetClanChatMessage
    ISteamFriends_GetClanChatMessage.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int, c_void_p, c_int, POINTER(EChatEntryType), POINTER(c_ulonglong) ]
    ISteamFriends_GetClanChatMessage.restype = c_int

    global ISteamFriends_IsClanChatAdmin
    ISteamFriends_IsClanChatAdmin = dll.SteamAPI_ISteamFriends_IsClanChatAdmin
    ISteamFriends_IsClanChatAdmin.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_ulonglong ]
    ISteamFriends_IsClanChatAdmin.restype = c_bool

    global ISteamFriends_IsClanChatWindowOpenInSteam
    ISteamFriends_IsClanChatWindowOpenInSteam = dll.SteamAPI_ISteamFriends_IsClanChatWindowOpenInSteam
    ISteamFriends_IsClanChatWindowOpenInSteam.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_IsClanChatWindowOpenInSteam.restype = c_bool

    global ISteamFriends_OpenClanChatWindowInSteam
    ISteamFriends_OpenClanChatWindowInSteam = dll.SteamAPI_ISteamFriends_OpenClanChatWindowInSteam
    ISteamFriends_OpenClanChatWindowInSteam.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_OpenClanChatWindowInSteam.restype = c_bool

    global ISteamFriends_CloseClanChatWindowInSteam
    ISteamFriends_CloseClanChatWindowInSteam = dll.SteamAPI_ISteamFriends_CloseClanChatWindowInSteam
    ISteamFriends_CloseClanChatWindowInSteam.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_CloseClanChatWindowInSteam.restype = c_bool

    global ISteamFriends_SetListenForFriendsMessages
    ISteamFriends_SetListenForFriendsMessages = dll.SteamAPI_ISteamFriends_SetListenForFriendsMessages
    ISteamFriends_SetListenForFriendsMessages.argtypes = [ POINTER(ISteamFriends), c_bool ]
    ISteamFriends_SetListenForFriendsMessages.restype = c_bool

    global ISteamFriends_ReplyToFriendMessage
    ISteamFriends_ReplyToFriendMessage = dll.SteamAPI_ISteamFriends_ReplyToFriendMessage
    ISteamFriends_ReplyToFriendMessage.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_char_p ]
    ISteamFriends_ReplyToFriendMessage.restype = c_bool

    global ISteamFriends_GetFriendMessage
    ISteamFriends_GetFriendMessage = dll.SteamAPI_ISteamFriends_GetFriendMessage
    ISteamFriends_GetFriendMessage.argtypes = [ POINTER(ISteamFriends), c_ulonglong, c_int, c_void_p, c_int, POINTER(EChatEntryType) ]
    ISteamFriends_GetFriendMessage.restype = c_int

    global ISteamFriends_GetFollowerCount
    ISteamFriends_GetFollowerCount = dll.SteamAPI_ISteamFriends_GetFollowerCount
    ISteamFriends_GetFollowerCount.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_GetFollowerCount.restype = c_ulonglong

    global ISteamFriends_IsFollowing
    ISteamFriends_IsFollowing = dll.SteamAPI_ISteamFriends_IsFollowing
    ISteamFriends_IsFollowing.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_IsFollowing.restype = c_ulonglong

    global ISteamFriends_EnumerateFollowingList
    ISteamFriends_EnumerateFollowingList = dll.SteamAPI_ISteamFriends_EnumerateFollowingList
    ISteamFriends_EnumerateFollowingList.argtypes = [ POINTER(ISteamFriends), c_uint ]
    ISteamFriends_EnumerateFollowingList.restype = c_ulonglong

    global ISteamFriends_IsClanPublic
    ISteamFriends_IsClanPublic = dll.SteamAPI_ISteamFriends_IsClanPublic
    ISteamFriends_IsClanPublic.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_IsClanPublic.restype = c_bool

    global ISteamFriends_IsClanOfficialGameGroup
    ISteamFriends_IsClanOfficialGameGroup = dll.SteamAPI_ISteamFriends_IsClanOfficialGameGroup
    ISteamFriends_IsClanOfficialGameGroup.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_IsClanOfficialGameGroup.restype = c_bool

    global ISteamFriends_GetNumChatsWithUnreadPriorityMessages
    ISteamFriends_GetNumChatsWithUnreadPriorityMessages = dll.SteamAPI_ISteamFriends_GetNumChatsWithUnreadPriorityMessages
    ISteamFriends_GetNumChatsWithUnreadPriorityMessages.argtypes = [ POINTER(ISteamFriends),  ]
    ISteamFriends_GetNumChatsWithUnreadPriorityMessages.restype = c_int

    global ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog
    ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog = dll.SteamAPI_ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog
    ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog.argtypes = [ POINTER(ISteamFriends), c_ulonglong ]
    ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog.restype = None

    global ISteamFriends_RegisterProtocolInOverlayBrowser
    ISteamFriends_RegisterProtocolInOverlayBrowser = dll.SteamAPI_ISteamFriends_RegisterProtocolInOverlayBrowser
    ISteamFriends_RegisterProtocolInOverlayBrowser.argtypes = [ POINTER(ISteamFriends), c_char_p ]
    ISteamFriends_RegisterProtocolInOverlayBrowser.restype = c_bool

    global ISteamFriends_ActivateGameOverlayInviteDialogConnectString
    ISteamFriends_ActivateGameOverlayInviteDialogConnectString = dll.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialogConnectString
    ISteamFriends_ActivateGameOverlayInviteDialogConnectString.argtypes = [ POINTER(ISteamFriends), c_char_p ]
    ISteamFriends_ActivateGameOverlayInviteDialogConnectString.restype = None

    global SteamFriends_v017
    SteamFriends_v017 = dll.SteamAPI_SteamFriends_v017
    SteamFriends_v017.argtypes = [ ]
    SteamFriends_v017.restype = POINTER(ISteamFriends)

    global ISteamUtils_GetSecondsSinceAppActive
    ISteamUtils_GetSecondsSinceAppActive = dll.SteamAPI_ISteamUtils_GetSecondsSinceAppActive
    ISteamUtils_GetSecondsSinceAppActive.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetSecondsSinceAppActive.restype = c_uint

    global ISteamUtils_GetSecondsSinceComputerActive
    ISteamUtils_GetSecondsSinceComputerActive = dll.SteamAPI_ISteamUtils_GetSecondsSinceComputerActive
    ISteamUtils_GetSecondsSinceComputerActive.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetSecondsSinceComputerActive.restype = c_uint

    global ISteamUtils_GetConnectedUniverse
    ISteamUtils_GetConnectedUniverse = dll.SteamAPI_ISteamUtils_GetConnectedUniverse
    ISteamUtils_GetConnectedUniverse.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetConnectedUniverse.restype = EUniverse

    global ISteamUtils_GetServerRealTime
    ISteamUtils_GetServerRealTime = dll.SteamAPI_ISteamUtils_GetServerRealTime
    ISteamUtils_GetServerRealTime.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetServerRealTime.restype = c_uint

    global ISteamUtils_GetIPCountry
    ISteamUtils_GetIPCountry = dll.SteamAPI_ISteamUtils_GetIPCountry
    ISteamUtils_GetIPCountry.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetIPCountry.restype = c_char_p

    global ISteamUtils_GetImageSize
    ISteamUtils_GetImageSize = dll.SteamAPI_ISteamUtils_GetImageSize
    ISteamUtils_GetImageSize.argtypes = [ POINTER(ISteamUtils), c_int, POINTER(c_uint), POINTER(c_uint) ]
    ISteamUtils_GetImageSize.restype = c_bool

    global ISteamUtils_GetImageRGBA
    ISteamUtils_GetImageRGBA = dll.SteamAPI_ISteamUtils_GetImageRGBA
    ISteamUtils_GetImageRGBA.argtypes = [ POINTER(ISteamUtils), c_int, POINTER(c_ubyte), c_int ]
    ISteamUtils_GetImageRGBA.restype = c_bool

    global ISteamUtils_GetCurrentBatteryPower
    ISteamUtils_GetCurrentBatteryPower = dll.SteamAPI_ISteamUtils_GetCurrentBatteryPower
    ISteamUtils_GetCurrentBatteryPower.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetCurrentBatteryPower.restype = c_ubyte

    global ISteamUtils_GetAppID
    ISteamUtils_GetAppID = dll.SteamAPI_ISteamUtils_GetAppID
    ISteamUtils_GetAppID.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetAppID.restype = c_uint

    global ISteamUtils_SetOverlayNotificationPosition
    ISteamUtils_SetOverlayNotificationPosition = dll.SteamAPI_ISteamUtils_SetOverlayNotificationPosition
    ISteamUtils_SetOverlayNotificationPosition.argtypes = [ POINTER(ISteamUtils), ENotificationPosition ]
    ISteamUtils_SetOverlayNotificationPosition.restype = None

    global ISteamUtils_IsAPICallCompleted
    ISteamUtils_IsAPICallCompleted = dll.SteamAPI_ISteamUtils_IsAPICallCompleted
    ISteamUtils_IsAPICallCompleted.argtypes = [ POINTER(ISteamUtils), c_ulonglong, POINTER(c_bool) ]
    ISteamUtils_IsAPICallCompleted.restype = c_bool

    global ISteamUtils_GetAPICallFailureReason
    ISteamUtils_GetAPICallFailureReason = dll.SteamAPI_ISteamUtils_GetAPICallFailureReason
    ISteamUtils_GetAPICallFailureReason.argtypes = [ POINTER(ISteamUtils), c_ulonglong ]
    ISteamUtils_GetAPICallFailureReason.restype = ESteamAPICallFailure

    global ISteamUtils_GetAPICallResult
    ISteamUtils_GetAPICallResult = dll.SteamAPI_ISteamUtils_GetAPICallResult
    ISteamUtils_GetAPICallResult.argtypes = [ POINTER(ISteamUtils), c_ulonglong, c_void_p, c_int, c_int, POINTER(c_bool) ]
    ISteamUtils_GetAPICallResult.restype = c_bool

    global ISteamUtils_GetIPCCallCount
    ISteamUtils_GetIPCCallCount = dll.SteamAPI_ISteamUtils_GetIPCCallCount
    ISteamUtils_GetIPCCallCount.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetIPCCallCount.restype = c_uint

    global ISteamUtils_SetWarningMessageHook
    ISteamUtils_SetWarningMessageHook = dll.SteamAPI_ISteamUtils_SetWarningMessageHook
    ISteamUtils_SetWarningMessageHook.argtypes = [ POINTER(ISteamUtils), c_void_p ]
    ISteamUtils_SetWarningMessageHook.restype = None

    global ISteamUtils_IsOverlayEnabled
    ISteamUtils_IsOverlayEnabled = dll.SteamAPI_ISteamUtils_IsOverlayEnabled
    ISteamUtils_IsOverlayEnabled.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsOverlayEnabled.restype = c_bool

    global ISteamUtils_BOverlayNeedsPresent
    ISteamUtils_BOverlayNeedsPresent = dll.SteamAPI_ISteamUtils_BOverlayNeedsPresent
    ISteamUtils_BOverlayNeedsPresent.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_BOverlayNeedsPresent.restype = c_bool

    global ISteamUtils_CheckFileSignature
    ISteamUtils_CheckFileSignature = dll.SteamAPI_ISteamUtils_CheckFileSignature
    ISteamUtils_CheckFileSignature.argtypes = [ POINTER(ISteamUtils), c_char_p ]
    ISteamUtils_CheckFileSignature.restype = c_ulonglong

    global ISteamUtils_ShowGamepadTextInput
    ISteamUtils_ShowGamepadTextInput = dll.SteamAPI_ISteamUtils_ShowGamepadTextInput
    ISteamUtils_ShowGamepadTextInput.argtypes = [ POINTER(ISteamUtils), EGamepadTextInputMode, EGamepadTextInputLineMode, c_char_p, c_uint, c_char_p ]
    ISteamUtils_ShowGamepadTextInput.restype = c_bool

    global ISteamUtils_GetEnteredGamepadTextLength
    ISteamUtils_GetEnteredGamepadTextLength = dll.SteamAPI_ISteamUtils_GetEnteredGamepadTextLength
    ISteamUtils_GetEnteredGamepadTextLength.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetEnteredGamepadTextLength.restype = c_uint

    global ISteamUtils_GetEnteredGamepadTextInput
    ISteamUtils_GetEnteredGamepadTextInput = dll.SteamAPI_ISteamUtils_GetEnteredGamepadTextInput
    ISteamUtils_GetEnteredGamepadTextInput.argtypes = [ POINTER(ISteamUtils), c_char_p, c_uint ]
    ISteamUtils_GetEnteredGamepadTextInput.restype = c_bool

    global ISteamUtils_GetSteamUILanguage
    ISteamUtils_GetSteamUILanguage = dll.SteamAPI_ISteamUtils_GetSteamUILanguage
    ISteamUtils_GetSteamUILanguage.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_GetSteamUILanguage.restype = c_char_p

    global ISteamUtils_IsSteamRunningInVR
    ISteamUtils_IsSteamRunningInVR = dll.SteamAPI_ISteamUtils_IsSteamRunningInVR
    ISteamUtils_IsSteamRunningInVR.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsSteamRunningInVR.restype = c_bool

    global ISteamUtils_SetOverlayNotificationInset
    ISteamUtils_SetOverlayNotificationInset = dll.SteamAPI_ISteamUtils_SetOverlayNotificationInset
    ISteamUtils_SetOverlayNotificationInset.argtypes = [ POINTER(ISteamUtils), c_int, c_int ]
    ISteamUtils_SetOverlayNotificationInset.restype = None

    global ISteamUtils_IsSteamInBigPictureMode
    ISteamUtils_IsSteamInBigPictureMode = dll.SteamAPI_ISteamUtils_IsSteamInBigPictureMode
    ISteamUtils_IsSteamInBigPictureMode.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsSteamInBigPictureMode.restype = c_bool

    global ISteamUtils_StartVRDashboard
    ISteamUtils_StartVRDashboard = dll.SteamAPI_ISteamUtils_StartVRDashboard
    ISteamUtils_StartVRDashboard.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_StartVRDashboard.restype = None

    global ISteamUtils_IsVRHeadsetStreamingEnabled
    ISteamUtils_IsVRHeadsetStreamingEnabled = dll.SteamAPI_ISteamUtils_IsVRHeadsetStreamingEnabled
    ISteamUtils_IsVRHeadsetStreamingEnabled.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsVRHeadsetStreamingEnabled.restype = c_bool

    global ISteamUtils_SetVRHeadsetStreamingEnabled
    ISteamUtils_SetVRHeadsetStreamingEnabled = dll.SteamAPI_ISteamUtils_SetVRHeadsetStreamingEnabled
    ISteamUtils_SetVRHeadsetStreamingEnabled.argtypes = [ POINTER(ISteamUtils), c_bool ]
    ISteamUtils_SetVRHeadsetStreamingEnabled.restype = None

    global ISteamUtils_IsSteamChinaLauncher
    ISteamUtils_IsSteamChinaLauncher = dll.SteamAPI_ISteamUtils_IsSteamChinaLauncher
    ISteamUtils_IsSteamChinaLauncher.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsSteamChinaLauncher.restype = c_bool

    global ISteamUtils_InitFilterText
    ISteamUtils_InitFilterText = dll.SteamAPI_ISteamUtils_InitFilterText
    ISteamUtils_InitFilterText.argtypes = [ POINTER(ISteamUtils), c_uint ]
    ISteamUtils_InitFilterText.restype = c_bool

    global ISteamUtils_FilterText
    ISteamUtils_FilterText = dll.SteamAPI_ISteamUtils_FilterText
    ISteamUtils_FilterText.argtypes = [ POINTER(ISteamUtils), ETextFilteringContext, c_ulonglong, c_char_p, c_char_p, c_uint ]
    ISteamUtils_FilterText.restype = c_int

    global ISteamUtils_GetIPv6ConnectivityState
    ISteamUtils_GetIPv6ConnectivityState = dll.SteamAPI_ISteamUtils_GetIPv6ConnectivityState
    ISteamUtils_GetIPv6ConnectivityState.argtypes = [ POINTER(ISteamUtils), ESteamIPv6ConnectivityProtocol ]
    ISteamUtils_GetIPv6ConnectivityState.restype = ESteamIPv6ConnectivityState

    global ISteamUtils_IsSteamRunningOnSteamDeck
    ISteamUtils_IsSteamRunningOnSteamDeck = dll.SteamAPI_ISteamUtils_IsSteamRunningOnSteamDeck
    ISteamUtils_IsSteamRunningOnSteamDeck.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_IsSteamRunningOnSteamDeck.restype = c_bool

    global ISteamUtils_ShowFloatingGamepadTextInput
    ISteamUtils_ShowFloatingGamepadTextInput = dll.SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput
    ISteamUtils_ShowFloatingGamepadTextInput.argtypes = [ POINTER(ISteamUtils), EFloatingGamepadTextInputMode, c_int, c_int, c_int, c_int ]
    ISteamUtils_ShowFloatingGamepadTextInput.restype = c_bool

    global ISteamUtils_SetGameLauncherMode
    ISteamUtils_SetGameLauncherMode = dll.SteamAPI_ISteamUtils_SetGameLauncherMode
    ISteamUtils_SetGameLauncherMode.argtypes = [ POINTER(ISteamUtils), c_bool ]
    ISteamUtils_SetGameLauncherMode.restype = None

    global ISteamUtils_DismissFloatingGamepadTextInput
    ISteamUtils_DismissFloatingGamepadTextInput = dll.SteamAPI_ISteamUtils_DismissFloatingGamepadTextInput
    ISteamUtils_DismissFloatingGamepadTextInput.argtypes = [ POINTER(ISteamUtils),  ]
    ISteamUtils_DismissFloatingGamepadTextInput.restype = c_bool

    global SteamUtils_v010
    SteamUtils_v010 = dll.SteamAPI_SteamUtils_v010
    SteamUtils_v010.argtypes = [ ]
    SteamUtils_v010.restype = POINTER(ISteamUtils)

    global SteamGameServerUtils_v010
    SteamGameServerUtils_v010 = dll.SteamAPI_SteamGameServerUtils_v010
    SteamGameServerUtils_v010.argtypes = [ ]
    SteamGameServerUtils_v010.restype = POINTER(ISteamUtils)

    global ISteamMatchmaking_GetFavoriteGameCount
    ISteamMatchmaking_GetFavoriteGameCount = dll.SteamAPI_ISteamMatchmaking_GetFavoriteGameCount
    ISteamMatchmaking_GetFavoriteGameCount.argtypes = [ POINTER(ISteamMatchmaking),  ]
    ISteamMatchmaking_GetFavoriteGameCount.restype = c_int

    global ISteamMatchmaking_GetFavoriteGame
    ISteamMatchmaking_GetFavoriteGame = dll.SteamAPI_ISteamMatchmaking_GetFavoriteGame
    ISteamMatchmaking_GetFavoriteGame.argtypes = [ POINTER(ISteamMatchmaking), c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_ushort), POINTER(c_ushort), POINTER(c_uint), POINTER(c_uint) ]
    ISteamMatchmaking_GetFavoriteGame.restype = c_bool

    global ISteamMatchmaking_AddFavoriteGame
    ISteamMatchmaking_AddFavoriteGame = dll.SteamAPI_ISteamMatchmaking_AddFavoriteGame
    ISteamMatchmaking_AddFavoriteGame.argtypes = [ POINTER(ISteamMatchmaking), c_uint, c_uint, c_ushort, c_ushort, c_uint, c_uint ]
    ISteamMatchmaking_AddFavoriteGame.restype = c_int

    global ISteamMatchmaking_RemoveFavoriteGame
    ISteamMatchmaking_RemoveFavoriteGame = dll.SteamAPI_ISteamMatchmaking_RemoveFavoriteGame
    ISteamMatchmaking_RemoveFavoriteGame.argtypes = [ POINTER(ISteamMatchmaking), c_uint, c_uint, c_ushort, c_ushort, c_uint ]
    ISteamMatchmaking_RemoveFavoriteGame.restype = c_bool

    global ISteamMatchmaking_RequestLobbyList
    ISteamMatchmaking_RequestLobbyList = dll.SteamAPI_ISteamMatchmaking_RequestLobbyList
    ISteamMatchmaking_RequestLobbyList.argtypes = [ POINTER(ISteamMatchmaking),  ]
    ISteamMatchmaking_RequestLobbyList.restype = c_ulonglong

    global ISteamMatchmaking_AddRequestLobbyListStringFilter
    ISteamMatchmaking_AddRequestLobbyListStringFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListStringFilter
    ISteamMatchmaking_AddRequestLobbyListStringFilter.argtypes = [ POINTER(ISteamMatchmaking), c_char_p, c_char_p, ELobbyComparison ]
    ISteamMatchmaking_AddRequestLobbyListStringFilter.restype = None

    global ISteamMatchmaking_AddRequestLobbyListNumericalFilter
    ISteamMatchmaking_AddRequestLobbyListNumericalFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNumericalFilter
    ISteamMatchmaking_AddRequestLobbyListNumericalFilter.argtypes = [ POINTER(ISteamMatchmaking), c_char_p, c_int, ELobbyComparison ]
    ISteamMatchmaking_AddRequestLobbyListNumericalFilter.restype = None

    global ISteamMatchmaking_AddRequestLobbyListNearValueFilter
    ISteamMatchmaking_AddRequestLobbyListNearValueFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNearValueFilter
    ISteamMatchmaking_AddRequestLobbyListNearValueFilter.argtypes = [ POINTER(ISteamMatchmaking), c_char_p, c_int ]
    ISteamMatchmaking_AddRequestLobbyListNearValueFilter.restype = None

    global ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable
    ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable
    ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable.argtypes = [ POINTER(ISteamMatchmaking), c_int ]
    ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable.restype = None

    global ISteamMatchmaking_AddRequestLobbyListDistanceFilter
    ISteamMatchmaking_AddRequestLobbyListDistanceFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListDistanceFilter
    ISteamMatchmaking_AddRequestLobbyListDistanceFilter.argtypes = [ POINTER(ISteamMatchmaking), ELobbyDistanceFilter ]
    ISteamMatchmaking_AddRequestLobbyListDistanceFilter.restype = None

    global ISteamMatchmaking_AddRequestLobbyListResultCountFilter
    ISteamMatchmaking_AddRequestLobbyListResultCountFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListResultCountFilter
    ISteamMatchmaking_AddRequestLobbyListResultCountFilter.argtypes = [ POINTER(ISteamMatchmaking), c_int ]
    ISteamMatchmaking_AddRequestLobbyListResultCountFilter.restype = None

    global ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter
    ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter = dll.SteamAPI_ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter
    ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter.restype = None

    global ISteamMatchmaking_GetLobbyByIndex
    ISteamMatchmaking_GetLobbyByIndex = dll.SteamAPI_ISteamMatchmaking_GetLobbyByIndex
    ISteamMatchmaking_GetLobbyByIndex.argtypes = [ POINTER(ISteamMatchmaking), c_int ]
    ISteamMatchmaking_GetLobbyByIndex.restype = c_ulonglong

    global ISteamMatchmaking_CreateLobby
    ISteamMatchmaking_CreateLobby = dll.SteamAPI_ISteamMatchmaking_CreateLobby
    ISteamMatchmaking_CreateLobby.argtypes = [ POINTER(ISteamMatchmaking), ELobbyType, c_int ]
    ISteamMatchmaking_CreateLobby.restype = c_ulonglong

    global ISteamMatchmaking_JoinLobby
    ISteamMatchmaking_JoinLobby = dll.SteamAPI_ISteamMatchmaking_JoinLobby
    ISteamMatchmaking_JoinLobby.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_JoinLobby.restype = c_ulonglong

    global ISteamMatchmaking_LeaveLobby
    ISteamMatchmaking_LeaveLobby = dll.SteamAPI_ISteamMatchmaking_LeaveLobby
    ISteamMatchmaking_LeaveLobby.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_LeaveLobby.restype = None

    global ISteamMatchmaking_InviteUserToLobby
    ISteamMatchmaking_InviteUserToLobby = dll.SteamAPI_ISteamMatchmaking_InviteUserToLobby
    ISteamMatchmaking_InviteUserToLobby.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_ulonglong ]
    ISteamMatchmaking_InviteUserToLobby.restype = c_bool

    global ISteamMatchmaking_GetNumLobbyMembers
    ISteamMatchmaking_GetNumLobbyMembers = dll.SteamAPI_ISteamMatchmaking_GetNumLobbyMembers
    ISteamMatchmaking_GetNumLobbyMembers.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_GetNumLobbyMembers.restype = c_int

    global ISteamMatchmaking_GetLobbyMemberByIndex
    ISteamMatchmaking_GetLobbyMemberByIndex = dll.SteamAPI_ISteamMatchmaking_GetLobbyMemberByIndex
    ISteamMatchmaking_GetLobbyMemberByIndex.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_int ]
    ISteamMatchmaking_GetLobbyMemberByIndex.restype = c_ulonglong

    global ISteamMatchmaking_GetLobbyData
    ISteamMatchmaking_GetLobbyData = dll.SteamAPI_ISteamMatchmaking_GetLobbyData
    ISteamMatchmaking_GetLobbyData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_char_p ]
    ISteamMatchmaking_GetLobbyData.restype = c_char_p

    global ISteamMatchmaking_SetLobbyData
    ISteamMatchmaking_SetLobbyData = dll.SteamAPI_ISteamMatchmaking_SetLobbyData
    ISteamMatchmaking_SetLobbyData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_char_p, c_char_p ]
    ISteamMatchmaking_SetLobbyData.restype = c_bool

    global ISteamMatchmaking_GetLobbyDataCount
    ISteamMatchmaking_GetLobbyDataCount = dll.SteamAPI_ISteamMatchmaking_GetLobbyDataCount
    ISteamMatchmaking_GetLobbyDataCount.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_GetLobbyDataCount.restype = c_int

    global ISteamMatchmaking_GetLobbyDataByIndex
    ISteamMatchmaking_GetLobbyDataByIndex = dll.SteamAPI_ISteamMatchmaking_GetLobbyDataByIndex
    ISteamMatchmaking_GetLobbyDataByIndex.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_int, c_char_p, c_int, c_char_p, c_int ]
    ISteamMatchmaking_GetLobbyDataByIndex.restype = c_bool

    global ISteamMatchmaking_DeleteLobbyData
    ISteamMatchmaking_DeleteLobbyData = dll.SteamAPI_ISteamMatchmaking_DeleteLobbyData
    ISteamMatchmaking_DeleteLobbyData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_char_p ]
    ISteamMatchmaking_DeleteLobbyData.restype = c_bool

    global ISteamMatchmaking_GetLobbyMemberData
    ISteamMatchmaking_GetLobbyMemberData = dll.SteamAPI_ISteamMatchmaking_GetLobbyMemberData
    ISteamMatchmaking_GetLobbyMemberData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_ulonglong, c_char_p ]
    ISteamMatchmaking_GetLobbyMemberData.restype = c_char_p

    global ISteamMatchmaking_SetLobbyMemberData
    ISteamMatchmaking_SetLobbyMemberData = dll.SteamAPI_ISteamMatchmaking_SetLobbyMemberData
    ISteamMatchmaking_SetLobbyMemberData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_char_p, c_char_p ]
    ISteamMatchmaking_SetLobbyMemberData.restype = None

    global ISteamMatchmaking_SendLobbyChatMsg
    ISteamMatchmaking_SendLobbyChatMsg = dll.SteamAPI_ISteamMatchmaking_SendLobbyChatMsg
    ISteamMatchmaking_SendLobbyChatMsg.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_void_p, c_int ]
    ISteamMatchmaking_SendLobbyChatMsg.restype = c_bool

    global ISteamMatchmaking_GetLobbyChatEntry
    ISteamMatchmaking_GetLobbyChatEntry = dll.SteamAPI_ISteamMatchmaking_GetLobbyChatEntry
    ISteamMatchmaking_GetLobbyChatEntry.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_int, POINTER(c_ulonglong), c_void_p, c_int, POINTER(EChatEntryType) ]
    ISteamMatchmaking_GetLobbyChatEntry.restype = c_int

    global ISteamMatchmaking_RequestLobbyData
    ISteamMatchmaking_RequestLobbyData = dll.SteamAPI_ISteamMatchmaking_RequestLobbyData
    ISteamMatchmaking_RequestLobbyData.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_RequestLobbyData.restype = c_bool

    global ISteamMatchmaking_SetLobbyGameServer
    ISteamMatchmaking_SetLobbyGameServer = dll.SteamAPI_ISteamMatchmaking_SetLobbyGameServer
    ISteamMatchmaking_SetLobbyGameServer.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_uint, c_ushort, c_ulonglong ]
    ISteamMatchmaking_SetLobbyGameServer.restype = None

    global ISteamMatchmaking_GetLobbyGameServer
    ISteamMatchmaking_GetLobbyGameServer = dll.SteamAPI_ISteamMatchmaking_GetLobbyGameServer
    ISteamMatchmaking_GetLobbyGameServer.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, POINTER(c_uint), POINTER(c_ushort), POINTER(c_ulonglong) ]
    ISteamMatchmaking_GetLobbyGameServer.restype = c_bool

    global ISteamMatchmaking_SetLobbyMemberLimit
    ISteamMatchmaking_SetLobbyMemberLimit = dll.SteamAPI_ISteamMatchmaking_SetLobbyMemberLimit
    ISteamMatchmaking_SetLobbyMemberLimit.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_int ]
    ISteamMatchmaking_SetLobbyMemberLimit.restype = c_bool

    global ISteamMatchmaking_GetLobbyMemberLimit
    ISteamMatchmaking_GetLobbyMemberLimit = dll.SteamAPI_ISteamMatchmaking_GetLobbyMemberLimit
    ISteamMatchmaking_GetLobbyMemberLimit.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_GetLobbyMemberLimit.restype = c_int

    global ISteamMatchmaking_SetLobbyType
    ISteamMatchmaking_SetLobbyType = dll.SteamAPI_ISteamMatchmaking_SetLobbyType
    ISteamMatchmaking_SetLobbyType.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, ELobbyType ]
    ISteamMatchmaking_SetLobbyType.restype = c_bool

    global ISteamMatchmaking_SetLobbyJoinable
    ISteamMatchmaking_SetLobbyJoinable = dll.SteamAPI_ISteamMatchmaking_SetLobbyJoinable
    ISteamMatchmaking_SetLobbyJoinable.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_bool ]
    ISteamMatchmaking_SetLobbyJoinable.restype = c_bool

    global ISteamMatchmaking_GetLobbyOwner
    ISteamMatchmaking_GetLobbyOwner = dll.SteamAPI_ISteamMatchmaking_GetLobbyOwner
    ISteamMatchmaking_GetLobbyOwner.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong ]
    ISteamMatchmaking_GetLobbyOwner.restype = c_ulonglong

    global ISteamMatchmaking_SetLobbyOwner
    ISteamMatchmaking_SetLobbyOwner = dll.SteamAPI_ISteamMatchmaking_SetLobbyOwner
    ISteamMatchmaking_SetLobbyOwner.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_ulonglong ]
    ISteamMatchmaking_SetLobbyOwner.restype = c_bool

    global ISteamMatchmaking_SetLinkedLobby
    ISteamMatchmaking_SetLinkedLobby = dll.SteamAPI_ISteamMatchmaking_SetLinkedLobby
    ISteamMatchmaking_SetLinkedLobby.argtypes = [ POINTER(ISteamMatchmaking), c_ulonglong, c_ulonglong ]
    ISteamMatchmaking_SetLinkedLobby.restype = c_bool

    global SteamMatchmaking_v009
    SteamMatchmaking_v009 = dll.SteamAPI_SteamMatchmaking_v009
    SteamMatchmaking_v009.argtypes = [ ]
    SteamMatchmaking_v009.restype = POINTER(ISteamMatchmaking)

    global ISteamMatchmakingServerListResponse_ServerResponded
    ISteamMatchmakingServerListResponse_ServerResponded = dll.SteamAPI_ISteamMatchmakingServerListResponse_ServerResponded
    ISteamMatchmakingServerListResponse_ServerResponded.argtypes = [ POINTER(ISteamMatchmakingServerListResponse), c_void_p, c_int ]
    ISteamMatchmakingServerListResponse_ServerResponded.restype = None

    global ISteamMatchmakingServerListResponse_ServerFailedToRespond
    ISteamMatchmakingServerListResponse_ServerFailedToRespond = dll.SteamAPI_ISteamMatchmakingServerListResponse_ServerFailedToRespond
    ISteamMatchmakingServerListResponse_ServerFailedToRespond.argtypes = [ POINTER(ISteamMatchmakingServerListResponse), c_void_p, c_int ]
    ISteamMatchmakingServerListResponse_ServerFailedToRespond.restype = None

    global ISteamMatchmakingServerListResponse_RefreshComplete
    ISteamMatchmakingServerListResponse_RefreshComplete = dll.SteamAPI_ISteamMatchmakingServerListResponse_RefreshComplete
    ISteamMatchmakingServerListResponse_RefreshComplete.argtypes = [ POINTER(ISteamMatchmakingServerListResponse), c_void_p, EMatchMakingServerResponse ]
    ISteamMatchmakingServerListResponse_RefreshComplete.restype = None

    global ISteamMatchmakingPingResponse_ServerResponded
    ISteamMatchmakingPingResponse_ServerResponded = dll.SteamAPI_ISteamMatchmakingPingResponse_ServerResponded
    ISteamMatchmakingPingResponse_ServerResponded.argtypes = [ POINTER(ISteamMatchmakingPingResponse), POINTER(gameserveritem_t) ]
    ISteamMatchmakingPingResponse_ServerResponded.restype = None

    global ISteamMatchmakingPingResponse_ServerFailedToRespond
    ISteamMatchmakingPingResponse_ServerFailedToRespond = dll.SteamAPI_ISteamMatchmakingPingResponse_ServerFailedToRespond
    ISteamMatchmakingPingResponse_ServerFailedToRespond.argtypes = [ POINTER(ISteamMatchmakingPingResponse),  ]
    ISteamMatchmakingPingResponse_ServerFailedToRespond.restype = None

    global ISteamMatchmakingPlayersResponse_AddPlayerToList
    ISteamMatchmakingPlayersResponse_AddPlayerToList = dll.SteamAPI_ISteamMatchmakingPlayersResponse_AddPlayerToList
    ISteamMatchmakingPlayersResponse_AddPlayerToList.argtypes = [ POINTER(ISteamMatchmakingPlayersResponse), c_char_p, c_int, c_float ]
    ISteamMatchmakingPlayersResponse_AddPlayerToList.restype = None

    global ISteamMatchmakingPlayersResponse_PlayersFailedToRespond
    ISteamMatchmakingPlayersResponse_PlayersFailedToRespond = dll.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersFailedToRespond
    ISteamMatchmakingPlayersResponse_PlayersFailedToRespond.argtypes = [ POINTER(ISteamMatchmakingPlayersResponse),  ]
    ISteamMatchmakingPlayersResponse_PlayersFailedToRespond.restype = None

    global ISteamMatchmakingPlayersResponse_PlayersRefreshComplete
    ISteamMatchmakingPlayersResponse_PlayersRefreshComplete = dll.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersRefreshComplete
    ISteamMatchmakingPlayersResponse_PlayersRefreshComplete.argtypes = [ POINTER(ISteamMatchmakingPlayersResponse),  ]
    ISteamMatchmakingPlayersResponse_PlayersRefreshComplete.restype = None

    global ISteamMatchmakingRulesResponse_RulesResponded
    ISteamMatchmakingRulesResponse_RulesResponded = dll.SteamAPI_ISteamMatchmakingRulesResponse_RulesResponded
    ISteamMatchmakingRulesResponse_RulesResponded.argtypes = [ POINTER(ISteamMatchmakingRulesResponse), c_char_p, c_char_p ]
    ISteamMatchmakingRulesResponse_RulesResponded.restype = None

    global ISteamMatchmakingRulesResponse_RulesFailedToRespond
    ISteamMatchmakingRulesResponse_RulesFailedToRespond = dll.SteamAPI_ISteamMatchmakingRulesResponse_RulesFailedToRespond
    ISteamMatchmakingRulesResponse_RulesFailedToRespond.argtypes = [ POINTER(ISteamMatchmakingRulesResponse),  ]
    ISteamMatchmakingRulesResponse_RulesFailedToRespond.restype = None

    global ISteamMatchmakingRulesResponse_RulesRefreshComplete
    ISteamMatchmakingRulesResponse_RulesRefreshComplete = dll.SteamAPI_ISteamMatchmakingRulesResponse_RulesRefreshComplete
    ISteamMatchmakingRulesResponse_RulesRefreshComplete.argtypes = [ POINTER(ISteamMatchmakingRulesResponse),  ]
    ISteamMatchmakingRulesResponse_RulesRefreshComplete.restype = None

    global ISteamMatchmakingServers_RequestInternetServerList
    ISteamMatchmakingServers_RequestInternetServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestInternetServerList
    ISteamMatchmakingServers_RequestInternetServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(POINTER(MatchMakingKeyValuePair_t)), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestInternetServerList.restype = c_void_p

    global ISteamMatchmakingServers_RequestLANServerList
    ISteamMatchmakingServers_RequestLANServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestLANServerList
    ISteamMatchmakingServers_RequestLANServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestLANServerList.restype = c_void_p

    global ISteamMatchmakingServers_RequestFriendsServerList
    ISteamMatchmakingServers_RequestFriendsServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestFriendsServerList
    ISteamMatchmakingServers_RequestFriendsServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(POINTER(MatchMakingKeyValuePair_t)), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestFriendsServerList.restype = c_void_p

    global ISteamMatchmakingServers_RequestFavoritesServerList
    ISteamMatchmakingServers_RequestFavoritesServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestFavoritesServerList
    ISteamMatchmakingServers_RequestFavoritesServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(POINTER(MatchMakingKeyValuePair_t)), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestFavoritesServerList.restype = c_void_p

    global ISteamMatchmakingServers_RequestHistoryServerList
    ISteamMatchmakingServers_RequestHistoryServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestHistoryServerList
    ISteamMatchmakingServers_RequestHistoryServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(POINTER(MatchMakingKeyValuePair_t)), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestHistoryServerList.restype = c_void_p

    global ISteamMatchmakingServers_RequestSpectatorServerList
    ISteamMatchmakingServers_RequestSpectatorServerList = dll.SteamAPI_ISteamMatchmakingServers_RequestSpectatorServerList
    ISteamMatchmakingServers_RequestSpectatorServerList.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, POINTER(POINTER(MatchMakingKeyValuePair_t)), c_uint, POINTER(ISteamMatchmakingServerListResponse) ]
    ISteamMatchmakingServers_RequestSpectatorServerList.restype = c_void_p

    global ISteamMatchmakingServers_ReleaseRequest
    ISteamMatchmakingServers_ReleaseRequest = dll.SteamAPI_ISteamMatchmakingServers_ReleaseRequest
    ISteamMatchmakingServers_ReleaseRequest.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p ]
    ISteamMatchmakingServers_ReleaseRequest.restype = None

    global ISteamMatchmakingServers_GetServerDetails
    ISteamMatchmakingServers_GetServerDetails = dll.SteamAPI_ISteamMatchmakingServers_GetServerDetails
    ISteamMatchmakingServers_GetServerDetails.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p, c_int ]
    ISteamMatchmakingServers_GetServerDetails.restype = POINTER(gameserveritem_t)

    global ISteamMatchmakingServers_CancelQuery
    ISteamMatchmakingServers_CancelQuery = dll.SteamAPI_ISteamMatchmakingServers_CancelQuery
    ISteamMatchmakingServers_CancelQuery.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p ]
    ISteamMatchmakingServers_CancelQuery.restype = None

    global ISteamMatchmakingServers_RefreshQuery
    ISteamMatchmakingServers_RefreshQuery = dll.SteamAPI_ISteamMatchmakingServers_RefreshQuery
    ISteamMatchmakingServers_RefreshQuery.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p ]
    ISteamMatchmakingServers_RefreshQuery.restype = None

    global ISteamMatchmakingServers_IsRefreshing
    ISteamMatchmakingServers_IsRefreshing = dll.SteamAPI_ISteamMatchmakingServers_IsRefreshing
    ISteamMatchmakingServers_IsRefreshing.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p ]
    ISteamMatchmakingServers_IsRefreshing.restype = c_bool

    global ISteamMatchmakingServers_GetServerCount
    ISteamMatchmakingServers_GetServerCount = dll.SteamAPI_ISteamMatchmakingServers_GetServerCount
    ISteamMatchmakingServers_GetServerCount.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p ]
    ISteamMatchmakingServers_GetServerCount.restype = c_int

    global ISteamMatchmakingServers_RefreshServer
    ISteamMatchmakingServers_RefreshServer = dll.SteamAPI_ISteamMatchmakingServers_RefreshServer
    ISteamMatchmakingServers_RefreshServer.argtypes = [ POINTER(ISteamMatchmakingServers), c_void_p, c_int ]
    ISteamMatchmakingServers_RefreshServer.restype = None

    global ISteamMatchmakingServers_PingServer
    ISteamMatchmakingServers_PingServer = dll.SteamAPI_ISteamMatchmakingServers_PingServer
    ISteamMatchmakingServers_PingServer.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, c_ushort, POINTER(ISteamMatchmakingPingResponse) ]
    ISteamMatchmakingServers_PingServer.restype = c_int

    global ISteamMatchmakingServers_PlayerDetails
    ISteamMatchmakingServers_PlayerDetails = dll.SteamAPI_ISteamMatchmakingServers_PlayerDetails
    ISteamMatchmakingServers_PlayerDetails.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, c_ushort, POINTER(ISteamMatchmakingPlayersResponse) ]
    ISteamMatchmakingServers_PlayerDetails.restype = c_int

    global ISteamMatchmakingServers_ServerRules
    ISteamMatchmakingServers_ServerRules = dll.SteamAPI_ISteamMatchmakingServers_ServerRules
    ISteamMatchmakingServers_ServerRules.argtypes = [ POINTER(ISteamMatchmakingServers), c_uint, c_ushort, POINTER(ISteamMatchmakingRulesResponse) ]
    ISteamMatchmakingServers_ServerRules.restype = c_int

    global ISteamMatchmakingServers_CancelServerQuery
    ISteamMatchmakingServers_CancelServerQuery = dll.SteamAPI_ISteamMatchmakingServers_CancelServerQuery
    ISteamMatchmakingServers_CancelServerQuery.argtypes = [ POINTER(ISteamMatchmakingServers), c_int ]
    ISteamMatchmakingServers_CancelServerQuery.restype = None

    global SteamMatchmakingServers_v002
    SteamMatchmakingServers_v002 = dll.SteamAPI_SteamMatchmakingServers_v002
    SteamMatchmakingServers_v002.argtypes = [ ]
    SteamMatchmakingServers_v002.restype = POINTER(ISteamMatchmakingServers)

    global ISteamGameSearch_AddGameSearchParams
    ISteamGameSearch_AddGameSearchParams = dll.SteamAPI_ISteamGameSearch_AddGameSearchParams
    ISteamGameSearch_AddGameSearchParams.argtypes = [ POINTER(ISteamGameSearch), c_char_p, c_char_p ]
    ISteamGameSearch_AddGameSearchParams.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_SearchForGameWithLobby
    ISteamGameSearch_SearchForGameWithLobby = dll.SteamAPI_ISteamGameSearch_SearchForGameWithLobby
    ISteamGameSearch_SearchForGameWithLobby.argtypes = [ POINTER(ISteamGameSearch), c_ulonglong, c_int, c_int ]
    ISteamGameSearch_SearchForGameWithLobby.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_SearchForGameSolo
    ISteamGameSearch_SearchForGameSolo = dll.SteamAPI_ISteamGameSearch_SearchForGameSolo
    ISteamGameSearch_SearchForGameSolo.argtypes = [ POINTER(ISteamGameSearch), c_int, c_int ]
    ISteamGameSearch_SearchForGameSolo.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_AcceptGame
    ISteamGameSearch_AcceptGame = dll.SteamAPI_ISteamGameSearch_AcceptGame
    ISteamGameSearch_AcceptGame.argtypes = [ POINTER(ISteamGameSearch),  ]
    ISteamGameSearch_AcceptGame.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_DeclineGame
    ISteamGameSearch_DeclineGame = dll.SteamAPI_ISteamGameSearch_DeclineGame
    ISteamGameSearch_DeclineGame.argtypes = [ POINTER(ISteamGameSearch),  ]
    ISteamGameSearch_DeclineGame.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_RetrieveConnectionDetails
    ISteamGameSearch_RetrieveConnectionDetails = dll.SteamAPI_ISteamGameSearch_RetrieveConnectionDetails
    ISteamGameSearch_RetrieveConnectionDetails.argtypes = [ POINTER(ISteamGameSearch), c_ulonglong, c_char_p, c_int ]
    ISteamGameSearch_RetrieveConnectionDetails.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_EndGameSearch
    ISteamGameSearch_EndGameSearch = dll.SteamAPI_ISteamGameSearch_EndGameSearch
    ISteamGameSearch_EndGameSearch.argtypes = [ POINTER(ISteamGameSearch),  ]
    ISteamGameSearch_EndGameSearch.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_SetGameHostParams
    ISteamGameSearch_SetGameHostParams = dll.SteamAPI_ISteamGameSearch_SetGameHostParams
    ISteamGameSearch_SetGameHostParams.argtypes = [ POINTER(ISteamGameSearch), c_char_p, c_char_p ]
    ISteamGameSearch_SetGameHostParams.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_SetConnectionDetails
    ISteamGameSearch_SetConnectionDetails = dll.SteamAPI_ISteamGameSearch_SetConnectionDetails
    ISteamGameSearch_SetConnectionDetails.argtypes = [ POINTER(ISteamGameSearch), c_char_p, c_int ]
    ISteamGameSearch_SetConnectionDetails.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_RequestPlayersForGame
    ISteamGameSearch_RequestPlayersForGame = dll.SteamAPI_ISteamGameSearch_RequestPlayersForGame
    ISteamGameSearch_RequestPlayersForGame.argtypes = [ POINTER(ISteamGameSearch), c_int, c_int, c_int ]
    ISteamGameSearch_RequestPlayersForGame.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_HostConfirmGameStart
    ISteamGameSearch_HostConfirmGameStart = dll.SteamAPI_ISteamGameSearch_HostConfirmGameStart
    ISteamGameSearch_HostConfirmGameStart.argtypes = [ POINTER(ISteamGameSearch), c_ulonglong ]
    ISteamGameSearch_HostConfirmGameStart.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_CancelRequestPlayersForGame
    ISteamGameSearch_CancelRequestPlayersForGame = dll.SteamAPI_ISteamGameSearch_CancelRequestPlayersForGame
    ISteamGameSearch_CancelRequestPlayersForGame.argtypes = [ POINTER(ISteamGameSearch),  ]
    ISteamGameSearch_CancelRequestPlayersForGame.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_SubmitPlayerResult
    ISteamGameSearch_SubmitPlayerResult = dll.SteamAPI_ISteamGameSearch_SubmitPlayerResult
    ISteamGameSearch_SubmitPlayerResult.argtypes = [ POINTER(ISteamGameSearch), c_ulonglong, c_ulonglong, EPlayerResult_t ]
    ISteamGameSearch_SubmitPlayerResult.restype = EGameSearchErrorCode_t

    global ISteamGameSearch_EndGame
    ISteamGameSearch_EndGame = dll.SteamAPI_ISteamGameSearch_EndGame
    ISteamGameSearch_EndGame.argtypes = [ POINTER(ISteamGameSearch), c_ulonglong ]
    ISteamGameSearch_EndGame.restype = EGameSearchErrorCode_t

    global SteamGameSearch_v001
    SteamGameSearch_v001 = dll.SteamAPI_SteamGameSearch_v001
    SteamGameSearch_v001.argtypes = [ ]
    SteamGameSearch_v001.restype = POINTER(ISteamGameSearch)

    global ISteamParties_GetNumActiveBeacons
    ISteamParties_GetNumActiveBeacons = dll.SteamAPI_ISteamParties_GetNumActiveBeacons
    ISteamParties_GetNumActiveBeacons.argtypes = [ POINTER(ISteamParties),  ]
    ISteamParties_GetNumActiveBeacons.restype = c_uint

    global ISteamParties_GetBeaconByIndex
    ISteamParties_GetBeaconByIndex = dll.SteamAPI_ISteamParties_GetBeaconByIndex
    ISteamParties_GetBeaconByIndex.argtypes = [ POINTER(ISteamParties), c_uint ]
    ISteamParties_GetBeaconByIndex.restype = c_ulonglong

    global ISteamParties_GetBeaconDetails
    ISteamParties_GetBeaconDetails = dll.SteamAPI_ISteamParties_GetBeaconDetails
    ISteamParties_GetBeaconDetails.argtypes = [ POINTER(ISteamParties), c_ulonglong, POINTER(c_ulonglong), POINTER(SteamPartyBeaconLocation_t), c_char_p, c_int ]
    ISteamParties_GetBeaconDetails.restype = c_bool

    global ISteamParties_JoinParty
    ISteamParties_JoinParty = dll.SteamAPI_ISteamParties_JoinParty
    ISteamParties_JoinParty.argtypes = [ POINTER(ISteamParties), c_ulonglong ]
    ISteamParties_JoinParty.restype = c_ulonglong

    global ISteamParties_GetNumAvailableBeaconLocations
    ISteamParties_GetNumAvailableBeaconLocations = dll.SteamAPI_ISteamParties_GetNumAvailableBeaconLocations
    ISteamParties_GetNumAvailableBeaconLocations.argtypes = [ POINTER(ISteamParties), POINTER(c_uint) ]
    ISteamParties_GetNumAvailableBeaconLocations.restype = c_bool

    global ISteamParties_GetAvailableBeaconLocations
    ISteamParties_GetAvailableBeaconLocations = dll.SteamAPI_ISteamParties_GetAvailableBeaconLocations
    ISteamParties_GetAvailableBeaconLocations.argtypes = [ POINTER(ISteamParties), POINTER(SteamPartyBeaconLocation_t), c_uint ]
    ISteamParties_GetAvailableBeaconLocations.restype = c_bool

    global ISteamParties_CreateBeacon
    ISteamParties_CreateBeacon = dll.SteamAPI_ISteamParties_CreateBeacon
    ISteamParties_CreateBeacon.argtypes = [ POINTER(ISteamParties), c_uint, POINTER(SteamPartyBeaconLocation_t), c_char_p, c_char_p ]
    ISteamParties_CreateBeacon.restype = c_ulonglong

    global ISteamParties_OnReservationCompleted
    ISteamParties_OnReservationCompleted = dll.SteamAPI_ISteamParties_OnReservationCompleted
    ISteamParties_OnReservationCompleted.argtypes = [ POINTER(ISteamParties), c_ulonglong, c_ulonglong ]
    ISteamParties_OnReservationCompleted.restype = None

    global ISteamParties_CancelReservation
    ISteamParties_CancelReservation = dll.SteamAPI_ISteamParties_CancelReservation
    ISteamParties_CancelReservation.argtypes = [ POINTER(ISteamParties), c_ulonglong, c_ulonglong ]
    ISteamParties_CancelReservation.restype = None

    global ISteamParties_ChangeNumOpenSlots
    ISteamParties_ChangeNumOpenSlots = dll.SteamAPI_ISteamParties_ChangeNumOpenSlots
    ISteamParties_ChangeNumOpenSlots.argtypes = [ POINTER(ISteamParties), c_ulonglong, c_uint ]
    ISteamParties_ChangeNumOpenSlots.restype = c_ulonglong

    global ISteamParties_DestroyBeacon
    ISteamParties_DestroyBeacon = dll.SteamAPI_ISteamParties_DestroyBeacon
    ISteamParties_DestroyBeacon.argtypes = [ POINTER(ISteamParties), c_ulonglong ]
    ISteamParties_DestroyBeacon.restype = c_bool

    global ISteamParties_GetBeaconLocationData
    ISteamParties_GetBeaconLocationData = dll.SteamAPI_ISteamParties_GetBeaconLocationData
    ISteamParties_GetBeaconLocationData.argtypes = [ POINTER(ISteamParties), SteamPartyBeaconLocation_t, ESteamPartyBeaconLocationData, c_char_p, c_int ]
    ISteamParties_GetBeaconLocationData.restype = c_bool

    global SteamParties_v002
    SteamParties_v002 = dll.SteamAPI_SteamParties_v002
    SteamParties_v002.argtypes = [ ]
    SteamParties_v002.restype = POINTER(ISteamParties)

    global ISteamRemoteStorage_FileWrite
    ISteamRemoteStorage_FileWrite = dll.SteamAPI_ISteamRemoteStorage_FileWrite
    ISteamRemoteStorage_FileWrite.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, c_void_p, c_int ]
    ISteamRemoteStorage_FileWrite.restype = c_bool

    global ISteamRemoteStorage_FileRead
    ISteamRemoteStorage_FileRead = dll.SteamAPI_ISteamRemoteStorage_FileRead
    ISteamRemoteStorage_FileRead.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, c_void_p, c_int ]
    ISteamRemoteStorage_FileRead.restype = c_int

    global ISteamRemoteStorage_FileWriteAsync
    ISteamRemoteStorage_FileWriteAsync = dll.SteamAPI_ISteamRemoteStorage_FileWriteAsync
    ISteamRemoteStorage_FileWriteAsync.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, c_void_p, c_uint ]
    ISteamRemoteStorage_FileWriteAsync.restype = c_ulonglong

    global ISteamRemoteStorage_FileReadAsync
    ISteamRemoteStorage_FileReadAsync = dll.SteamAPI_ISteamRemoteStorage_FileReadAsync
    ISteamRemoteStorage_FileReadAsync.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, c_uint, c_uint ]
    ISteamRemoteStorage_FileReadAsync.restype = c_ulonglong

    global ISteamRemoteStorage_FileReadAsyncComplete
    ISteamRemoteStorage_FileReadAsyncComplete = dll.SteamAPI_ISteamRemoteStorage_FileReadAsyncComplete
    ISteamRemoteStorage_FileReadAsyncComplete.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_void_p, c_uint ]
    ISteamRemoteStorage_FileReadAsyncComplete.restype = c_bool

    global ISteamRemoteStorage_FileForget
    ISteamRemoteStorage_FileForget = dll.SteamAPI_ISteamRemoteStorage_FileForget
    ISteamRemoteStorage_FileForget.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FileForget.restype = c_bool

    global ISteamRemoteStorage_FileDelete
    ISteamRemoteStorage_FileDelete = dll.SteamAPI_ISteamRemoteStorage_FileDelete
    ISteamRemoteStorage_FileDelete.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FileDelete.restype = c_bool

    global ISteamRemoteStorage_FileShare
    ISteamRemoteStorage_FileShare = dll.SteamAPI_ISteamRemoteStorage_FileShare
    ISteamRemoteStorage_FileShare.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FileShare.restype = c_ulonglong

    global ISteamRemoteStorage_SetSyncPlatforms
    ISteamRemoteStorage_SetSyncPlatforms = dll.SteamAPI_ISteamRemoteStorage_SetSyncPlatforms
    ISteamRemoteStorage_SetSyncPlatforms.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, ERemoteStoragePlatform ]
    ISteamRemoteStorage_SetSyncPlatforms.restype = c_bool

    global ISteamRemoteStorage_FileWriteStreamOpen
    ISteamRemoteStorage_FileWriteStreamOpen = dll.SteamAPI_ISteamRemoteStorage_FileWriteStreamOpen
    ISteamRemoteStorage_FileWriteStreamOpen.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FileWriteStreamOpen.restype = c_ulonglong

    global ISteamRemoteStorage_FileWriteStreamWriteChunk
    ISteamRemoteStorage_FileWriteStreamWriteChunk = dll.SteamAPI_ISteamRemoteStorage_FileWriteStreamWriteChunk
    ISteamRemoteStorage_FileWriteStreamWriteChunk.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_void_p, c_int ]
    ISteamRemoteStorage_FileWriteStreamWriteChunk.restype = c_bool

    global ISteamRemoteStorage_FileWriteStreamClose
    ISteamRemoteStorage_FileWriteStreamClose = dll.SteamAPI_ISteamRemoteStorage_FileWriteStreamClose
    ISteamRemoteStorage_FileWriteStreamClose.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_FileWriteStreamClose.restype = c_bool

    global ISteamRemoteStorage_FileWriteStreamCancel
    ISteamRemoteStorage_FileWriteStreamCancel = dll.SteamAPI_ISteamRemoteStorage_FileWriteStreamCancel
    ISteamRemoteStorage_FileWriteStreamCancel.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_FileWriteStreamCancel.restype = c_bool

    global ISteamRemoteStorage_FileExists
    ISteamRemoteStorage_FileExists = dll.SteamAPI_ISteamRemoteStorage_FileExists
    ISteamRemoteStorage_FileExists.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FileExists.restype = c_bool

    global ISteamRemoteStorage_FilePersisted
    ISteamRemoteStorage_FilePersisted = dll.SteamAPI_ISteamRemoteStorage_FilePersisted
    ISteamRemoteStorage_FilePersisted.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_FilePersisted.restype = c_bool

    global ISteamRemoteStorage_GetFileSize
    ISteamRemoteStorage_GetFileSize = dll.SteamAPI_ISteamRemoteStorage_GetFileSize
    ISteamRemoteStorage_GetFileSize.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_GetFileSize.restype = c_int

    global ISteamRemoteStorage_GetFileTimestamp
    ISteamRemoteStorage_GetFileTimestamp = dll.SteamAPI_ISteamRemoteStorage_GetFileTimestamp
    ISteamRemoteStorage_GetFileTimestamp.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_GetFileTimestamp.restype = c_longlong

    global ISteamRemoteStorage_GetSyncPlatforms
    ISteamRemoteStorage_GetSyncPlatforms = dll.SteamAPI_ISteamRemoteStorage_GetSyncPlatforms
    ISteamRemoteStorage_GetSyncPlatforms.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p ]
    ISteamRemoteStorage_GetSyncPlatforms.restype = ERemoteStoragePlatform

    global ISteamRemoteStorage_GetFileCount
    ISteamRemoteStorage_GetFileCount = dll.SteamAPI_ISteamRemoteStorage_GetFileCount
    ISteamRemoteStorage_GetFileCount.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_GetFileCount.restype = c_int

    global ISteamRemoteStorage_GetFileNameAndSize
    ISteamRemoteStorage_GetFileNameAndSize = dll.SteamAPI_ISteamRemoteStorage_GetFileNameAndSize
    ISteamRemoteStorage_GetFileNameAndSize.argtypes = [ POINTER(ISteamRemoteStorage), c_int, POINTER(c_int) ]
    ISteamRemoteStorage_GetFileNameAndSize.restype = c_char_p

    global ISteamRemoteStorage_GetQuota
    ISteamRemoteStorage_GetQuota = dll.SteamAPI_ISteamRemoteStorage_GetQuota
    ISteamRemoteStorage_GetQuota.argtypes = [ POINTER(ISteamRemoteStorage), POINTER(c_ulonglong), POINTER(c_ulonglong) ]
    ISteamRemoteStorage_GetQuota.restype = c_bool

    global ISteamRemoteStorage_IsCloudEnabledForAccount
    ISteamRemoteStorage_IsCloudEnabledForAccount = dll.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForAccount
    ISteamRemoteStorage_IsCloudEnabledForAccount.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_IsCloudEnabledForAccount.restype = c_bool

    global ISteamRemoteStorage_IsCloudEnabledForApp
    ISteamRemoteStorage_IsCloudEnabledForApp = dll.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForApp
    ISteamRemoteStorage_IsCloudEnabledForApp.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_IsCloudEnabledForApp.restype = c_bool

    global ISteamRemoteStorage_SetCloudEnabledForApp
    ISteamRemoteStorage_SetCloudEnabledForApp = dll.SteamAPI_ISteamRemoteStorage_SetCloudEnabledForApp
    ISteamRemoteStorage_SetCloudEnabledForApp.argtypes = [ POINTER(ISteamRemoteStorage), c_bool ]
    ISteamRemoteStorage_SetCloudEnabledForApp.restype = None

    global ISteamRemoteStorage_UGCDownload
    ISteamRemoteStorage_UGCDownload = dll.SteamAPI_ISteamRemoteStorage_UGCDownload
    ISteamRemoteStorage_UGCDownload.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_uint ]
    ISteamRemoteStorage_UGCDownload.restype = c_ulonglong

    global ISteamRemoteStorage_GetUGCDownloadProgress
    ISteamRemoteStorage_GetUGCDownloadProgress = dll.SteamAPI_ISteamRemoteStorage_GetUGCDownloadProgress
    ISteamRemoteStorage_GetUGCDownloadProgress.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, POINTER(c_int), POINTER(c_int) ]
    ISteamRemoteStorage_GetUGCDownloadProgress.restype = c_bool

    global ISteamRemoteStorage_GetUGCDetails
    ISteamRemoteStorage_GetUGCDetails = dll.SteamAPI_ISteamRemoteStorage_GetUGCDetails
    ISteamRemoteStorage_GetUGCDetails.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, POINTER(c_uint), POINTER(c_char_p), POINTER(c_int), POINTER(c_ulonglong) ]
    ISteamRemoteStorage_GetUGCDetails.restype = c_bool

    global ISteamRemoteStorage_UGCRead
    ISteamRemoteStorage_UGCRead = dll.SteamAPI_ISteamRemoteStorage_UGCRead
    ISteamRemoteStorage_UGCRead.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_void_p, c_int, c_uint, EUGCReadAction ]
    ISteamRemoteStorage_UGCRead.restype = c_int

    global ISteamRemoteStorage_GetCachedUGCCount
    ISteamRemoteStorage_GetCachedUGCCount = dll.SteamAPI_ISteamRemoteStorage_GetCachedUGCCount
    ISteamRemoteStorage_GetCachedUGCCount.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_GetCachedUGCCount.restype = c_int

    global ISteamRemoteStorage_GetCachedUGCHandle
    ISteamRemoteStorage_GetCachedUGCHandle = dll.SteamAPI_ISteamRemoteStorage_GetCachedUGCHandle
    ISteamRemoteStorage_GetCachedUGCHandle.argtypes = [ POINTER(ISteamRemoteStorage), c_int ]
    ISteamRemoteStorage_GetCachedUGCHandle.restype = c_ulonglong

    global ISteamRemoteStorage_PublishWorkshopFile
    ISteamRemoteStorage_PublishWorkshopFile = dll.SteamAPI_ISteamRemoteStorage_PublishWorkshopFile
    ISteamRemoteStorage_PublishWorkshopFile.argtypes = [ POINTER(ISteamRemoteStorage), c_char_p, c_char_p, c_uint, c_char_p, c_char_p, ERemoteStoragePublishedFileVisibility, POINTER(SteamParamStringArray_t), EWorkshopFileType ]
    ISteamRemoteStorage_PublishWorkshopFile.restype = c_ulonglong

    global ISteamRemoteStorage_CreatePublishedFileUpdateRequest
    ISteamRemoteStorage_CreatePublishedFileUpdateRequest = dll.SteamAPI_ISteamRemoteStorage_CreatePublishedFileUpdateRequest
    ISteamRemoteStorage_CreatePublishedFileUpdateRequest.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_CreatePublishedFileUpdateRequest.restype = c_ulonglong

    global ISteamRemoteStorage_UpdatePublishedFileFile
    ISteamRemoteStorage_UpdatePublishedFileFile = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileFile
    ISteamRemoteStorage_UpdatePublishedFileFile.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p ]
    ISteamRemoteStorage_UpdatePublishedFileFile.restype = c_bool

    global ISteamRemoteStorage_UpdatePublishedFilePreviewFile
    ISteamRemoteStorage_UpdatePublishedFilePreviewFile = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFilePreviewFile
    ISteamRemoteStorage_UpdatePublishedFilePreviewFile.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p ]
    ISteamRemoteStorage_UpdatePublishedFilePreviewFile.restype = c_bool

    global ISteamRemoteStorage_UpdatePublishedFileTitle
    ISteamRemoteStorage_UpdatePublishedFileTitle = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTitle
    ISteamRemoteStorage_UpdatePublishedFileTitle.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p ]
    ISteamRemoteStorage_UpdatePublishedFileTitle.restype = c_bool

    global ISteamRemoteStorage_UpdatePublishedFileDescription
    ISteamRemoteStorage_UpdatePublishedFileDescription = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileDescription
    ISteamRemoteStorage_UpdatePublishedFileDescription.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p ]
    ISteamRemoteStorage_UpdatePublishedFileDescription.restype = c_bool

    global ISteamRemoteStorage_UpdatePublishedFileVisibility
    ISteamRemoteStorage_UpdatePublishedFileVisibility = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileVisibility
    ISteamRemoteStorage_UpdatePublishedFileVisibility.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, ERemoteStoragePublishedFileVisibility ]
    ISteamRemoteStorage_UpdatePublishedFileVisibility.restype = c_bool

    global ISteamRemoteStorage_UpdatePublishedFileTags
    ISteamRemoteStorage_UpdatePublishedFileTags = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTags
    ISteamRemoteStorage_UpdatePublishedFileTags.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, POINTER(SteamParamStringArray_t) ]
    ISteamRemoteStorage_UpdatePublishedFileTags.restype = c_bool

    global ISteamRemoteStorage_CommitPublishedFileUpdate
    ISteamRemoteStorage_CommitPublishedFileUpdate = dll.SteamAPI_ISteamRemoteStorage_CommitPublishedFileUpdate
    ISteamRemoteStorage_CommitPublishedFileUpdate.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_CommitPublishedFileUpdate.restype = c_ulonglong

    global ISteamRemoteStorage_GetPublishedFileDetails
    ISteamRemoteStorage_GetPublishedFileDetails = dll.SteamAPI_ISteamRemoteStorage_GetPublishedFileDetails
    ISteamRemoteStorage_GetPublishedFileDetails.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_uint ]
    ISteamRemoteStorage_GetPublishedFileDetails.restype = c_ulonglong

    global ISteamRemoteStorage_DeletePublishedFile
    ISteamRemoteStorage_DeletePublishedFile = dll.SteamAPI_ISteamRemoteStorage_DeletePublishedFile
    ISteamRemoteStorage_DeletePublishedFile.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_DeletePublishedFile.restype = c_ulonglong

    global ISteamRemoteStorage_EnumerateUserPublishedFiles
    ISteamRemoteStorage_EnumerateUserPublishedFiles = dll.SteamAPI_ISteamRemoteStorage_EnumerateUserPublishedFiles
    ISteamRemoteStorage_EnumerateUserPublishedFiles.argtypes = [ POINTER(ISteamRemoteStorage), c_uint ]
    ISteamRemoteStorage_EnumerateUserPublishedFiles.restype = c_ulonglong

    global ISteamRemoteStorage_SubscribePublishedFile
    ISteamRemoteStorage_SubscribePublishedFile = dll.SteamAPI_ISteamRemoteStorage_SubscribePublishedFile
    ISteamRemoteStorage_SubscribePublishedFile.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_SubscribePublishedFile.restype = c_ulonglong

    global ISteamRemoteStorage_EnumerateUserSubscribedFiles
    ISteamRemoteStorage_EnumerateUserSubscribedFiles = dll.SteamAPI_ISteamRemoteStorage_EnumerateUserSubscribedFiles
    ISteamRemoteStorage_EnumerateUserSubscribedFiles.argtypes = [ POINTER(ISteamRemoteStorage), c_uint ]
    ISteamRemoteStorage_EnumerateUserSubscribedFiles.restype = c_ulonglong

    global ISteamRemoteStorage_UnsubscribePublishedFile
    ISteamRemoteStorage_UnsubscribePublishedFile = dll.SteamAPI_ISteamRemoteStorage_UnsubscribePublishedFile
    ISteamRemoteStorage_UnsubscribePublishedFile.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_UnsubscribePublishedFile.restype = c_ulonglong

    global ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription
    ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription = dll.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription
    ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p ]
    ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription.restype = c_bool

    global ISteamRemoteStorage_GetPublishedItemVoteDetails
    ISteamRemoteStorage_GetPublishedItemVoteDetails = dll.SteamAPI_ISteamRemoteStorage_GetPublishedItemVoteDetails
    ISteamRemoteStorage_GetPublishedItemVoteDetails.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_GetPublishedItemVoteDetails.restype = c_ulonglong

    global ISteamRemoteStorage_UpdateUserPublishedItemVote
    ISteamRemoteStorage_UpdateUserPublishedItemVote = dll.SteamAPI_ISteamRemoteStorage_UpdateUserPublishedItemVote
    ISteamRemoteStorage_UpdateUserPublishedItemVote.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_bool ]
    ISteamRemoteStorage_UpdateUserPublishedItemVote.restype = c_ulonglong

    global ISteamRemoteStorage_GetUserPublishedItemVoteDetails
    ISteamRemoteStorage_GetUserPublishedItemVoteDetails = dll.SteamAPI_ISteamRemoteStorage_GetUserPublishedItemVoteDetails
    ISteamRemoteStorage_GetUserPublishedItemVoteDetails.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong ]
    ISteamRemoteStorage_GetUserPublishedItemVoteDetails.restype = c_ulonglong

    global ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles
    ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles = dll.SteamAPI_ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles
    ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_uint, POINTER(SteamParamStringArray_t), POINTER(SteamParamStringArray_t) ]
    ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles.restype = c_ulonglong

    global ISteamRemoteStorage_PublishVideo
    ISteamRemoteStorage_PublishVideo = dll.SteamAPI_ISteamRemoteStorage_PublishVideo
    ISteamRemoteStorage_PublishVideo.argtypes = [ POINTER(ISteamRemoteStorage), EWorkshopVideoProvider, c_char_p, c_char_p, c_char_p, c_uint, c_char_p, c_char_p, ERemoteStoragePublishedFileVisibility, POINTER(SteamParamStringArray_t) ]
    ISteamRemoteStorage_PublishVideo.restype = c_ulonglong

    global ISteamRemoteStorage_SetUserPublishedFileAction
    ISteamRemoteStorage_SetUserPublishedFileAction = dll.SteamAPI_ISteamRemoteStorage_SetUserPublishedFileAction
    ISteamRemoteStorage_SetUserPublishedFileAction.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, EWorkshopFileAction ]
    ISteamRemoteStorage_SetUserPublishedFileAction.restype = c_ulonglong

    global ISteamRemoteStorage_EnumeratePublishedFilesByUserAction
    ISteamRemoteStorage_EnumeratePublishedFilesByUserAction = dll.SteamAPI_ISteamRemoteStorage_EnumeratePublishedFilesByUserAction
    ISteamRemoteStorage_EnumeratePublishedFilesByUserAction.argtypes = [ POINTER(ISteamRemoteStorage), EWorkshopFileAction, c_uint ]
    ISteamRemoteStorage_EnumeratePublishedFilesByUserAction.restype = c_ulonglong

    global ISteamRemoteStorage_EnumeratePublishedWorkshopFiles
    ISteamRemoteStorage_EnumeratePublishedWorkshopFiles = dll.SteamAPI_ISteamRemoteStorage_EnumeratePublishedWorkshopFiles
    ISteamRemoteStorage_EnumeratePublishedWorkshopFiles.argtypes = [ POINTER(ISteamRemoteStorage), EWorkshopEnumerationType, c_uint, c_uint, c_uint, POINTER(SteamParamStringArray_t), POINTER(SteamParamStringArray_t) ]
    ISteamRemoteStorage_EnumeratePublishedWorkshopFiles.restype = c_ulonglong

    global ISteamRemoteStorage_UGCDownloadToLocation
    ISteamRemoteStorage_UGCDownloadToLocation = dll.SteamAPI_ISteamRemoteStorage_UGCDownloadToLocation
    ISteamRemoteStorage_UGCDownloadToLocation.argtypes = [ POINTER(ISteamRemoteStorage), c_ulonglong, c_char_p, c_uint ]
    ISteamRemoteStorage_UGCDownloadToLocation.restype = c_ulonglong

    global ISteamRemoteStorage_GetLocalFileChangeCount
    ISteamRemoteStorage_GetLocalFileChangeCount = dll.SteamAPI_ISteamRemoteStorage_GetLocalFileChangeCount
    ISteamRemoteStorage_GetLocalFileChangeCount.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_GetLocalFileChangeCount.restype = c_int

    global ISteamRemoteStorage_GetLocalFileChange
    ISteamRemoteStorage_GetLocalFileChange = dll.SteamAPI_ISteamRemoteStorage_GetLocalFileChange
    ISteamRemoteStorage_GetLocalFileChange.argtypes = [ POINTER(ISteamRemoteStorage), c_int, POINTER(ERemoteStorageLocalFileChange), POINTER(ERemoteStorageFilePathType) ]
    ISteamRemoteStorage_GetLocalFileChange.restype = c_char_p

    global ISteamRemoteStorage_BeginFileWriteBatch
    ISteamRemoteStorage_BeginFileWriteBatch = dll.SteamAPI_ISteamRemoteStorage_BeginFileWriteBatch
    ISteamRemoteStorage_BeginFileWriteBatch.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_BeginFileWriteBatch.restype = c_bool

    global ISteamRemoteStorage_EndFileWriteBatch
    ISteamRemoteStorage_EndFileWriteBatch = dll.SteamAPI_ISteamRemoteStorage_EndFileWriteBatch
    ISteamRemoteStorage_EndFileWriteBatch.argtypes = [ POINTER(ISteamRemoteStorage),  ]
    ISteamRemoteStorage_EndFileWriteBatch.restype = c_bool

    global SteamRemoteStorage_v016
    SteamRemoteStorage_v016 = dll.SteamAPI_SteamRemoteStorage_v016
    SteamRemoteStorage_v016.argtypes = [ ]
    SteamRemoteStorage_v016.restype = POINTER(ISteamRemoteStorage)

    global ISteamUserStats_RequestCurrentStats
    ISteamUserStats_RequestCurrentStats = dll.SteamAPI_ISteamUserStats_RequestCurrentStats
    ISteamUserStats_RequestCurrentStats.argtypes = [ POINTER(ISteamUserStats),  ]
    ISteamUserStats_RequestCurrentStats.restype = c_bool

    global ISteamUserStats_GetStatInt32
    ISteamUserStats_GetStatInt32 = dll.SteamAPI_ISteamUserStats_GetStatInt32
    ISteamUserStats_GetStatInt32.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_int) ]
    ISteamUserStats_GetStatInt32.restype = c_bool

    global ISteamUserStats_GetStatFloat
    ISteamUserStats_GetStatFloat = dll.SteamAPI_ISteamUserStats_GetStatFloat
    ISteamUserStats_GetStatFloat.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_float) ]
    ISteamUserStats_GetStatFloat.restype = c_bool

    global ISteamUserStats_SetStatInt32
    ISteamUserStats_SetStatInt32 = dll.SteamAPI_ISteamUserStats_SetStatInt32
    ISteamUserStats_SetStatInt32.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_int ]
    ISteamUserStats_SetStatInt32.restype = c_bool

    global ISteamUserStats_SetStatFloat
    ISteamUserStats_SetStatFloat = dll.SteamAPI_ISteamUserStats_SetStatFloat
    ISteamUserStats_SetStatFloat.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_float ]
    ISteamUserStats_SetStatFloat.restype = c_bool

    global ISteamUserStats_UpdateAvgRateStat
    ISteamUserStats_UpdateAvgRateStat = dll.SteamAPI_ISteamUserStats_UpdateAvgRateStat
    ISteamUserStats_UpdateAvgRateStat.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_float, c_double ]
    ISteamUserStats_UpdateAvgRateStat.restype = c_bool

    global ISteamUserStats_GetAchievement
    ISteamUserStats_GetAchievement = dll.SteamAPI_ISteamUserStats_GetAchievement
    ISteamUserStats_GetAchievement.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_bool) ]
    ISteamUserStats_GetAchievement.restype = c_bool

    global ISteamUserStats_SetAchievement
    ISteamUserStats_SetAchievement = dll.SteamAPI_ISteamUserStats_SetAchievement
    ISteamUserStats_SetAchievement.argtypes = [ POINTER(ISteamUserStats), c_char_p ]
    ISteamUserStats_SetAchievement.restype = c_bool

    global ISteamUserStats_ClearAchievement
    ISteamUserStats_ClearAchievement = dll.SteamAPI_ISteamUserStats_ClearAchievement
    ISteamUserStats_ClearAchievement.argtypes = [ POINTER(ISteamUserStats), c_char_p ]
    ISteamUserStats_ClearAchievement.restype = c_bool

    global ISteamUserStats_GetAchievementAndUnlockTime
    ISteamUserStats_GetAchievementAndUnlockTime = dll.SteamAPI_ISteamUserStats_GetAchievementAndUnlockTime
    ISteamUserStats_GetAchievementAndUnlockTime.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_bool), POINTER(c_uint) ]
    ISteamUserStats_GetAchievementAndUnlockTime.restype = c_bool

    global ISteamUserStats_StoreStats
    ISteamUserStats_StoreStats = dll.SteamAPI_ISteamUserStats_StoreStats
    ISteamUserStats_StoreStats.argtypes = [ POINTER(ISteamUserStats),  ]
    ISteamUserStats_StoreStats.restype = c_bool

    global ISteamUserStats_GetAchievementIcon
    ISteamUserStats_GetAchievementIcon = dll.SteamAPI_ISteamUserStats_GetAchievementIcon
    ISteamUserStats_GetAchievementIcon.argtypes = [ POINTER(ISteamUserStats), c_char_p ]
    ISteamUserStats_GetAchievementIcon.restype = c_int

    global ISteamUserStats_GetAchievementDisplayAttribute
    ISteamUserStats_GetAchievementDisplayAttribute = dll.SteamAPI_ISteamUserStats_GetAchievementDisplayAttribute
    ISteamUserStats_GetAchievementDisplayAttribute.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_char_p ]
    ISteamUserStats_GetAchievementDisplayAttribute.restype = c_char_p

    global ISteamUserStats_IndicateAchievementProgress
    ISteamUserStats_IndicateAchievementProgress = dll.SteamAPI_ISteamUserStats_IndicateAchievementProgress
    ISteamUserStats_IndicateAchievementProgress.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_uint, c_uint ]
    ISteamUserStats_IndicateAchievementProgress.restype = c_bool

    global ISteamUserStats_GetNumAchievements
    ISteamUserStats_GetNumAchievements = dll.SteamAPI_ISteamUserStats_GetNumAchievements
    ISteamUserStats_GetNumAchievements.argtypes = [ POINTER(ISteamUserStats),  ]
    ISteamUserStats_GetNumAchievements.restype = c_uint

    global ISteamUserStats_GetAchievementName
    ISteamUserStats_GetAchievementName = dll.SteamAPI_ISteamUserStats_GetAchievementName
    ISteamUserStats_GetAchievementName.argtypes = [ POINTER(ISteamUserStats), c_uint ]
    ISteamUserStats_GetAchievementName.restype = c_char_p

    global ISteamUserStats_RequestUserStats
    ISteamUserStats_RequestUserStats = dll.SteamAPI_ISteamUserStats_RequestUserStats
    ISteamUserStats_RequestUserStats.argtypes = [ POINTER(ISteamUserStats), c_ulonglong ]
    ISteamUserStats_RequestUserStats.restype = c_ulonglong

    global ISteamUserStats_GetUserStatInt32
    ISteamUserStats_GetUserStatInt32 = dll.SteamAPI_ISteamUserStats_GetUserStatInt32
    ISteamUserStats_GetUserStatInt32.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_char_p, POINTER(c_int) ]
    ISteamUserStats_GetUserStatInt32.restype = c_bool

    global ISteamUserStats_GetUserStatFloat
    ISteamUserStats_GetUserStatFloat = dll.SteamAPI_ISteamUserStats_GetUserStatFloat
    ISteamUserStats_GetUserStatFloat.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_char_p, POINTER(c_float) ]
    ISteamUserStats_GetUserStatFloat.restype = c_bool

    global ISteamUserStats_GetUserAchievement
    ISteamUserStats_GetUserAchievement = dll.SteamAPI_ISteamUserStats_GetUserAchievement
    ISteamUserStats_GetUserAchievement.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_char_p, POINTER(c_bool) ]
    ISteamUserStats_GetUserAchievement.restype = c_bool

    global ISteamUserStats_GetUserAchievementAndUnlockTime
    ISteamUserStats_GetUserAchievementAndUnlockTime = dll.SteamAPI_ISteamUserStats_GetUserAchievementAndUnlockTime
    ISteamUserStats_GetUserAchievementAndUnlockTime.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_char_p, POINTER(c_bool), POINTER(c_uint) ]
    ISteamUserStats_GetUserAchievementAndUnlockTime.restype = c_bool

    global ISteamUserStats_ResetAllStats
    ISteamUserStats_ResetAllStats = dll.SteamAPI_ISteamUserStats_ResetAllStats
    ISteamUserStats_ResetAllStats.argtypes = [ POINTER(ISteamUserStats), c_bool ]
    ISteamUserStats_ResetAllStats.restype = c_bool

    global ISteamUserStats_FindOrCreateLeaderboard
    ISteamUserStats_FindOrCreateLeaderboard = dll.SteamAPI_ISteamUserStats_FindOrCreateLeaderboard
    ISteamUserStats_FindOrCreateLeaderboard.argtypes = [ POINTER(ISteamUserStats), c_char_p, ELeaderboardSortMethod, ELeaderboardDisplayType ]
    ISteamUserStats_FindOrCreateLeaderboard.restype = c_ulonglong

    global ISteamUserStats_FindLeaderboard
    ISteamUserStats_FindLeaderboard = dll.SteamAPI_ISteamUserStats_FindLeaderboard
    ISteamUserStats_FindLeaderboard.argtypes = [ POINTER(ISteamUserStats), c_char_p ]
    ISteamUserStats_FindLeaderboard.restype = c_ulonglong

    global ISteamUserStats_GetLeaderboardName
    ISteamUserStats_GetLeaderboardName = dll.SteamAPI_ISteamUserStats_GetLeaderboardName
    ISteamUserStats_GetLeaderboardName.argtypes = [ POINTER(ISteamUserStats), c_ulonglong ]
    ISteamUserStats_GetLeaderboardName.restype = c_char_p

    global ISteamUserStats_GetLeaderboardEntryCount
    ISteamUserStats_GetLeaderboardEntryCount = dll.SteamAPI_ISteamUserStats_GetLeaderboardEntryCount
    ISteamUserStats_GetLeaderboardEntryCount.argtypes = [ POINTER(ISteamUserStats), c_ulonglong ]
    ISteamUserStats_GetLeaderboardEntryCount.restype = c_int

    global ISteamUserStats_GetLeaderboardSortMethod
    ISteamUserStats_GetLeaderboardSortMethod = dll.SteamAPI_ISteamUserStats_GetLeaderboardSortMethod
    ISteamUserStats_GetLeaderboardSortMethod.argtypes = [ POINTER(ISteamUserStats), c_ulonglong ]
    ISteamUserStats_GetLeaderboardSortMethod.restype = ELeaderboardSortMethod

    global ISteamUserStats_GetLeaderboardDisplayType
    ISteamUserStats_GetLeaderboardDisplayType = dll.SteamAPI_ISteamUserStats_GetLeaderboardDisplayType
    ISteamUserStats_GetLeaderboardDisplayType.argtypes = [ POINTER(ISteamUserStats), c_ulonglong ]
    ISteamUserStats_GetLeaderboardDisplayType.restype = ELeaderboardDisplayType

    global ISteamUserStats_DownloadLeaderboardEntries
    ISteamUserStats_DownloadLeaderboardEntries = dll.SteamAPI_ISteamUserStats_DownloadLeaderboardEntries
    ISteamUserStats_DownloadLeaderboardEntries.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, ELeaderboardDataRequest, c_int, c_int ]
    ISteamUserStats_DownloadLeaderboardEntries.restype = c_ulonglong

    global ISteamUserStats_DownloadLeaderboardEntriesForUsers
    ISteamUserStats_DownloadLeaderboardEntriesForUsers = dll.SteamAPI_ISteamUserStats_DownloadLeaderboardEntriesForUsers
    ISteamUserStats_DownloadLeaderboardEntriesForUsers.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, POINTER(c_ulonglong), c_int ]
    ISteamUserStats_DownloadLeaderboardEntriesForUsers.restype = c_ulonglong

    global ISteamUserStats_GetDownloadedLeaderboardEntry
    ISteamUserStats_GetDownloadedLeaderboardEntry = dll.SteamAPI_ISteamUserStats_GetDownloadedLeaderboardEntry
    ISteamUserStats_GetDownloadedLeaderboardEntry.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_int, POINTER(LeaderboardEntry_t), POINTER(c_int), c_int ]
    ISteamUserStats_GetDownloadedLeaderboardEntry.restype = c_bool

    global ISteamUserStats_UploadLeaderboardScore
    ISteamUserStats_UploadLeaderboardScore = dll.SteamAPI_ISteamUserStats_UploadLeaderboardScore
    ISteamUserStats_UploadLeaderboardScore.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, ELeaderboardUploadScoreMethod, c_int, POINTER(c_int), c_int ]
    ISteamUserStats_UploadLeaderboardScore.restype = c_ulonglong

    global ISteamUserStats_AttachLeaderboardUGC
    ISteamUserStats_AttachLeaderboardUGC = dll.SteamAPI_ISteamUserStats_AttachLeaderboardUGC
    ISteamUserStats_AttachLeaderboardUGC.argtypes = [ POINTER(ISteamUserStats), c_ulonglong, c_ulonglong ]
    ISteamUserStats_AttachLeaderboardUGC.restype = c_ulonglong

    global ISteamUserStats_GetNumberOfCurrentPlayers
    ISteamUserStats_GetNumberOfCurrentPlayers = dll.SteamAPI_ISteamUserStats_GetNumberOfCurrentPlayers
    ISteamUserStats_GetNumberOfCurrentPlayers.argtypes = [ POINTER(ISteamUserStats),  ]
    ISteamUserStats_GetNumberOfCurrentPlayers.restype = c_ulonglong

    global ISteamUserStats_RequestGlobalAchievementPercentages
    ISteamUserStats_RequestGlobalAchievementPercentages = dll.SteamAPI_ISteamUserStats_RequestGlobalAchievementPercentages
    ISteamUserStats_RequestGlobalAchievementPercentages.argtypes = [ POINTER(ISteamUserStats),  ]
    ISteamUserStats_RequestGlobalAchievementPercentages.restype = c_ulonglong

    global ISteamUserStats_GetMostAchievedAchievementInfo
    ISteamUserStats_GetMostAchievedAchievementInfo = dll.SteamAPI_ISteamUserStats_GetMostAchievedAchievementInfo
    ISteamUserStats_GetMostAchievedAchievementInfo.argtypes = [ POINTER(ISteamUserStats), c_char_p, c_uint, POINTER(c_float), POINTER(c_bool) ]
    ISteamUserStats_GetMostAchievedAchievementInfo.restype = c_int

    global ISteamUserStats_GetNextMostAchievedAchievementInfo
    ISteamUserStats_GetNextMostAchievedAchievementInfo = dll.SteamAPI_ISteamUserStats_GetNextMostAchievedAchievementInfo
    ISteamUserStats_GetNextMostAchievedAchievementInfo.argtypes = [ POINTER(ISteamUserStats), c_int, c_char_p, c_uint, POINTER(c_float), POINTER(c_bool) ]
    ISteamUserStats_GetNextMostAchievedAchievementInfo.restype = c_int

    global ISteamUserStats_GetAchievementAchievedPercent
    ISteamUserStats_GetAchievementAchievedPercent = dll.SteamAPI_ISteamUserStats_GetAchievementAchievedPercent
    ISteamUserStats_GetAchievementAchievedPercent.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_float) ]
    ISteamUserStats_GetAchievementAchievedPercent.restype = c_bool

    global ISteamUserStats_RequestGlobalStats
    ISteamUserStats_RequestGlobalStats = dll.SteamAPI_ISteamUserStats_RequestGlobalStats
    ISteamUserStats_RequestGlobalStats.argtypes = [ POINTER(ISteamUserStats), c_int ]
    ISteamUserStats_RequestGlobalStats.restype = c_ulonglong

    global ISteamUserStats_GetGlobalStatInt64
    ISteamUserStats_GetGlobalStatInt64 = dll.SteamAPI_ISteamUserStats_GetGlobalStatInt64
    ISteamUserStats_GetGlobalStatInt64.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_longlong) ]
    ISteamUserStats_GetGlobalStatInt64.restype = c_bool

    global ISteamUserStats_GetGlobalStatDouble
    ISteamUserStats_GetGlobalStatDouble = dll.SteamAPI_ISteamUserStats_GetGlobalStatDouble
    ISteamUserStats_GetGlobalStatDouble.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_double) ]
    ISteamUserStats_GetGlobalStatDouble.restype = c_bool

    global ISteamUserStats_GetGlobalStatHistoryInt64
    ISteamUserStats_GetGlobalStatHistoryInt64 = dll.SteamAPI_ISteamUserStats_GetGlobalStatHistoryInt64
    ISteamUserStats_GetGlobalStatHistoryInt64.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_longlong), c_uint ]
    ISteamUserStats_GetGlobalStatHistoryInt64.restype = c_int

    global ISteamUserStats_GetGlobalStatHistoryDouble
    ISteamUserStats_GetGlobalStatHistoryDouble = dll.SteamAPI_ISteamUserStats_GetGlobalStatHistoryDouble
    ISteamUserStats_GetGlobalStatHistoryDouble.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_double), c_uint ]
    ISteamUserStats_GetGlobalStatHistoryDouble.restype = c_int

    global ISteamUserStats_GetAchievementProgressLimitsInt32
    ISteamUserStats_GetAchievementProgressLimitsInt32 = dll.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsInt32
    ISteamUserStats_GetAchievementProgressLimitsInt32.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_int), POINTER(c_int) ]
    ISteamUserStats_GetAchievementProgressLimitsInt32.restype = c_bool

    global ISteamUserStats_GetAchievementProgressLimitsFloat
    ISteamUserStats_GetAchievementProgressLimitsFloat = dll.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsFloat
    ISteamUserStats_GetAchievementProgressLimitsFloat.argtypes = [ POINTER(ISteamUserStats), c_char_p, POINTER(c_float), POINTER(c_float) ]
    ISteamUserStats_GetAchievementProgressLimitsFloat.restype = c_bool

    global SteamUserStats_v012
    SteamUserStats_v012 = dll.SteamAPI_SteamUserStats_v012
    SteamUserStats_v012.argtypes = [ ]
    SteamUserStats_v012.restype = POINTER(ISteamUserStats)

    global ISteamApps_BIsSubscribed
    ISteamApps_BIsSubscribed = dll.SteamAPI_ISteamApps_BIsSubscribed
    ISteamApps_BIsSubscribed.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsSubscribed.restype = c_bool

    global ISteamApps_BIsLowViolence
    ISteamApps_BIsLowViolence = dll.SteamAPI_ISteamApps_BIsLowViolence
    ISteamApps_BIsLowViolence.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsLowViolence.restype = c_bool

    global ISteamApps_BIsCybercafe
    ISteamApps_BIsCybercafe = dll.SteamAPI_ISteamApps_BIsCybercafe
    ISteamApps_BIsCybercafe.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsCybercafe.restype = c_bool

    global ISteamApps_BIsVACBanned
    ISteamApps_BIsVACBanned = dll.SteamAPI_ISteamApps_BIsVACBanned
    ISteamApps_BIsVACBanned.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsVACBanned.restype = c_bool

    global ISteamApps_GetCurrentGameLanguage
    ISteamApps_GetCurrentGameLanguage = dll.SteamAPI_ISteamApps_GetCurrentGameLanguage
    ISteamApps_GetCurrentGameLanguage.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_GetCurrentGameLanguage.restype = c_char_p

    global ISteamApps_GetAvailableGameLanguages
    ISteamApps_GetAvailableGameLanguages = dll.SteamAPI_ISteamApps_GetAvailableGameLanguages
    ISteamApps_GetAvailableGameLanguages.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_GetAvailableGameLanguages.restype = c_char_p

    global ISteamApps_BIsSubscribedApp
    ISteamApps_BIsSubscribedApp = dll.SteamAPI_ISteamApps_BIsSubscribedApp
    ISteamApps_BIsSubscribedApp.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_BIsSubscribedApp.restype = c_bool

    global ISteamApps_BIsDlcInstalled
    ISteamApps_BIsDlcInstalled = dll.SteamAPI_ISteamApps_BIsDlcInstalled
    ISteamApps_BIsDlcInstalled.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_BIsDlcInstalled.restype = c_bool

    global ISteamApps_GetEarliestPurchaseUnixTime
    ISteamApps_GetEarliestPurchaseUnixTime = dll.SteamAPI_ISteamApps_GetEarliestPurchaseUnixTime
    ISteamApps_GetEarliestPurchaseUnixTime.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_GetEarliestPurchaseUnixTime.restype = c_uint

    global ISteamApps_BIsSubscribedFromFreeWeekend
    ISteamApps_BIsSubscribedFromFreeWeekend = dll.SteamAPI_ISteamApps_BIsSubscribedFromFreeWeekend
    ISteamApps_BIsSubscribedFromFreeWeekend.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsSubscribedFromFreeWeekend.restype = c_bool

    global ISteamApps_GetDLCCount
    ISteamApps_GetDLCCount = dll.SteamAPI_ISteamApps_GetDLCCount
    ISteamApps_GetDLCCount.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_GetDLCCount.restype = c_int

    global ISteamApps_BGetDLCDataByIndex
    ISteamApps_BGetDLCDataByIndex = dll.SteamAPI_ISteamApps_BGetDLCDataByIndex
    ISteamApps_BGetDLCDataByIndex.argtypes = [ POINTER(ISteamApps), c_int, POINTER(c_uint), POINTER(c_bool), c_char_p, c_int ]
    ISteamApps_BGetDLCDataByIndex.restype = c_bool

    global ISteamApps_InstallDLC
    ISteamApps_InstallDLC = dll.SteamAPI_ISteamApps_InstallDLC
    ISteamApps_InstallDLC.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_InstallDLC.restype = None

    global ISteamApps_UninstallDLC
    ISteamApps_UninstallDLC = dll.SteamAPI_ISteamApps_UninstallDLC
    ISteamApps_UninstallDLC.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_UninstallDLC.restype = None

    global ISteamApps_RequestAppProofOfPurchaseKey
    ISteamApps_RequestAppProofOfPurchaseKey = dll.SteamAPI_ISteamApps_RequestAppProofOfPurchaseKey
    ISteamApps_RequestAppProofOfPurchaseKey.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_RequestAppProofOfPurchaseKey.restype = None

    global ISteamApps_GetCurrentBetaName
    ISteamApps_GetCurrentBetaName = dll.SteamAPI_ISteamApps_GetCurrentBetaName
    ISteamApps_GetCurrentBetaName.argtypes = [ POINTER(ISteamApps), c_char_p, c_int ]
    ISteamApps_GetCurrentBetaName.restype = c_bool

    global ISteamApps_MarkContentCorrupt
    ISteamApps_MarkContentCorrupt = dll.SteamAPI_ISteamApps_MarkContentCorrupt
    ISteamApps_MarkContentCorrupt.argtypes = [ POINTER(ISteamApps), c_bool ]
    ISteamApps_MarkContentCorrupt.restype = c_bool

    global ISteamApps_GetInstalledDepots
    ISteamApps_GetInstalledDepots = dll.SteamAPI_ISteamApps_GetInstalledDepots
    ISteamApps_GetInstalledDepots.argtypes = [ POINTER(ISteamApps), c_uint, POINTER(c_uint), c_uint ]
    ISteamApps_GetInstalledDepots.restype = c_uint

    global ISteamApps_GetAppInstallDir
    ISteamApps_GetAppInstallDir = dll.SteamAPI_ISteamApps_GetAppInstallDir
    ISteamApps_GetAppInstallDir.argtypes = [ POINTER(ISteamApps), c_uint, c_char_p, c_uint ]
    ISteamApps_GetAppInstallDir.restype = c_uint

    global ISteamApps_BIsAppInstalled
    ISteamApps_BIsAppInstalled = dll.SteamAPI_ISteamApps_BIsAppInstalled
    ISteamApps_BIsAppInstalled.argtypes = [ POINTER(ISteamApps), c_uint ]
    ISteamApps_BIsAppInstalled.restype = c_bool

    global ISteamApps_GetAppOwner
    ISteamApps_GetAppOwner = dll.SteamAPI_ISteamApps_GetAppOwner
    ISteamApps_GetAppOwner.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_GetAppOwner.restype = c_ulonglong

    global ISteamApps_GetLaunchQueryParam
    ISteamApps_GetLaunchQueryParam = dll.SteamAPI_ISteamApps_GetLaunchQueryParam
    ISteamApps_GetLaunchQueryParam.argtypes = [ POINTER(ISteamApps), c_char_p ]
    ISteamApps_GetLaunchQueryParam.restype = c_char_p

    global ISteamApps_GetDlcDownloadProgress
    ISteamApps_GetDlcDownloadProgress = dll.SteamAPI_ISteamApps_GetDlcDownloadProgress
    ISteamApps_GetDlcDownloadProgress.argtypes = [ POINTER(ISteamApps), c_uint, POINTER(c_ulonglong), POINTER(c_ulonglong) ]
    ISteamApps_GetDlcDownloadProgress.restype = c_bool

    global ISteamApps_GetAppBuildId
    ISteamApps_GetAppBuildId = dll.SteamAPI_ISteamApps_GetAppBuildId
    ISteamApps_GetAppBuildId.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_GetAppBuildId.restype = c_int

    global ISteamApps_RequestAllProofOfPurchaseKeys
    ISteamApps_RequestAllProofOfPurchaseKeys = dll.SteamAPI_ISteamApps_RequestAllProofOfPurchaseKeys
    ISteamApps_RequestAllProofOfPurchaseKeys.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_RequestAllProofOfPurchaseKeys.restype = None

    global ISteamApps_GetFileDetails
    ISteamApps_GetFileDetails = dll.SteamAPI_ISteamApps_GetFileDetails
    ISteamApps_GetFileDetails.argtypes = [ POINTER(ISteamApps), c_char_p ]
    ISteamApps_GetFileDetails.restype = c_ulonglong

    global ISteamApps_GetLaunchCommandLine
    ISteamApps_GetLaunchCommandLine = dll.SteamAPI_ISteamApps_GetLaunchCommandLine
    ISteamApps_GetLaunchCommandLine.argtypes = [ POINTER(ISteamApps), c_char_p, c_int ]
    ISteamApps_GetLaunchCommandLine.restype = c_int

    global ISteamApps_BIsSubscribedFromFamilySharing
    ISteamApps_BIsSubscribedFromFamilySharing = dll.SteamAPI_ISteamApps_BIsSubscribedFromFamilySharing
    ISteamApps_BIsSubscribedFromFamilySharing.argtypes = [ POINTER(ISteamApps),  ]
    ISteamApps_BIsSubscribedFromFamilySharing.restype = c_bool

    global ISteamApps_BIsTimedTrial
    ISteamApps_BIsTimedTrial = dll.SteamAPI_ISteamApps_BIsTimedTrial
    ISteamApps_BIsTimedTrial.argtypes = [ POINTER(ISteamApps), POINTER(c_uint), POINTER(c_uint) ]
    ISteamApps_BIsTimedTrial.restype = c_bool

    global SteamApps_v008
    SteamApps_v008 = dll.SteamAPI_SteamApps_v008
    SteamApps_v008.argtypes = [ ]
    SteamApps_v008.restype = POINTER(ISteamApps)

    global ISteamNetworking_SendP2PPacket
    ISteamNetworking_SendP2PPacket = dll.SteamAPI_ISteamNetworking_SendP2PPacket
    ISteamNetworking_SendP2PPacket.argtypes = [ POINTER(ISteamNetworking), c_ulonglong, c_void_p, c_uint, EP2PSend, c_int ]
    ISteamNetworking_SendP2PPacket.restype = c_bool

    global ISteamNetworking_IsP2PPacketAvailable
    ISteamNetworking_IsP2PPacketAvailable = dll.SteamAPI_ISteamNetworking_IsP2PPacketAvailable
    ISteamNetworking_IsP2PPacketAvailable.argtypes = [ POINTER(ISteamNetworking), POINTER(c_uint), c_int ]
    ISteamNetworking_IsP2PPacketAvailable.restype = c_bool

    global ISteamNetworking_ReadP2PPacket
    ISteamNetworking_ReadP2PPacket = dll.SteamAPI_ISteamNetworking_ReadP2PPacket
    ISteamNetworking_ReadP2PPacket.argtypes = [ POINTER(ISteamNetworking), c_void_p, c_uint, POINTER(c_uint), POINTER(c_ulonglong), c_int ]
    ISteamNetworking_ReadP2PPacket.restype = c_bool

    global ISteamNetworking_AcceptP2PSessionWithUser
    ISteamNetworking_AcceptP2PSessionWithUser = dll.SteamAPI_ISteamNetworking_AcceptP2PSessionWithUser
    ISteamNetworking_AcceptP2PSessionWithUser.argtypes = [ POINTER(ISteamNetworking), c_ulonglong ]
    ISteamNetworking_AcceptP2PSessionWithUser.restype = c_bool

    global ISteamNetworking_CloseP2PSessionWithUser
    ISteamNetworking_CloseP2PSessionWithUser = dll.SteamAPI_ISteamNetworking_CloseP2PSessionWithUser
    ISteamNetworking_CloseP2PSessionWithUser.argtypes = [ POINTER(ISteamNetworking), c_ulonglong ]
    ISteamNetworking_CloseP2PSessionWithUser.restype = c_bool

    global ISteamNetworking_CloseP2PChannelWithUser
    ISteamNetworking_CloseP2PChannelWithUser = dll.SteamAPI_ISteamNetworking_CloseP2PChannelWithUser
    ISteamNetworking_CloseP2PChannelWithUser.argtypes = [ POINTER(ISteamNetworking), c_ulonglong, c_int ]
    ISteamNetworking_CloseP2PChannelWithUser.restype = c_bool

    global ISteamNetworking_GetP2PSessionState
    ISteamNetworking_GetP2PSessionState = dll.SteamAPI_ISteamNetworking_GetP2PSessionState
    ISteamNetworking_GetP2PSessionState.argtypes = [ POINTER(ISteamNetworking), c_ulonglong, POINTER(P2PSessionState_t) ]
    ISteamNetworking_GetP2PSessionState.restype = c_bool

    global ISteamNetworking_AllowP2PPacketRelay
    ISteamNetworking_AllowP2PPacketRelay = dll.SteamAPI_ISteamNetworking_AllowP2PPacketRelay
    ISteamNetworking_AllowP2PPacketRelay.argtypes = [ POINTER(ISteamNetworking), c_bool ]
    ISteamNetworking_AllowP2PPacketRelay.restype = c_bool

    global ISteamNetworking_CreateListenSocket
    ISteamNetworking_CreateListenSocket = dll.SteamAPI_ISteamNetworking_CreateListenSocket
    ISteamNetworking_CreateListenSocket.argtypes = [ POINTER(ISteamNetworking), c_int, SteamIPAddress_t, c_ushort, c_bool ]
    ISteamNetworking_CreateListenSocket.restype = c_uint

    global ISteamNetworking_CreateP2PConnectionSocket
    ISteamNetworking_CreateP2PConnectionSocket = dll.SteamAPI_ISteamNetworking_CreateP2PConnectionSocket
    ISteamNetworking_CreateP2PConnectionSocket.argtypes = [ POINTER(ISteamNetworking), c_ulonglong, c_int, c_int, c_bool ]
    ISteamNetworking_CreateP2PConnectionSocket.restype = c_uint

    global ISteamNetworking_CreateConnectionSocket
    ISteamNetworking_CreateConnectionSocket = dll.SteamAPI_ISteamNetworking_CreateConnectionSocket
    ISteamNetworking_CreateConnectionSocket.argtypes = [ POINTER(ISteamNetworking), SteamIPAddress_t, c_ushort, c_int ]
    ISteamNetworking_CreateConnectionSocket.restype = c_uint

    global ISteamNetworking_DestroySocket
    ISteamNetworking_DestroySocket = dll.SteamAPI_ISteamNetworking_DestroySocket
    ISteamNetworking_DestroySocket.argtypes = [ POINTER(ISteamNetworking), c_uint, c_bool ]
    ISteamNetworking_DestroySocket.restype = c_bool

    global ISteamNetworking_DestroyListenSocket
    ISteamNetworking_DestroyListenSocket = dll.SteamAPI_ISteamNetworking_DestroyListenSocket
    ISteamNetworking_DestroyListenSocket.argtypes = [ POINTER(ISteamNetworking), c_uint, c_bool ]
    ISteamNetworking_DestroyListenSocket.restype = c_bool

    global ISteamNetworking_SendDataOnSocket
    ISteamNetworking_SendDataOnSocket = dll.SteamAPI_ISteamNetworking_SendDataOnSocket
    ISteamNetworking_SendDataOnSocket.argtypes = [ POINTER(ISteamNetworking), c_uint, c_void_p, c_uint, c_bool ]
    ISteamNetworking_SendDataOnSocket.restype = c_bool

    global ISteamNetworking_IsDataAvailableOnSocket
    ISteamNetworking_IsDataAvailableOnSocket = dll.SteamAPI_ISteamNetworking_IsDataAvailableOnSocket
    ISteamNetworking_IsDataAvailableOnSocket.argtypes = [ POINTER(ISteamNetworking), c_uint, POINTER(c_uint) ]
    ISteamNetworking_IsDataAvailableOnSocket.restype = c_bool

    global ISteamNetworking_RetrieveDataFromSocket
    ISteamNetworking_RetrieveDataFromSocket = dll.SteamAPI_ISteamNetworking_RetrieveDataFromSocket
    ISteamNetworking_RetrieveDataFromSocket.argtypes = [ POINTER(ISteamNetworking), c_uint, c_void_p, c_uint, POINTER(c_uint) ]
    ISteamNetworking_RetrieveDataFromSocket.restype = c_bool

    global ISteamNetworking_IsDataAvailable
    ISteamNetworking_IsDataAvailable = dll.SteamAPI_ISteamNetworking_IsDataAvailable
    ISteamNetworking_IsDataAvailable.argtypes = [ POINTER(ISteamNetworking), c_uint, POINTER(c_uint), POINTER(c_uint) ]
    ISteamNetworking_IsDataAvailable.restype = c_bool

    global ISteamNetworking_RetrieveData
    ISteamNetworking_RetrieveData = dll.SteamAPI_ISteamNetworking_RetrieveData
    ISteamNetworking_RetrieveData.argtypes = [ POINTER(ISteamNetworking), c_uint, c_void_p, c_uint, POINTER(c_uint), POINTER(c_uint) ]
    ISteamNetworking_RetrieveData.restype = c_bool

    global ISteamNetworking_GetSocketInfo
    ISteamNetworking_GetSocketInfo = dll.SteamAPI_ISteamNetworking_GetSocketInfo
    ISteamNetworking_GetSocketInfo.argtypes = [ POINTER(ISteamNetworking), c_uint, POINTER(c_ulonglong), POINTER(c_int), POINTER(SteamIPAddress_t), POINTER(c_ushort) ]
    ISteamNetworking_GetSocketInfo.restype = c_bool

    global ISteamNetworking_GetListenSocketInfo
    ISteamNetworking_GetListenSocketInfo = dll.SteamAPI_ISteamNetworking_GetListenSocketInfo
    ISteamNetworking_GetListenSocketInfo.argtypes = [ POINTER(ISteamNetworking), c_uint, POINTER(SteamIPAddress_t), POINTER(c_ushort) ]
    ISteamNetworking_GetListenSocketInfo.restype = c_bool

    global ISteamNetworking_GetSocketConnectionType
    ISteamNetworking_GetSocketConnectionType = dll.SteamAPI_ISteamNetworking_GetSocketConnectionType
    ISteamNetworking_GetSocketConnectionType.argtypes = [ POINTER(ISteamNetworking), c_uint ]
    ISteamNetworking_GetSocketConnectionType.restype = ESNetSocketConnectionType

    global ISteamNetworking_GetMaxPacketSize
    ISteamNetworking_GetMaxPacketSize = dll.SteamAPI_ISteamNetworking_GetMaxPacketSize
    ISteamNetworking_GetMaxPacketSize.argtypes = [ POINTER(ISteamNetworking), c_uint ]
    ISteamNetworking_GetMaxPacketSize.restype = c_int

    global SteamNetworking_v006
    SteamNetworking_v006 = dll.SteamAPI_SteamNetworking_v006
    SteamNetworking_v006.argtypes = [ ]
    SteamNetworking_v006.restype = POINTER(ISteamNetworking)

    global SteamGameServerNetworking_v006
    SteamGameServerNetworking_v006 = dll.SteamAPI_SteamGameServerNetworking_v006
    SteamGameServerNetworking_v006.argtypes = [ ]
    SteamGameServerNetworking_v006.restype = POINTER(ISteamNetworking)

    global ISteamScreenshots_WriteScreenshot
    ISteamScreenshots_WriteScreenshot = dll.SteamAPI_ISteamScreenshots_WriteScreenshot
    ISteamScreenshots_WriteScreenshot.argtypes = [ POINTER(ISteamScreenshots), c_void_p, c_uint, c_int, c_int ]
    ISteamScreenshots_WriteScreenshot.restype = c_uint

    global ISteamScreenshots_AddScreenshotToLibrary
    ISteamScreenshots_AddScreenshotToLibrary = dll.SteamAPI_ISteamScreenshots_AddScreenshotToLibrary
    ISteamScreenshots_AddScreenshotToLibrary.argtypes = [ POINTER(ISteamScreenshots), c_char_p, c_char_p, c_int, c_int ]
    ISteamScreenshots_AddScreenshotToLibrary.restype = c_uint

    global ISteamScreenshots_TriggerScreenshot
    ISteamScreenshots_TriggerScreenshot = dll.SteamAPI_ISteamScreenshots_TriggerScreenshot
    ISteamScreenshots_TriggerScreenshot.argtypes = [ POINTER(ISteamScreenshots),  ]
    ISteamScreenshots_TriggerScreenshot.restype = None

    global ISteamScreenshots_HookScreenshots
    ISteamScreenshots_HookScreenshots = dll.SteamAPI_ISteamScreenshots_HookScreenshots
    ISteamScreenshots_HookScreenshots.argtypes = [ POINTER(ISteamScreenshots), c_bool ]
    ISteamScreenshots_HookScreenshots.restype = None

    global ISteamScreenshots_SetLocation
    ISteamScreenshots_SetLocation = dll.SteamAPI_ISteamScreenshots_SetLocation
    ISteamScreenshots_SetLocation.argtypes = [ POINTER(ISteamScreenshots), c_uint, c_char_p ]
    ISteamScreenshots_SetLocation.restype = c_bool

    global ISteamScreenshots_TagUser
    ISteamScreenshots_TagUser = dll.SteamAPI_ISteamScreenshots_TagUser
    ISteamScreenshots_TagUser.argtypes = [ POINTER(ISteamScreenshots), c_uint, c_ulonglong ]
    ISteamScreenshots_TagUser.restype = c_bool

    global ISteamScreenshots_TagPublishedFile
    ISteamScreenshots_TagPublishedFile = dll.SteamAPI_ISteamScreenshots_TagPublishedFile
    ISteamScreenshots_TagPublishedFile.argtypes = [ POINTER(ISteamScreenshots), c_uint, c_ulonglong ]
    ISteamScreenshots_TagPublishedFile.restype = c_bool

    global ISteamScreenshots_IsScreenshotsHooked
    ISteamScreenshots_IsScreenshotsHooked = dll.SteamAPI_ISteamScreenshots_IsScreenshotsHooked
    ISteamScreenshots_IsScreenshotsHooked.argtypes = [ POINTER(ISteamScreenshots),  ]
    ISteamScreenshots_IsScreenshotsHooked.restype = c_bool

    global ISteamScreenshots_AddVRScreenshotToLibrary
    ISteamScreenshots_AddVRScreenshotToLibrary = dll.SteamAPI_ISteamScreenshots_AddVRScreenshotToLibrary
    ISteamScreenshots_AddVRScreenshotToLibrary.argtypes = [ POINTER(ISteamScreenshots), EVRScreenshotType, c_char_p, c_char_p ]
    ISteamScreenshots_AddVRScreenshotToLibrary.restype = c_uint

    global SteamScreenshots_v003
    SteamScreenshots_v003 = dll.SteamAPI_SteamScreenshots_v003
    SteamScreenshots_v003.argtypes = [ ]
    SteamScreenshots_v003.restype = POINTER(ISteamScreenshots)

    global ISteamMusic_BIsEnabled
    ISteamMusic_BIsEnabled = dll.SteamAPI_ISteamMusic_BIsEnabled
    ISteamMusic_BIsEnabled.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_BIsEnabled.restype = c_bool

    global ISteamMusic_BIsPlaying
    ISteamMusic_BIsPlaying = dll.SteamAPI_ISteamMusic_BIsPlaying
    ISteamMusic_BIsPlaying.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_BIsPlaying.restype = c_bool

    global ISteamMusic_GetPlaybackStatus
    ISteamMusic_GetPlaybackStatus = dll.SteamAPI_ISteamMusic_GetPlaybackStatus
    ISteamMusic_GetPlaybackStatus.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_GetPlaybackStatus.restype = AudioPlayback_Status

    global ISteamMusic_Play
    ISteamMusic_Play = dll.SteamAPI_ISteamMusic_Play
    ISteamMusic_Play.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_Play.restype = None

    global ISteamMusic_Pause
    ISteamMusic_Pause = dll.SteamAPI_ISteamMusic_Pause
    ISteamMusic_Pause.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_Pause.restype = None

    global ISteamMusic_PlayPrevious
    ISteamMusic_PlayPrevious = dll.SteamAPI_ISteamMusic_PlayPrevious
    ISteamMusic_PlayPrevious.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_PlayPrevious.restype = None

    global ISteamMusic_PlayNext
    ISteamMusic_PlayNext = dll.SteamAPI_ISteamMusic_PlayNext
    ISteamMusic_PlayNext.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_PlayNext.restype = None

    global ISteamMusic_SetVolume
    ISteamMusic_SetVolume = dll.SteamAPI_ISteamMusic_SetVolume
    ISteamMusic_SetVolume.argtypes = [ POINTER(ISteamMusic), c_float ]
    ISteamMusic_SetVolume.restype = None

    global ISteamMusic_GetVolume
    ISteamMusic_GetVolume = dll.SteamAPI_ISteamMusic_GetVolume
    ISteamMusic_GetVolume.argtypes = [ POINTER(ISteamMusic),  ]
    ISteamMusic_GetVolume.restype = c_float

    global SteamMusic_v001
    SteamMusic_v001 = dll.SteamAPI_SteamMusic_v001
    SteamMusic_v001.argtypes = [ ]
    SteamMusic_v001.restype = POINTER(ISteamMusic)

    global ISteamMusicRemote_RegisterSteamMusicRemote
    ISteamMusicRemote_RegisterSteamMusicRemote = dll.SteamAPI_ISteamMusicRemote_RegisterSteamMusicRemote
    ISteamMusicRemote_RegisterSteamMusicRemote.argtypes = [ POINTER(ISteamMusicRemote), c_char_p ]
    ISteamMusicRemote_RegisterSteamMusicRemote.restype = c_bool

    global ISteamMusicRemote_DeregisterSteamMusicRemote
    ISteamMusicRemote_DeregisterSteamMusicRemote = dll.SteamAPI_ISteamMusicRemote_DeregisterSteamMusicRemote
    ISteamMusicRemote_DeregisterSteamMusicRemote.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_DeregisterSteamMusicRemote.restype = c_bool

    global ISteamMusicRemote_BIsCurrentMusicRemote
    ISteamMusicRemote_BIsCurrentMusicRemote = dll.SteamAPI_ISteamMusicRemote_BIsCurrentMusicRemote
    ISteamMusicRemote_BIsCurrentMusicRemote.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_BIsCurrentMusicRemote.restype = c_bool

    global ISteamMusicRemote_BActivationSuccess
    ISteamMusicRemote_BActivationSuccess = dll.SteamAPI_ISteamMusicRemote_BActivationSuccess
    ISteamMusicRemote_BActivationSuccess.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_BActivationSuccess.restype = c_bool

    global ISteamMusicRemote_SetDisplayName
    ISteamMusicRemote_SetDisplayName = dll.SteamAPI_ISteamMusicRemote_SetDisplayName
    ISteamMusicRemote_SetDisplayName.argtypes = [ POINTER(ISteamMusicRemote), c_char_p ]
    ISteamMusicRemote_SetDisplayName.restype = c_bool

    global ISteamMusicRemote_SetPNGIcon_64x64
    ISteamMusicRemote_SetPNGIcon_64x64 = dll.SteamAPI_ISteamMusicRemote_SetPNGIcon_64x64
    ISteamMusicRemote_SetPNGIcon_64x64.argtypes = [ POINTER(ISteamMusicRemote), c_void_p, c_uint ]
    ISteamMusicRemote_SetPNGIcon_64x64.restype = c_bool

    global ISteamMusicRemote_EnablePlayPrevious
    ISteamMusicRemote_EnablePlayPrevious = dll.SteamAPI_ISteamMusicRemote_EnablePlayPrevious
    ISteamMusicRemote_EnablePlayPrevious.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnablePlayPrevious.restype = c_bool

    global ISteamMusicRemote_EnablePlayNext
    ISteamMusicRemote_EnablePlayNext = dll.SteamAPI_ISteamMusicRemote_EnablePlayNext
    ISteamMusicRemote_EnablePlayNext.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnablePlayNext.restype = c_bool

    global ISteamMusicRemote_EnableShuffled
    ISteamMusicRemote_EnableShuffled = dll.SteamAPI_ISteamMusicRemote_EnableShuffled
    ISteamMusicRemote_EnableShuffled.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnableShuffled.restype = c_bool

    global ISteamMusicRemote_EnableLooped
    ISteamMusicRemote_EnableLooped = dll.SteamAPI_ISteamMusicRemote_EnableLooped
    ISteamMusicRemote_EnableLooped.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnableLooped.restype = c_bool

    global ISteamMusicRemote_EnableQueue
    ISteamMusicRemote_EnableQueue = dll.SteamAPI_ISteamMusicRemote_EnableQueue
    ISteamMusicRemote_EnableQueue.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnableQueue.restype = c_bool

    global ISteamMusicRemote_EnablePlaylists
    ISteamMusicRemote_EnablePlaylists = dll.SteamAPI_ISteamMusicRemote_EnablePlaylists
    ISteamMusicRemote_EnablePlaylists.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_EnablePlaylists.restype = c_bool

    global ISteamMusicRemote_UpdatePlaybackStatus
    ISteamMusicRemote_UpdatePlaybackStatus = dll.SteamAPI_ISteamMusicRemote_UpdatePlaybackStatus
    ISteamMusicRemote_UpdatePlaybackStatus.argtypes = [ POINTER(ISteamMusicRemote), AudioPlayback_Status ]
    ISteamMusicRemote_UpdatePlaybackStatus.restype = c_bool

    global ISteamMusicRemote_UpdateShuffled
    ISteamMusicRemote_UpdateShuffled = dll.SteamAPI_ISteamMusicRemote_UpdateShuffled
    ISteamMusicRemote_UpdateShuffled.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_UpdateShuffled.restype = c_bool

    global ISteamMusicRemote_UpdateLooped
    ISteamMusicRemote_UpdateLooped = dll.SteamAPI_ISteamMusicRemote_UpdateLooped
    ISteamMusicRemote_UpdateLooped.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_UpdateLooped.restype = c_bool

    global ISteamMusicRemote_UpdateVolume
    ISteamMusicRemote_UpdateVolume = dll.SteamAPI_ISteamMusicRemote_UpdateVolume
    ISteamMusicRemote_UpdateVolume.argtypes = [ POINTER(ISteamMusicRemote), c_float ]
    ISteamMusicRemote_UpdateVolume.restype = c_bool

    global ISteamMusicRemote_CurrentEntryWillChange
    ISteamMusicRemote_CurrentEntryWillChange = dll.SteamAPI_ISteamMusicRemote_CurrentEntryWillChange
    ISteamMusicRemote_CurrentEntryWillChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_CurrentEntryWillChange.restype = c_bool

    global ISteamMusicRemote_CurrentEntryIsAvailable
    ISteamMusicRemote_CurrentEntryIsAvailable = dll.SteamAPI_ISteamMusicRemote_CurrentEntryIsAvailable
    ISteamMusicRemote_CurrentEntryIsAvailable.argtypes = [ POINTER(ISteamMusicRemote), c_bool ]
    ISteamMusicRemote_CurrentEntryIsAvailable.restype = c_bool

    global ISteamMusicRemote_UpdateCurrentEntryText
    ISteamMusicRemote_UpdateCurrentEntryText = dll.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryText
    ISteamMusicRemote_UpdateCurrentEntryText.argtypes = [ POINTER(ISteamMusicRemote), c_char_p ]
    ISteamMusicRemote_UpdateCurrentEntryText.restype = c_bool

    global ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds
    ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds = dll.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds
    ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds.argtypes = [ POINTER(ISteamMusicRemote), c_int ]
    ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds.restype = c_bool

    global ISteamMusicRemote_UpdateCurrentEntryCoverArt
    ISteamMusicRemote_UpdateCurrentEntryCoverArt = dll.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryCoverArt
    ISteamMusicRemote_UpdateCurrentEntryCoverArt.argtypes = [ POINTER(ISteamMusicRemote), c_void_p, c_uint ]
    ISteamMusicRemote_UpdateCurrentEntryCoverArt.restype = c_bool

    global ISteamMusicRemote_CurrentEntryDidChange
    ISteamMusicRemote_CurrentEntryDidChange = dll.SteamAPI_ISteamMusicRemote_CurrentEntryDidChange
    ISteamMusicRemote_CurrentEntryDidChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_CurrentEntryDidChange.restype = c_bool

    global ISteamMusicRemote_QueueWillChange
    ISteamMusicRemote_QueueWillChange = dll.SteamAPI_ISteamMusicRemote_QueueWillChange
    ISteamMusicRemote_QueueWillChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_QueueWillChange.restype = c_bool

    global ISteamMusicRemote_ResetQueueEntries
    ISteamMusicRemote_ResetQueueEntries = dll.SteamAPI_ISteamMusicRemote_ResetQueueEntries
    ISteamMusicRemote_ResetQueueEntries.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_ResetQueueEntries.restype = c_bool

    global ISteamMusicRemote_SetQueueEntry
    ISteamMusicRemote_SetQueueEntry = dll.SteamAPI_ISteamMusicRemote_SetQueueEntry
    ISteamMusicRemote_SetQueueEntry.argtypes = [ POINTER(ISteamMusicRemote), c_int, c_int, c_char_p ]
    ISteamMusicRemote_SetQueueEntry.restype = c_bool

    global ISteamMusicRemote_SetCurrentQueueEntry
    ISteamMusicRemote_SetCurrentQueueEntry = dll.SteamAPI_ISteamMusicRemote_SetCurrentQueueEntry
    ISteamMusicRemote_SetCurrentQueueEntry.argtypes = [ POINTER(ISteamMusicRemote), c_int ]
    ISteamMusicRemote_SetCurrentQueueEntry.restype = c_bool

    global ISteamMusicRemote_QueueDidChange
    ISteamMusicRemote_QueueDidChange = dll.SteamAPI_ISteamMusicRemote_QueueDidChange
    ISteamMusicRemote_QueueDidChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_QueueDidChange.restype = c_bool

    global ISteamMusicRemote_PlaylistWillChange
    ISteamMusicRemote_PlaylistWillChange = dll.SteamAPI_ISteamMusicRemote_PlaylistWillChange
    ISteamMusicRemote_PlaylistWillChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_PlaylistWillChange.restype = c_bool

    global ISteamMusicRemote_ResetPlaylistEntries
    ISteamMusicRemote_ResetPlaylistEntries = dll.SteamAPI_ISteamMusicRemote_ResetPlaylistEntries
    ISteamMusicRemote_ResetPlaylistEntries.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_ResetPlaylistEntries.restype = c_bool

    global ISteamMusicRemote_SetPlaylistEntry
    ISteamMusicRemote_SetPlaylistEntry = dll.SteamAPI_ISteamMusicRemote_SetPlaylistEntry
    ISteamMusicRemote_SetPlaylistEntry.argtypes = [ POINTER(ISteamMusicRemote), c_int, c_int, c_char_p ]
    ISteamMusicRemote_SetPlaylistEntry.restype = c_bool

    global ISteamMusicRemote_SetCurrentPlaylistEntry
    ISteamMusicRemote_SetCurrentPlaylistEntry = dll.SteamAPI_ISteamMusicRemote_SetCurrentPlaylistEntry
    ISteamMusicRemote_SetCurrentPlaylistEntry.argtypes = [ POINTER(ISteamMusicRemote), c_int ]
    ISteamMusicRemote_SetCurrentPlaylistEntry.restype = c_bool

    global ISteamMusicRemote_PlaylistDidChange
    ISteamMusicRemote_PlaylistDidChange = dll.SteamAPI_ISteamMusicRemote_PlaylistDidChange
    ISteamMusicRemote_PlaylistDidChange.argtypes = [ POINTER(ISteamMusicRemote),  ]
    ISteamMusicRemote_PlaylistDidChange.restype = c_bool

    global SteamMusicRemote_v001
    SteamMusicRemote_v001 = dll.SteamAPI_SteamMusicRemote_v001
    SteamMusicRemote_v001.argtypes = [ ]
    SteamMusicRemote_v001.restype = POINTER(ISteamMusicRemote)

    global ISteamHTTP_CreateHTTPRequest
    ISteamHTTP_CreateHTTPRequest = dll.SteamAPI_ISteamHTTP_CreateHTTPRequest
    ISteamHTTP_CreateHTTPRequest.argtypes = [ POINTER(ISteamHTTP), EHTTPMethod, c_char_p ]
    ISteamHTTP_CreateHTTPRequest.restype = c_uint

    global ISteamHTTP_SetHTTPRequestContextValue
    ISteamHTTP_SetHTTPRequestContextValue = dll.SteamAPI_ISteamHTTP_SetHTTPRequestContextValue
    ISteamHTTP_SetHTTPRequestContextValue.argtypes = [ POINTER(ISteamHTTP), c_uint, c_ulonglong ]
    ISteamHTTP_SetHTTPRequestContextValue.restype = c_bool

    global ISteamHTTP_SetHTTPRequestNetworkActivityTimeout
    ISteamHTTP_SetHTTPRequestNetworkActivityTimeout = dll.SteamAPI_ISteamHTTP_SetHTTPRequestNetworkActivityTimeout
    ISteamHTTP_SetHTTPRequestNetworkActivityTimeout.argtypes = [ POINTER(ISteamHTTP), c_uint, c_uint ]
    ISteamHTTP_SetHTTPRequestNetworkActivityTimeout.restype = c_bool

    global ISteamHTTP_SetHTTPRequestHeaderValue
    ISteamHTTP_SetHTTPRequestHeaderValue = dll.SteamAPI_ISteamHTTP_SetHTTPRequestHeaderValue
    ISteamHTTP_SetHTTPRequestHeaderValue.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, c_char_p ]
    ISteamHTTP_SetHTTPRequestHeaderValue.restype = c_bool

    global ISteamHTTP_SetHTTPRequestGetOrPostParameter
    ISteamHTTP_SetHTTPRequestGetOrPostParameter = dll.SteamAPI_ISteamHTTP_SetHTTPRequestGetOrPostParameter
    ISteamHTTP_SetHTTPRequestGetOrPostParameter.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, c_char_p ]
    ISteamHTTP_SetHTTPRequestGetOrPostParameter.restype = c_bool

    global ISteamHTTP_SendHTTPRequest
    ISteamHTTP_SendHTTPRequest = dll.SteamAPI_ISteamHTTP_SendHTTPRequest
    ISteamHTTP_SendHTTPRequest.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_ulonglong) ]
    ISteamHTTP_SendHTTPRequest.restype = c_bool

    global ISteamHTTP_SendHTTPRequestAndStreamResponse
    ISteamHTTP_SendHTTPRequestAndStreamResponse = dll.SteamAPI_ISteamHTTP_SendHTTPRequestAndStreamResponse
    ISteamHTTP_SendHTTPRequestAndStreamResponse.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_ulonglong) ]
    ISteamHTTP_SendHTTPRequestAndStreamResponse.restype = c_bool

    global ISteamHTTP_DeferHTTPRequest
    ISteamHTTP_DeferHTTPRequest = dll.SteamAPI_ISteamHTTP_DeferHTTPRequest
    ISteamHTTP_DeferHTTPRequest.argtypes = [ POINTER(ISteamHTTP), c_uint ]
    ISteamHTTP_DeferHTTPRequest.restype = c_bool

    global ISteamHTTP_PrioritizeHTTPRequest
    ISteamHTTP_PrioritizeHTTPRequest = dll.SteamAPI_ISteamHTTP_PrioritizeHTTPRequest
    ISteamHTTP_PrioritizeHTTPRequest.argtypes = [ POINTER(ISteamHTTP), c_uint ]
    ISteamHTTP_PrioritizeHTTPRequest.restype = c_bool

    global ISteamHTTP_GetHTTPResponseHeaderSize
    ISteamHTTP_GetHTTPResponseHeaderSize = dll.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderSize
    ISteamHTTP_GetHTTPResponseHeaderSize.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, POINTER(c_uint) ]
    ISteamHTTP_GetHTTPResponseHeaderSize.restype = c_bool

    global ISteamHTTP_GetHTTPResponseHeaderValue
    ISteamHTTP_GetHTTPResponseHeaderValue = dll.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderValue
    ISteamHTTP_GetHTTPResponseHeaderValue.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, POINTER(c_ubyte), c_uint ]
    ISteamHTTP_GetHTTPResponseHeaderValue.restype = c_bool

    global ISteamHTTP_GetHTTPResponseBodySize
    ISteamHTTP_GetHTTPResponseBodySize = dll.SteamAPI_ISteamHTTP_GetHTTPResponseBodySize
    ISteamHTTP_GetHTTPResponseBodySize.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_uint) ]
    ISteamHTTP_GetHTTPResponseBodySize.restype = c_bool

    global ISteamHTTP_GetHTTPResponseBodyData
    ISteamHTTP_GetHTTPResponseBodyData = dll.SteamAPI_ISteamHTTP_GetHTTPResponseBodyData
    ISteamHTTP_GetHTTPResponseBodyData.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_ubyte), c_uint ]
    ISteamHTTP_GetHTTPResponseBodyData.restype = c_bool

    global ISteamHTTP_GetHTTPStreamingResponseBodyData
    ISteamHTTP_GetHTTPStreamingResponseBodyData = dll.SteamAPI_ISteamHTTP_GetHTTPStreamingResponseBodyData
    ISteamHTTP_GetHTTPStreamingResponseBodyData.argtypes = [ POINTER(ISteamHTTP), c_uint, c_uint, POINTER(c_ubyte), c_uint ]
    ISteamHTTP_GetHTTPStreamingResponseBodyData.restype = c_bool

    global ISteamHTTP_ReleaseHTTPRequest
    ISteamHTTP_ReleaseHTTPRequest = dll.SteamAPI_ISteamHTTP_ReleaseHTTPRequest
    ISteamHTTP_ReleaseHTTPRequest.argtypes = [ POINTER(ISteamHTTP), c_uint ]
    ISteamHTTP_ReleaseHTTPRequest.restype = c_bool

    global ISteamHTTP_GetHTTPDownloadProgressPct
    ISteamHTTP_GetHTTPDownloadProgressPct = dll.SteamAPI_ISteamHTTP_GetHTTPDownloadProgressPct
    ISteamHTTP_GetHTTPDownloadProgressPct.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_float) ]
    ISteamHTTP_GetHTTPDownloadProgressPct.restype = c_bool

    global ISteamHTTP_SetHTTPRequestRawPostBody
    ISteamHTTP_SetHTTPRequestRawPostBody = dll.SteamAPI_ISteamHTTP_SetHTTPRequestRawPostBody
    ISteamHTTP_SetHTTPRequestRawPostBody.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, POINTER(c_ubyte), c_uint ]
    ISteamHTTP_SetHTTPRequestRawPostBody.restype = c_bool

    global ISteamHTTP_CreateCookieContainer
    ISteamHTTP_CreateCookieContainer = dll.SteamAPI_ISteamHTTP_CreateCookieContainer
    ISteamHTTP_CreateCookieContainer.argtypes = [ POINTER(ISteamHTTP), c_bool ]
    ISteamHTTP_CreateCookieContainer.restype = c_uint

    global ISteamHTTP_ReleaseCookieContainer
    ISteamHTTP_ReleaseCookieContainer = dll.SteamAPI_ISteamHTTP_ReleaseCookieContainer
    ISteamHTTP_ReleaseCookieContainer.argtypes = [ POINTER(ISteamHTTP), c_uint ]
    ISteamHTTP_ReleaseCookieContainer.restype = c_bool

    global ISteamHTTP_SetCookie
    ISteamHTTP_SetCookie = dll.SteamAPI_ISteamHTTP_SetCookie
    ISteamHTTP_SetCookie.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p, c_char_p, c_char_p ]
    ISteamHTTP_SetCookie.restype = c_bool

    global ISteamHTTP_SetHTTPRequestCookieContainer
    ISteamHTTP_SetHTTPRequestCookieContainer = dll.SteamAPI_ISteamHTTP_SetHTTPRequestCookieContainer
    ISteamHTTP_SetHTTPRequestCookieContainer.argtypes = [ POINTER(ISteamHTTP), c_uint, c_uint ]
    ISteamHTTP_SetHTTPRequestCookieContainer.restype = c_bool

    global ISteamHTTP_SetHTTPRequestUserAgentInfo
    ISteamHTTP_SetHTTPRequestUserAgentInfo = dll.SteamAPI_ISteamHTTP_SetHTTPRequestUserAgentInfo
    ISteamHTTP_SetHTTPRequestUserAgentInfo.argtypes = [ POINTER(ISteamHTTP), c_uint, c_char_p ]
    ISteamHTTP_SetHTTPRequestUserAgentInfo.restype = c_bool

    global ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate
    ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate = dll.SteamAPI_ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate
    ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate.argtypes = [ POINTER(ISteamHTTP), c_uint, c_bool ]
    ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate.restype = c_bool

    global ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS
    ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS = dll.SteamAPI_ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS
    ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS.argtypes = [ POINTER(ISteamHTTP), c_uint, c_uint ]
    ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS.restype = c_bool

    global ISteamHTTP_GetHTTPRequestWasTimedOut
    ISteamHTTP_GetHTTPRequestWasTimedOut = dll.SteamAPI_ISteamHTTP_GetHTTPRequestWasTimedOut
    ISteamHTTP_GetHTTPRequestWasTimedOut.argtypes = [ POINTER(ISteamHTTP), c_uint, POINTER(c_bool) ]
    ISteamHTTP_GetHTTPRequestWasTimedOut.restype = c_bool

    global SteamHTTP_v003
    SteamHTTP_v003 = dll.SteamAPI_SteamHTTP_v003
    SteamHTTP_v003.argtypes = [ ]
    SteamHTTP_v003.restype = POINTER(ISteamHTTP)

    global SteamGameServerHTTP_v003
    SteamGameServerHTTP_v003 = dll.SteamAPI_SteamGameServerHTTP_v003
    SteamGameServerHTTP_v003.argtypes = [ ]
    SteamGameServerHTTP_v003.restype = POINTER(ISteamHTTP)

    global ISteamInput_Init
    ISteamInput_Init = dll.SteamAPI_ISteamInput_Init
    ISteamInput_Init.argtypes = [ POINTER(ISteamInput), c_bool ]
    ISteamInput_Init.restype = c_bool

    global ISteamInput_Shutdown
    ISteamInput_Shutdown = dll.SteamAPI_ISteamInput_Shutdown
    ISteamInput_Shutdown.argtypes = [ POINTER(ISteamInput),  ]
    ISteamInput_Shutdown.restype = c_bool

    global ISteamInput_SetInputActionManifestFilePath
    ISteamInput_SetInputActionManifestFilePath = dll.SteamAPI_ISteamInput_SetInputActionManifestFilePath
    ISteamInput_SetInputActionManifestFilePath.argtypes = [ POINTER(ISteamInput), c_char_p ]
    ISteamInput_SetInputActionManifestFilePath.restype = c_bool

    global ISteamInput_RunFrame
    ISteamInput_RunFrame = dll.SteamAPI_ISteamInput_RunFrame
    ISteamInput_RunFrame.argtypes = [ POINTER(ISteamInput), c_bool ]
    ISteamInput_RunFrame.restype = None

    global ISteamInput_BWaitForData
    ISteamInput_BWaitForData = dll.SteamAPI_ISteamInput_BWaitForData
    ISteamInput_BWaitForData.argtypes = [ POINTER(ISteamInput), c_bool, c_uint ]
    ISteamInput_BWaitForData.restype = c_bool

    global ISteamInput_BNewDataAvailable
    ISteamInput_BNewDataAvailable = dll.SteamAPI_ISteamInput_BNewDataAvailable
    ISteamInput_BNewDataAvailable.argtypes = [ POINTER(ISteamInput),  ]
    ISteamInput_BNewDataAvailable.restype = c_bool

    global ISteamInput_GetConnectedControllers
    ISteamInput_GetConnectedControllers = dll.SteamAPI_ISteamInput_GetConnectedControllers
    ISteamInput_GetConnectedControllers.argtypes = [ POINTER(ISteamInput), POINTER(c_ulonglong) ]
    ISteamInput_GetConnectedControllers.restype = c_int

    global ISteamInput_EnableDeviceCallbacks
    ISteamInput_EnableDeviceCallbacks = dll.SteamAPI_ISteamInput_EnableDeviceCallbacks
    ISteamInput_EnableDeviceCallbacks.argtypes = [ POINTER(ISteamInput),  ]
    ISteamInput_EnableDeviceCallbacks.restype = None

    global ISteamInput_EnableActionEventCallbacks
    ISteamInput_EnableActionEventCallbacks = dll.SteamAPI_ISteamInput_EnableActionEventCallbacks
    ISteamInput_EnableActionEventCallbacks.argtypes = [ POINTER(ISteamInput), c_void_p ]
    ISteamInput_EnableActionEventCallbacks.restype = None

    global ISteamInput_GetActionSetHandle
    ISteamInput_GetActionSetHandle = dll.SteamAPI_ISteamInput_GetActionSetHandle
    ISteamInput_GetActionSetHandle.argtypes = [ POINTER(ISteamInput), c_char_p ]
    ISteamInput_GetActionSetHandle.restype = c_ulonglong

    global ISteamInput_ActivateActionSet
    ISteamInput_ActivateActionSet = dll.SteamAPI_ISteamInput_ActivateActionSet
    ISteamInput_ActivateActionSet.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_ActivateActionSet.restype = None

    global ISteamInput_GetCurrentActionSet
    ISteamInput_GetCurrentActionSet = dll.SteamAPI_ISteamInput_GetCurrentActionSet
    ISteamInput_GetCurrentActionSet.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetCurrentActionSet.restype = c_ulonglong

    global ISteamInput_ActivateActionSetLayer
    ISteamInput_ActivateActionSetLayer = dll.SteamAPI_ISteamInput_ActivateActionSetLayer
    ISteamInput_ActivateActionSetLayer.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_ActivateActionSetLayer.restype = None

    global ISteamInput_DeactivateActionSetLayer
    ISteamInput_DeactivateActionSetLayer = dll.SteamAPI_ISteamInput_DeactivateActionSetLayer
    ISteamInput_DeactivateActionSetLayer.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_DeactivateActionSetLayer.restype = None

    global ISteamInput_DeactivateAllActionSetLayers
    ISteamInput_DeactivateAllActionSetLayers = dll.SteamAPI_ISteamInput_DeactivateAllActionSetLayers
    ISteamInput_DeactivateAllActionSetLayers.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_DeactivateAllActionSetLayers.restype = None

    global ISteamInput_GetActiveActionSetLayers
    ISteamInput_GetActiveActionSetLayers = dll.SteamAPI_ISteamInput_GetActiveActionSetLayers
    ISteamInput_GetActiveActionSetLayers.argtypes = [ POINTER(ISteamInput), c_ulonglong, POINTER(c_ulonglong) ]
    ISteamInput_GetActiveActionSetLayers.restype = c_int

    global ISteamInput_GetDigitalActionHandle
    ISteamInput_GetDigitalActionHandle = dll.SteamAPI_ISteamInput_GetDigitalActionHandle
    ISteamInput_GetDigitalActionHandle.argtypes = [ POINTER(ISteamInput), c_char_p ]
    ISteamInput_GetDigitalActionHandle.restype = c_ulonglong

    global ISteamInput_GetDigitalActionData
    ISteamInput_GetDigitalActionData = dll.SteamAPI_ISteamInput_GetDigitalActionData
    ISteamInput_GetDigitalActionData.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_GetDigitalActionData.restype = InputDigitalActionData_t

    global ISteamInput_GetDigitalActionOrigins
    ISteamInput_GetDigitalActionOrigins = dll.SteamAPI_ISteamInput_GetDigitalActionOrigins
    ISteamInput_GetDigitalActionOrigins.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong, c_ulonglong, POINTER(EInputActionOrigin) ]
    ISteamInput_GetDigitalActionOrigins.restype = c_int

    global ISteamInput_GetStringForDigitalActionName
    ISteamInput_GetStringForDigitalActionName = dll.SteamAPI_ISteamInput_GetStringForDigitalActionName
    ISteamInput_GetStringForDigitalActionName.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetStringForDigitalActionName.restype = c_char_p

    global ISteamInput_GetAnalogActionHandle
    ISteamInput_GetAnalogActionHandle = dll.SteamAPI_ISteamInput_GetAnalogActionHandle
    ISteamInput_GetAnalogActionHandle.argtypes = [ POINTER(ISteamInput), c_char_p ]
    ISteamInput_GetAnalogActionHandle.restype = c_ulonglong

    global ISteamInput_GetAnalogActionData
    ISteamInput_GetAnalogActionData = dll.SteamAPI_ISteamInput_GetAnalogActionData
    ISteamInput_GetAnalogActionData.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_GetAnalogActionData.restype = InputAnalogActionData_t

    global ISteamInput_GetAnalogActionOrigins
    ISteamInput_GetAnalogActionOrigins = dll.SteamAPI_ISteamInput_GetAnalogActionOrigins
    ISteamInput_GetAnalogActionOrigins.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong, c_ulonglong, POINTER(EInputActionOrigin) ]
    ISteamInput_GetAnalogActionOrigins.restype = c_int

    global ISteamInput_GetGlyphPNGForActionOrigin
    ISteamInput_GetGlyphPNGForActionOrigin = dll.SteamAPI_ISteamInput_GetGlyphPNGForActionOrigin
    ISteamInput_GetGlyphPNGForActionOrigin.argtypes = [ POINTER(ISteamInput), EInputActionOrigin, ESteamInputGlyphSize, c_uint ]
    ISteamInput_GetGlyphPNGForActionOrigin.restype = c_char_p

    global ISteamInput_GetGlyphSVGForActionOrigin
    ISteamInput_GetGlyphSVGForActionOrigin = dll.SteamAPI_ISteamInput_GetGlyphSVGForActionOrigin
    ISteamInput_GetGlyphSVGForActionOrigin.argtypes = [ POINTER(ISteamInput), EInputActionOrigin, c_uint ]
    ISteamInput_GetGlyphSVGForActionOrigin.restype = c_char_p

    global ISteamInput_GetGlyphForActionOrigin_Legacy
    ISteamInput_GetGlyphForActionOrigin_Legacy = dll.SteamAPI_ISteamInput_GetGlyphForActionOrigin_Legacy
    ISteamInput_GetGlyphForActionOrigin_Legacy.argtypes = [ POINTER(ISteamInput), EInputActionOrigin ]
    ISteamInput_GetGlyphForActionOrigin_Legacy.restype = c_char_p

    global ISteamInput_GetStringForActionOrigin
    ISteamInput_GetStringForActionOrigin = dll.SteamAPI_ISteamInput_GetStringForActionOrigin
    ISteamInput_GetStringForActionOrigin.argtypes = [ POINTER(ISteamInput), EInputActionOrigin ]
    ISteamInput_GetStringForActionOrigin.restype = c_char_p

    global ISteamInput_GetStringForAnalogActionName
    ISteamInput_GetStringForAnalogActionName = dll.SteamAPI_ISteamInput_GetStringForAnalogActionName
    ISteamInput_GetStringForAnalogActionName.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetStringForAnalogActionName.restype = c_char_p

    global ISteamInput_StopAnalogActionMomentum
    ISteamInput_StopAnalogActionMomentum = dll.SteamAPI_ISteamInput_StopAnalogActionMomentum
    ISteamInput_StopAnalogActionMomentum.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ulonglong ]
    ISteamInput_StopAnalogActionMomentum.restype = None

    global ISteamInput_GetMotionData
    ISteamInput_GetMotionData = dll.SteamAPI_ISteamInput_GetMotionData
    ISteamInput_GetMotionData.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetMotionData.restype = InputMotionData_t

    global ISteamInput_TriggerVibration
    ISteamInput_TriggerVibration = dll.SteamAPI_ISteamInput_TriggerVibration
    ISteamInput_TriggerVibration.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ushort, c_ushort ]
    ISteamInput_TriggerVibration.restype = None

    global ISteamInput_TriggerVibrationExtended
    ISteamInput_TriggerVibrationExtended = dll.SteamAPI_ISteamInput_TriggerVibrationExtended
    ISteamInput_TriggerVibrationExtended.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ushort, c_ushort, c_ushort, c_ushort ]
    ISteamInput_TriggerVibrationExtended.restype = None

    global ISteamInput_TriggerSimpleHapticEvent
    ISteamInput_TriggerSimpleHapticEvent = dll.SteamAPI_ISteamInput_TriggerSimpleHapticEvent
    ISteamInput_TriggerSimpleHapticEvent.argtypes = [ POINTER(ISteamInput), c_ulonglong, EControllerHapticLocation, c_ubyte, c_byte, c_ubyte, c_byte ]
    ISteamInput_TriggerSimpleHapticEvent.restype = None

    global ISteamInput_SetLEDColor
    ISteamInput_SetLEDColor = dll.SteamAPI_ISteamInput_SetLEDColor
    ISteamInput_SetLEDColor.argtypes = [ POINTER(ISteamInput), c_ulonglong, c_ubyte, c_ubyte, c_ubyte, c_uint ]
    ISteamInput_SetLEDColor.restype = None

    global ISteamInput_Legacy_TriggerHapticPulse
    ISteamInput_Legacy_TriggerHapticPulse = dll.SteamAPI_ISteamInput_Legacy_TriggerHapticPulse
    ISteamInput_Legacy_TriggerHapticPulse.argtypes = [ POINTER(ISteamInput), c_ulonglong, ESteamControllerPad, c_ushort ]
    ISteamInput_Legacy_TriggerHapticPulse.restype = None

    global ISteamInput_Legacy_TriggerRepeatedHapticPulse
    ISteamInput_Legacy_TriggerRepeatedHapticPulse = dll.SteamAPI_ISteamInput_Legacy_TriggerRepeatedHapticPulse
    ISteamInput_Legacy_TriggerRepeatedHapticPulse.argtypes = [ POINTER(ISteamInput), c_ulonglong, ESteamControllerPad, c_ushort, c_ushort, c_ushort, c_uint ]
    ISteamInput_Legacy_TriggerRepeatedHapticPulse.restype = None

    global ISteamInput_ShowBindingPanel
    ISteamInput_ShowBindingPanel = dll.SteamAPI_ISteamInput_ShowBindingPanel
    ISteamInput_ShowBindingPanel.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_ShowBindingPanel.restype = c_bool

    global ISteamInput_GetInputTypeForHandle
    ISteamInput_GetInputTypeForHandle = dll.SteamAPI_ISteamInput_GetInputTypeForHandle
    ISteamInput_GetInputTypeForHandle.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetInputTypeForHandle.restype = ESteamInputType

    global ISteamInput_GetControllerForGamepadIndex
    ISteamInput_GetControllerForGamepadIndex = dll.SteamAPI_ISteamInput_GetControllerForGamepadIndex
    ISteamInput_GetControllerForGamepadIndex.argtypes = [ POINTER(ISteamInput), c_int ]
    ISteamInput_GetControllerForGamepadIndex.restype = c_ulonglong

    global ISteamInput_GetGamepadIndexForController
    ISteamInput_GetGamepadIndexForController = dll.SteamAPI_ISteamInput_GetGamepadIndexForController
    ISteamInput_GetGamepadIndexForController.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetGamepadIndexForController.restype = c_int

    global ISteamInput_GetStringForXboxOrigin
    ISteamInput_GetStringForXboxOrigin = dll.SteamAPI_ISteamInput_GetStringForXboxOrigin
    ISteamInput_GetStringForXboxOrigin.argtypes = [ POINTER(ISteamInput), EXboxOrigin ]
    ISteamInput_GetStringForXboxOrigin.restype = c_char_p

    global ISteamInput_GetGlyphForXboxOrigin
    ISteamInput_GetGlyphForXboxOrigin = dll.SteamAPI_ISteamInput_GetGlyphForXboxOrigin
    ISteamInput_GetGlyphForXboxOrigin.argtypes = [ POINTER(ISteamInput), EXboxOrigin ]
    ISteamInput_GetGlyphForXboxOrigin.restype = c_char_p

    global ISteamInput_GetActionOriginFromXboxOrigin
    ISteamInput_GetActionOriginFromXboxOrigin = dll.SteamAPI_ISteamInput_GetActionOriginFromXboxOrigin
    ISteamInput_GetActionOriginFromXboxOrigin.argtypes = [ POINTER(ISteamInput), c_ulonglong, EXboxOrigin ]
    ISteamInput_GetActionOriginFromXboxOrigin.restype = EInputActionOrigin

    global ISteamInput_TranslateActionOrigin
    ISteamInput_TranslateActionOrigin = dll.SteamAPI_ISteamInput_TranslateActionOrigin
    ISteamInput_TranslateActionOrigin.argtypes = [ POINTER(ISteamInput), ESteamInputType, EInputActionOrigin ]
    ISteamInput_TranslateActionOrigin.restype = EInputActionOrigin

    global ISteamInput_GetDeviceBindingRevision
    ISteamInput_GetDeviceBindingRevision = dll.SteamAPI_ISteamInput_GetDeviceBindingRevision
    ISteamInput_GetDeviceBindingRevision.argtypes = [ POINTER(ISteamInput), c_ulonglong, POINTER(c_int), POINTER(c_int) ]
    ISteamInput_GetDeviceBindingRevision.restype = c_bool

    global ISteamInput_GetRemotePlaySessionID
    ISteamInput_GetRemotePlaySessionID = dll.SteamAPI_ISteamInput_GetRemotePlaySessionID
    ISteamInput_GetRemotePlaySessionID.argtypes = [ POINTER(ISteamInput), c_ulonglong ]
    ISteamInput_GetRemotePlaySessionID.restype = c_uint

    global ISteamInput_GetSessionInputConfigurationSettings
    ISteamInput_GetSessionInputConfigurationSettings = dll.SteamAPI_ISteamInput_GetSessionInputConfigurationSettings
    ISteamInput_GetSessionInputConfigurationSettings.argtypes = [ POINTER(ISteamInput),  ]
    ISteamInput_GetSessionInputConfigurationSettings.restype = c_ushort

    global SteamInput_v006
    SteamInput_v006 = dll.SteamAPI_SteamInput_v006
    SteamInput_v006.argtypes = [ ]
    SteamInput_v006.restype = POINTER(ISteamInput)

    global ISteamController_Init
    ISteamController_Init = dll.SteamAPI_ISteamController_Init
    ISteamController_Init.argtypes = [ POINTER(ISteamController),  ]
    ISteamController_Init.restype = c_bool

    global ISteamController_Shutdown
    ISteamController_Shutdown = dll.SteamAPI_ISteamController_Shutdown
    ISteamController_Shutdown.argtypes = [ POINTER(ISteamController),  ]
    ISteamController_Shutdown.restype = c_bool

    global ISteamController_RunFrame
    ISteamController_RunFrame = dll.SteamAPI_ISteamController_RunFrame
    ISteamController_RunFrame.argtypes = [ POINTER(ISteamController),  ]
    ISteamController_RunFrame.restype = None

    global ISteamController_GetConnectedControllers
    ISteamController_GetConnectedControllers = dll.SteamAPI_ISteamController_GetConnectedControllers
    ISteamController_GetConnectedControllers.argtypes = [ POINTER(ISteamController), POINTER(c_ulonglong) ]
    ISteamController_GetConnectedControllers.restype = c_int

    global ISteamController_GetActionSetHandle
    ISteamController_GetActionSetHandle = dll.SteamAPI_ISteamController_GetActionSetHandle
    ISteamController_GetActionSetHandle.argtypes = [ POINTER(ISteamController), c_char_p ]
    ISteamController_GetActionSetHandle.restype = c_ulonglong

    global ISteamController_ActivateActionSet
    ISteamController_ActivateActionSet = dll.SteamAPI_ISteamController_ActivateActionSet
    ISteamController_ActivateActionSet.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_ActivateActionSet.restype = None

    global ISteamController_GetCurrentActionSet
    ISteamController_GetCurrentActionSet = dll.SteamAPI_ISteamController_GetCurrentActionSet
    ISteamController_GetCurrentActionSet.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_GetCurrentActionSet.restype = c_ulonglong

    global ISteamController_ActivateActionSetLayer
    ISteamController_ActivateActionSetLayer = dll.SteamAPI_ISteamController_ActivateActionSetLayer
    ISteamController_ActivateActionSetLayer.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_ActivateActionSetLayer.restype = None

    global ISteamController_DeactivateActionSetLayer
    ISteamController_DeactivateActionSetLayer = dll.SteamAPI_ISteamController_DeactivateActionSetLayer
    ISteamController_DeactivateActionSetLayer.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_DeactivateActionSetLayer.restype = None

    global ISteamController_DeactivateAllActionSetLayers
    ISteamController_DeactivateAllActionSetLayers = dll.SteamAPI_ISteamController_DeactivateAllActionSetLayers
    ISteamController_DeactivateAllActionSetLayers.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_DeactivateAllActionSetLayers.restype = None

    global ISteamController_GetActiveActionSetLayers
    ISteamController_GetActiveActionSetLayers = dll.SteamAPI_ISteamController_GetActiveActionSetLayers
    ISteamController_GetActiveActionSetLayers.argtypes = [ POINTER(ISteamController), c_ulonglong, POINTER(c_ulonglong) ]
    ISteamController_GetActiveActionSetLayers.restype = c_int

    global ISteamController_GetDigitalActionHandle
    ISteamController_GetDigitalActionHandle = dll.SteamAPI_ISteamController_GetDigitalActionHandle
    ISteamController_GetDigitalActionHandle.argtypes = [ POINTER(ISteamController), c_char_p ]
    ISteamController_GetDigitalActionHandle.restype = c_ulonglong

    global ISteamController_GetDigitalActionData
    ISteamController_GetDigitalActionData = dll.SteamAPI_ISteamController_GetDigitalActionData
    ISteamController_GetDigitalActionData.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_GetDigitalActionData.restype = InputDigitalActionData_t

    global ISteamController_GetDigitalActionOrigins
    ISteamController_GetDigitalActionOrigins = dll.SteamAPI_ISteamController_GetDigitalActionOrigins
    ISteamController_GetDigitalActionOrigins.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong, c_ulonglong, POINTER(EControllerActionOrigin) ]
    ISteamController_GetDigitalActionOrigins.restype = c_int

    global ISteamController_GetAnalogActionHandle
    ISteamController_GetAnalogActionHandle = dll.SteamAPI_ISteamController_GetAnalogActionHandle
    ISteamController_GetAnalogActionHandle.argtypes = [ POINTER(ISteamController), c_char_p ]
    ISteamController_GetAnalogActionHandle.restype = c_ulonglong

    global ISteamController_GetAnalogActionData
    ISteamController_GetAnalogActionData = dll.SteamAPI_ISteamController_GetAnalogActionData
    ISteamController_GetAnalogActionData.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_GetAnalogActionData.restype = InputAnalogActionData_t

    global ISteamController_GetAnalogActionOrigins
    ISteamController_GetAnalogActionOrigins = dll.SteamAPI_ISteamController_GetAnalogActionOrigins
    ISteamController_GetAnalogActionOrigins.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong, c_ulonglong, POINTER(EControllerActionOrigin) ]
    ISteamController_GetAnalogActionOrigins.restype = c_int

    global ISteamController_GetGlyphForActionOrigin
    ISteamController_GetGlyphForActionOrigin = dll.SteamAPI_ISteamController_GetGlyphForActionOrigin
    ISteamController_GetGlyphForActionOrigin.argtypes = [ POINTER(ISteamController), EControllerActionOrigin ]
    ISteamController_GetGlyphForActionOrigin.restype = c_char_p

    global ISteamController_GetStringForActionOrigin
    ISteamController_GetStringForActionOrigin = dll.SteamAPI_ISteamController_GetStringForActionOrigin
    ISteamController_GetStringForActionOrigin.argtypes = [ POINTER(ISteamController), EControllerActionOrigin ]
    ISteamController_GetStringForActionOrigin.restype = c_char_p

    global ISteamController_StopAnalogActionMomentum
    ISteamController_StopAnalogActionMomentum = dll.SteamAPI_ISteamController_StopAnalogActionMomentum
    ISteamController_StopAnalogActionMomentum.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ulonglong ]
    ISteamController_StopAnalogActionMomentum.restype = None

    global ISteamController_GetMotionData
    ISteamController_GetMotionData = dll.SteamAPI_ISteamController_GetMotionData
    ISteamController_GetMotionData.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_GetMotionData.restype = InputMotionData_t

    global ISteamController_TriggerHapticPulse
    ISteamController_TriggerHapticPulse = dll.SteamAPI_ISteamController_TriggerHapticPulse
    ISteamController_TriggerHapticPulse.argtypes = [ POINTER(ISteamController), c_ulonglong, ESteamControllerPad, c_ushort ]
    ISteamController_TriggerHapticPulse.restype = None

    global ISteamController_TriggerRepeatedHapticPulse
    ISteamController_TriggerRepeatedHapticPulse = dll.SteamAPI_ISteamController_TriggerRepeatedHapticPulse
    ISteamController_TriggerRepeatedHapticPulse.argtypes = [ POINTER(ISteamController), c_ulonglong, ESteamControllerPad, c_ushort, c_ushort, c_ushort, c_uint ]
    ISteamController_TriggerRepeatedHapticPulse.restype = None

    global ISteamController_TriggerVibration
    ISteamController_TriggerVibration = dll.SteamAPI_ISteamController_TriggerVibration
    ISteamController_TriggerVibration.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ushort, c_ushort ]
    ISteamController_TriggerVibration.restype = None

    global ISteamController_SetLEDColor
    ISteamController_SetLEDColor = dll.SteamAPI_ISteamController_SetLEDColor
    ISteamController_SetLEDColor.argtypes = [ POINTER(ISteamController), c_ulonglong, c_ubyte, c_ubyte, c_ubyte, c_uint ]
    ISteamController_SetLEDColor.restype = None

    global ISteamController_ShowBindingPanel
    ISteamController_ShowBindingPanel = dll.SteamAPI_ISteamController_ShowBindingPanel
    ISteamController_ShowBindingPanel.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_ShowBindingPanel.restype = c_bool

    global ISteamController_GetInputTypeForHandle
    ISteamController_GetInputTypeForHandle = dll.SteamAPI_ISteamController_GetInputTypeForHandle
    ISteamController_GetInputTypeForHandle.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_GetInputTypeForHandle.restype = ESteamInputType

    global ISteamController_GetControllerForGamepadIndex
    ISteamController_GetControllerForGamepadIndex = dll.SteamAPI_ISteamController_GetControllerForGamepadIndex
    ISteamController_GetControllerForGamepadIndex.argtypes = [ POINTER(ISteamController), c_int ]
    ISteamController_GetControllerForGamepadIndex.restype = c_ulonglong

    global ISteamController_GetGamepadIndexForController
    ISteamController_GetGamepadIndexForController = dll.SteamAPI_ISteamController_GetGamepadIndexForController
    ISteamController_GetGamepadIndexForController.argtypes = [ POINTER(ISteamController), c_ulonglong ]
    ISteamController_GetGamepadIndexForController.restype = c_int

    global ISteamController_GetStringForXboxOrigin
    ISteamController_GetStringForXboxOrigin = dll.SteamAPI_ISteamController_GetStringForXboxOrigin
    ISteamController_GetStringForXboxOrigin.argtypes = [ POINTER(ISteamController), EXboxOrigin ]
    ISteamController_GetStringForXboxOrigin.restype = c_char_p

    global ISteamController_GetGlyphForXboxOrigin
    ISteamController_GetGlyphForXboxOrigin = dll.SteamAPI_ISteamController_GetGlyphForXboxOrigin
    ISteamController_GetGlyphForXboxOrigin.argtypes = [ POINTER(ISteamController), EXboxOrigin ]
    ISteamController_GetGlyphForXboxOrigin.restype = c_char_p

    global ISteamController_GetActionOriginFromXboxOrigin
    ISteamController_GetActionOriginFromXboxOrigin = dll.SteamAPI_ISteamController_GetActionOriginFromXboxOrigin
    ISteamController_GetActionOriginFromXboxOrigin.argtypes = [ POINTER(ISteamController), c_ulonglong, EXboxOrigin ]
    ISteamController_GetActionOriginFromXboxOrigin.restype = EControllerActionOrigin

    global ISteamController_TranslateActionOrigin
    ISteamController_TranslateActionOrigin = dll.SteamAPI_ISteamController_TranslateActionOrigin
    ISteamController_TranslateActionOrigin.argtypes = [ POINTER(ISteamController), ESteamInputType, EControllerActionOrigin ]
    ISteamController_TranslateActionOrigin.restype = EControllerActionOrigin

    global ISteamController_GetControllerBindingRevision
    ISteamController_GetControllerBindingRevision = dll.SteamAPI_ISteamController_GetControllerBindingRevision
    ISteamController_GetControllerBindingRevision.argtypes = [ POINTER(ISteamController), c_ulonglong, POINTER(c_int), POINTER(c_int) ]
    ISteamController_GetControllerBindingRevision.restype = c_bool

    global SteamController_v008
    SteamController_v008 = dll.SteamAPI_SteamController_v008
    SteamController_v008.argtypes = [ ]
    SteamController_v008.restype = POINTER(ISteamController)

    global ISteamUGC_CreateQueryUserUGCRequest
    ISteamUGC_CreateQueryUserUGCRequest = dll.SteamAPI_ISteamUGC_CreateQueryUserUGCRequest
    ISteamUGC_CreateQueryUserUGCRequest.argtypes = [ POINTER(ISteamUGC), c_uint, EUserUGCList, EUGCMatchingUGCType, EUserUGCListSortOrder, c_uint, c_uint, c_uint ]
    ISteamUGC_CreateQueryUserUGCRequest.restype = c_ulonglong

    global ISteamUGC_CreateQueryAllUGCRequestPage
    ISteamUGC_CreateQueryAllUGCRequestPage = dll.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestPage
    ISteamUGC_CreateQueryAllUGCRequestPage.argtypes = [ POINTER(ISteamUGC), EUGCQuery, EUGCMatchingUGCType, c_uint, c_uint, c_uint ]
    ISteamUGC_CreateQueryAllUGCRequestPage.restype = c_ulonglong

    global ISteamUGC_CreateQueryAllUGCRequestCursor
    ISteamUGC_CreateQueryAllUGCRequestCursor = dll.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestCursor
    ISteamUGC_CreateQueryAllUGCRequestCursor.argtypes = [ POINTER(ISteamUGC), EUGCQuery, EUGCMatchingUGCType, c_uint, c_uint, c_char_p ]
    ISteamUGC_CreateQueryAllUGCRequestCursor.restype = c_ulonglong

    global ISteamUGC_CreateQueryUGCDetailsRequest
    ISteamUGC_CreateQueryUGCDetailsRequest = dll.SteamAPI_ISteamUGC_CreateQueryUGCDetailsRequest
    ISteamUGC_CreateQueryUGCDetailsRequest.argtypes = [ POINTER(ISteamUGC), POINTER(c_ulonglong), c_uint ]
    ISteamUGC_CreateQueryUGCDetailsRequest.restype = c_ulonglong

    global ISteamUGC_SendQueryUGCRequest
    ISteamUGC_SendQueryUGCRequest = dll.SteamAPI_ISteamUGC_SendQueryUGCRequest
    ISteamUGC_SendQueryUGCRequest.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_SendQueryUGCRequest.restype = c_ulonglong

    global ISteamUGC_GetQueryUGCResult
    ISteamUGC_GetQueryUGCResult = dll.SteamAPI_ISteamUGC_GetQueryUGCResult
    ISteamUGC_GetQueryUGCResult.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, POINTER(SteamUGCDetails_t) ]
    ISteamUGC_GetQueryUGCResult.restype = c_bool

    global ISteamUGC_GetQueryUGCNumTags
    ISteamUGC_GetQueryUGCNumTags = dll.SteamAPI_ISteamUGC_GetQueryUGCNumTags
    ISteamUGC_GetQueryUGCNumTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_GetQueryUGCNumTags.restype = c_uint

    global ISteamUGC_GetQueryUGCTag
    ISteamUGC_GetQueryUGCTag = dll.SteamAPI_ISteamUGC_GetQueryUGCTag
    ISteamUGC_GetQueryUGCTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint, c_char_p, c_uint ]
    ISteamUGC_GetQueryUGCTag.restype = c_bool

    global ISteamUGC_GetQueryUGCTagDisplayName
    ISteamUGC_GetQueryUGCTagDisplayName = dll.SteamAPI_ISteamUGC_GetQueryUGCTagDisplayName
    ISteamUGC_GetQueryUGCTagDisplayName.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint, c_char_p, c_uint ]
    ISteamUGC_GetQueryUGCTagDisplayName.restype = c_bool

    global ISteamUGC_GetQueryUGCPreviewURL
    ISteamUGC_GetQueryUGCPreviewURL = dll.SteamAPI_ISteamUGC_GetQueryUGCPreviewURL
    ISteamUGC_GetQueryUGCPreviewURL.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_char_p, c_uint ]
    ISteamUGC_GetQueryUGCPreviewURL.restype = c_bool

    global ISteamUGC_GetQueryUGCMetadata
    ISteamUGC_GetQueryUGCMetadata = dll.SteamAPI_ISteamUGC_GetQueryUGCMetadata
    ISteamUGC_GetQueryUGCMetadata.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_char_p, c_uint ]
    ISteamUGC_GetQueryUGCMetadata.restype = c_bool

    global ISteamUGC_GetQueryUGCChildren
    ISteamUGC_GetQueryUGCChildren = dll.SteamAPI_ISteamUGC_GetQueryUGCChildren
    ISteamUGC_GetQueryUGCChildren.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, POINTER(c_ulonglong), c_uint ]
    ISteamUGC_GetQueryUGCChildren.restype = c_bool

    global ISteamUGC_GetQueryUGCStatistic
    ISteamUGC_GetQueryUGCStatistic = dll.SteamAPI_ISteamUGC_GetQueryUGCStatistic
    ISteamUGC_GetQueryUGCStatistic.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, EItemStatistic, POINTER(c_ulonglong) ]
    ISteamUGC_GetQueryUGCStatistic.restype = c_bool

    global ISteamUGC_GetQueryUGCNumAdditionalPreviews
    ISteamUGC_GetQueryUGCNumAdditionalPreviews = dll.SteamAPI_ISteamUGC_GetQueryUGCNumAdditionalPreviews
    ISteamUGC_GetQueryUGCNumAdditionalPreviews.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_GetQueryUGCNumAdditionalPreviews.restype = c_uint

    global ISteamUGC_GetQueryUGCAdditionalPreview
    ISteamUGC_GetQueryUGCAdditionalPreview = dll.SteamAPI_ISteamUGC_GetQueryUGCAdditionalPreview
    ISteamUGC_GetQueryUGCAdditionalPreview.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint, c_char_p, c_uint, c_char_p, c_uint, POINTER(EItemPreviewType) ]
    ISteamUGC_GetQueryUGCAdditionalPreview.restype = c_bool

    global ISteamUGC_GetQueryUGCNumKeyValueTags
    ISteamUGC_GetQueryUGCNumKeyValueTags = dll.SteamAPI_ISteamUGC_GetQueryUGCNumKeyValueTags
    ISteamUGC_GetQueryUGCNumKeyValueTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_GetQueryUGCNumKeyValueTags.restype = c_uint

    global ISteamUGC_GetQueryUGCKeyValueTag
    ISteamUGC_GetQueryUGCKeyValueTag = dll.SteamAPI_ISteamUGC_GetQueryUGCKeyValueTag
    ISteamUGC_GetQueryUGCKeyValueTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint, c_char_p, c_uint, c_char_p, c_uint ]
    ISteamUGC_GetQueryUGCKeyValueTag.restype = c_bool

    global ISteamUGC_GetQueryFirstUGCKeyValueTag
    ISteamUGC_GetQueryFirstUGCKeyValueTag = dll.SteamAPI_ISteamUGC_GetQueryFirstUGCKeyValueTag
    ISteamUGC_GetQueryFirstUGCKeyValueTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_char_p, c_char_p, c_uint ]
    ISteamUGC_GetQueryFirstUGCKeyValueTag.restype = c_bool

    global ISteamUGC_ReleaseQueryUGCRequest
    ISteamUGC_ReleaseQueryUGCRequest = dll.SteamAPI_ISteamUGC_ReleaseQueryUGCRequest
    ISteamUGC_ReleaseQueryUGCRequest.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_ReleaseQueryUGCRequest.restype = c_bool

    global ISteamUGC_AddRequiredTag
    ISteamUGC_AddRequiredTag = dll.SteamAPI_ISteamUGC_AddRequiredTag
    ISteamUGC_AddRequiredTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_AddRequiredTag.restype = c_bool

    global ISteamUGC_AddRequiredTagGroup
    ISteamUGC_AddRequiredTagGroup = dll.SteamAPI_ISteamUGC_AddRequiredTagGroup
    ISteamUGC_AddRequiredTagGroup.argtypes = [ POINTER(ISteamUGC), c_ulonglong, POINTER(SteamParamStringArray_t) ]
    ISteamUGC_AddRequiredTagGroup.restype = c_bool

    global ISteamUGC_AddExcludedTag
    ISteamUGC_AddExcludedTag = dll.SteamAPI_ISteamUGC_AddExcludedTag
    ISteamUGC_AddExcludedTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_AddExcludedTag.restype = c_bool

    global ISteamUGC_SetReturnOnlyIDs
    ISteamUGC_SetReturnOnlyIDs = dll.SteamAPI_ISteamUGC_SetReturnOnlyIDs
    ISteamUGC_SetReturnOnlyIDs.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnOnlyIDs.restype = c_bool

    global ISteamUGC_SetReturnKeyValueTags
    ISteamUGC_SetReturnKeyValueTags = dll.SteamAPI_ISteamUGC_SetReturnKeyValueTags
    ISteamUGC_SetReturnKeyValueTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnKeyValueTags.restype = c_bool

    global ISteamUGC_SetReturnLongDescription
    ISteamUGC_SetReturnLongDescription = dll.SteamAPI_ISteamUGC_SetReturnLongDescription
    ISteamUGC_SetReturnLongDescription.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnLongDescription.restype = c_bool

    global ISteamUGC_SetReturnMetadata
    ISteamUGC_SetReturnMetadata = dll.SteamAPI_ISteamUGC_SetReturnMetadata
    ISteamUGC_SetReturnMetadata.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnMetadata.restype = c_bool

    global ISteamUGC_SetReturnChildren
    ISteamUGC_SetReturnChildren = dll.SteamAPI_ISteamUGC_SetReturnChildren
    ISteamUGC_SetReturnChildren.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnChildren.restype = c_bool

    global ISteamUGC_SetReturnAdditionalPreviews
    ISteamUGC_SetReturnAdditionalPreviews = dll.SteamAPI_ISteamUGC_SetReturnAdditionalPreviews
    ISteamUGC_SetReturnAdditionalPreviews.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnAdditionalPreviews.restype = c_bool

    global ISteamUGC_SetReturnTotalOnly
    ISteamUGC_SetReturnTotalOnly = dll.SteamAPI_ISteamUGC_SetReturnTotalOnly
    ISteamUGC_SetReturnTotalOnly.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetReturnTotalOnly.restype = c_bool

    global ISteamUGC_SetReturnPlaytimeStats
    ISteamUGC_SetReturnPlaytimeStats = dll.SteamAPI_ISteamUGC_SetReturnPlaytimeStats
    ISteamUGC_SetReturnPlaytimeStats.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_SetReturnPlaytimeStats.restype = c_bool

    global ISteamUGC_SetLanguage
    ISteamUGC_SetLanguage = dll.SteamAPI_ISteamUGC_SetLanguage
    ISteamUGC_SetLanguage.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetLanguage.restype = c_bool

    global ISteamUGC_SetAllowCachedResponse
    ISteamUGC_SetAllowCachedResponse = dll.SteamAPI_ISteamUGC_SetAllowCachedResponse
    ISteamUGC_SetAllowCachedResponse.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_SetAllowCachedResponse.restype = c_bool

    global ISteamUGC_SetCloudFileNameFilter
    ISteamUGC_SetCloudFileNameFilter = dll.SteamAPI_ISteamUGC_SetCloudFileNameFilter
    ISteamUGC_SetCloudFileNameFilter.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetCloudFileNameFilter.restype = c_bool

    global ISteamUGC_SetMatchAnyTag
    ISteamUGC_SetMatchAnyTag = dll.SteamAPI_ISteamUGC_SetMatchAnyTag
    ISteamUGC_SetMatchAnyTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetMatchAnyTag.restype = c_bool

    global ISteamUGC_SetSearchText
    ISteamUGC_SetSearchText = dll.SteamAPI_ISteamUGC_SetSearchText
    ISteamUGC_SetSearchText.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetSearchText.restype = c_bool

    global ISteamUGC_SetRankedByTrendDays
    ISteamUGC_SetRankedByTrendDays = dll.SteamAPI_ISteamUGC_SetRankedByTrendDays
    ISteamUGC_SetRankedByTrendDays.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_SetRankedByTrendDays.restype = c_bool

    global ISteamUGC_SetTimeCreatedDateRange
    ISteamUGC_SetTimeCreatedDateRange = dll.SteamAPI_ISteamUGC_SetTimeCreatedDateRange
    ISteamUGC_SetTimeCreatedDateRange.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint ]
    ISteamUGC_SetTimeCreatedDateRange.restype = c_bool

    global ISteamUGC_SetTimeUpdatedDateRange
    ISteamUGC_SetTimeUpdatedDateRange = dll.SteamAPI_ISteamUGC_SetTimeUpdatedDateRange
    ISteamUGC_SetTimeUpdatedDateRange.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_uint ]
    ISteamUGC_SetTimeUpdatedDateRange.restype = c_bool

    global ISteamUGC_AddRequiredKeyValueTag
    ISteamUGC_AddRequiredKeyValueTag = dll.SteamAPI_ISteamUGC_AddRequiredKeyValueTag
    ISteamUGC_AddRequiredKeyValueTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p, c_char_p ]
    ISteamUGC_AddRequiredKeyValueTag.restype = c_bool

    global ISteamUGC_RequestUGCDetails
    ISteamUGC_RequestUGCDetails = dll.SteamAPI_ISteamUGC_RequestUGCDetails
    ISteamUGC_RequestUGCDetails.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_RequestUGCDetails.restype = c_ulonglong

    global ISteamUGC_CreateItem
    ISteamUGC_CreateItem = dll.SteamAPI_ISteamUGC_CreateItem
    ISteamUGC_CreateItem.argtypes = [ POINTER(ISteamUGC), c_uint, EWorkshopFileType ]
    ISteamUGC_CreateItem.restype = c_ulonglong

    global ISteamUGC_StartItemUpdate
    ISteamUGC_StartItemUpdate = dll.SteamAPI_ISteamUGC_StartItemUpdate
    ISteamUGC_StartItemUpdate.argtypes = [ POINTER(ISteamUGC), c_uint, c_ulonglong ]
    ISteamUGC_StartItemUpdate.restype = c_ulonglong

    global ISteamUGC_SetItemTitle
    ISteamUGC_SetItemTitle = dll.SteamAPI_ISteamUGC_SetItemTitle
    ISteamUGC_SetItemTitle.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemTitle.restype = c_bool

    global ISteamUGC_SetItemDescription
    ISteamUGC_SetItemDescription = dll.SteamAPI_ISteamUGC_SetItemDescription
    ISteamUGC_SetItemDescription.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemDescription.restype = c_bool

    global ISteamUGC_SetItemUpdateLanguage
    ISteamUGC_SetItemUpdateLanguage = dll.SteamAPI_ISteamUGC_SetItemUpdateLanguage
    ISteamUGC_SetItemUpdateLanguage.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemUpdateLanguage.restype = c_bool

    global ISteamUGC_SetItemMetadata
    ISteamUGC_SetItemMetadata = dll.SteamAPI_ISteamUGC_SetItemMetadata
    ISteamUGC_SetItemMetadata.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemMetadata.restype = c_bool

    global ISteamUGC_SetItemVisibility
    ISteamUGC_SetItemVisibility = dll.SteamAPI_ISteamUGC_SetItemVisibility
    ISteamUGC_SetItemVisibility.argtypes = [ POINTER(ISteamUGC), c_ulonglong, ERemoteStoragePublishedFileVisibility ]
    ISteamUGC_SetItemVisibility.restype = c_bool

    global ISteamUGC_SetItemTags
    ISteamUGC_SetItemTags = dll.SteamAPI_ISteamUGC_SetItemTags
    ISteamUGC_SetItemTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong, POINTER(SteamParamStringArray_t) ]
    ISteamUGC_SetItemTags.restype = c_bool

    global ISteamUGC_SetItemContent
    ISteamUGC_SetItemContent = dll.SteamAPI_ISteamUGC_SetItemContent
    ISteamUGC_SetItemContent.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemContent.restype = c_bool

    global ISteamUGC_SetItemPreview
    ISteamUGC_SetItemPreview = dll.SteamAPI_ISteamUGC_SetItemPreview
    ISteamUGC_SetItemPreview.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SetItemPreview.restype = c_bool

    global ISteamUGC_SetAllowLegacyUpload
    ISteamUGC_SetAllowLegacyUpload = dll.SteamAPI_ISteamUGC_SetAllowLegacyUpload
    ISteamUGC_SetAllowLegacyUpload.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetAllowLegacyUpload.restype = c_bool

    global ISteamUGC_RemoveAllItemKeyValueTags
    ISteamUGC_RemoveAllItemKeyValueTags = dll.SteamAPI_ISteamUGC_RemoveAllItemKeyValueTags
    ISteamUGC_RemoveAllItemKeyValueTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_RemoveAllItemKeyValueTags.restype = c_bool

    global ISteamUGC_RemoveItemKeyValueTags
    ISteamUGC_RemoveItemKeyValueTags = dll.SteamAPI_ISteamUGC_RemoveItemKeyValueTags
    ISteamUGC_RemoveItemKeyValueTags.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_RemoveItemKeyValueTags.restype = c_bool

    global ISteamUGC_AddItemKeyValueTag
    ISteamUGC_AddItemKeyValueTag = dll.SteamAPI_ISteamUGC_AddItemKeyValueTag
    ISteamUGC_AddItemKeyValueTag.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p, c_char_p ]
    ISteamUGC_AddItemKeyValueTag.restype = c_bool

    global ISteamUGC_AddItemPreviewFile
    ISteamUGC_AddItemPreviewFile = dll.SteamAPI_ISteamUGC_AddItemPreviewFile
    ISteamUGC_AddItemPreviewFile.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p, EItemPreviewType ]
    ISteamUGC_AddItemPreviewFile.restype = c_bool

    global ISteamUGC_AddItemPreviewVideo
    ISteamUGC_AddItemPreviewVideo = dll.SteamAPI_ISteamUGC_AddItemPreviewVideo
    ISteamUGC_AddItemPreviewVideo.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_AddItemPreviewVideo.restype = c_bool

    global ISteamUGC_UpdateItemPreviewFile
    ISteamUGC_UpdateItemPreviewFile = dll.SteamAPI_ISteamUGC_UpdateItemPreviewFile
    ISteamUGC_UpdateItemPreviewFile.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_char_p ]
    ISteamUGC_UpdateItemPreviewFile.restype = c_bool

    global ISteamUGC_UpdateItemPreviewVideo
    ISteamUGC_UpdateItemPreviewVideo = dll.SteamAPI_ISteamUGC_UpdateItemPreviewVideo
    ISteamUGC_UpdateItemPreviewVideo.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint, c_char_p ]
    ISteamUGC_UpdateItemPreviewVideo.restype = c_bool

    global ISteamUGC_RemoveItemPreview
    ISteamUGC_RemoveItemPreview = dll.SteamAPI_ISteamUGC_RemoveItemPreview
    ISteamUGC_RemoveItemPreview.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_RemoveItemPreview.restype = c_bool

    global ISteamUGC_SubmitItemUpdate
    ISteamUGC_SubmitItemUpdate = dll.SteamAPI_ISteamUGC_SubmitItemUpdate
    ISteamUGC_SubmitItemUpdate.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_char_p ]
    ISteamUGC_SubmitItemUpdate.restype = c_ulonglong

    global ISteamUGC_GetItemUpdateProgress
    ISteamUGC_GetItemUpdateProgress = dll.SteamAPI_ISteamUGC_GetItemUpdateProgress
    ISteamUGC_GetItemUpdateProgress.argtypes = [ POINTER(ISteamUGC), c_ulonglong, POINTER(c_ulonglong), POINTER(c_ulonglong) ]
    ISteamUGC_GetItemUpdateProgress.restype = EItemUpdateStatus

    global ISteamUGC_SetUserItemVote
    ISteamUGC_SetUserItemVote = dll.SteamAPI_ISteamUGC_SetUserItemVote
    ISteamUGC_SetUserItemVote.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_SetUserItemVote.restype = c_ulonglong

    global ISteamUGC_GetUserItemVote
    ISteamUGC_GetUserItemVote = dll.SteamAPI_ISteamUGC_GetUserItemVote
    ISteamUGC_GetUserItemVote.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_GetUserItemVote.restype = c_ulonglong

    global ISteamUGC_AddItemToFavorites
    ISteamUGC_AddItemToFavorites = dll.SteamAPI_ISteamUGC_AddItemToFavorites
    ISteamUGC_AddItemToFavorites.argtypes = [ POINTER(ISteamUGC), c_uint, c_ulonglong ]
    ISteamUGC_AddItemToFavorites.restype = c_ulonglong

    global ISteamUGC_RemoveItemFromFavorites
    ISteamUGC_RemoveItemFromFavorites = dll.SteamAPI_ISteamUGC_RemoveItemFromFavorites
    ISteamUGC_RemoveItemFromFavorites.argtypes = [ POINTER(ISteamUGC), c_uint, c_ulonglong ]
    ISteamUGC_RemoveItemFromFavorites.restype = c_ulonglong

    global ISteamUGC_SubscribeItem
    ISteamUGC_SubscribeItem = dll.SteamAPI_ISteamUGC_SubscribeItem
    ISteamUGC_SubscribeItem.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_SubscribeItem.restype = c_ulonglong

    global ISteamUGC_UnsubscribeItem
    ISteamUGC_UnsubscribeItem = dll.SteamAPI_ISteamUGC_UnsubscribeItem
    ISteamUGC_UnsubscribeItem.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_UnsubscribeItem.restype = c_ulonglong

    global ISteamUGC_GetNumSubscribedItems
    ISteamUGC_GetNumSubscribedItems = dll.SteamAPI_ISteamUGC_GetNumSubscribedItems
    ISteamUGC_GetNumSubscribedItems.argtypes = [ POINTER(ISteamUGC),  ]
    ISteamUGC_GetNumSubscribedItems.restype = c_uint

    global ISteamUGC_GetSubscribedItems
    ISteamUGC_GetSubscribedItems = dll.SteamAPI_ISteamUGC_GetSubscribedItems
    ISteamUGC_GetSubscribedItems.argtypes = [ POINTER(ISteamUGC), POINTER(c_ulonglong), c_uint ]
    ISteamUGC_GetSubscribedItems.restype = c_uint

    global ISteamUGC_GetItemState
    ISteamUGC_GetItemState = dll.SteamAPI_ISteamUGC_GetItemState
    ISteamUGC_GetItemState.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_GetItemState.restype = c_uint

    global ISteamUGC_GetItemInstallInfo
    ISteamUGC_GetItemInstallInfo = dll.SteamAPI_ISteamUGC_GetItemInstallInfo
    ISteamUGC_GetItemInstallInfo.argtypes = [ POINTER(ISteamUGC), c_ulonglong, POINTER(c_ulonglong), c_char_p, c_uint, POINTER(c_uint) ]
    ISteamUGC_GetItemInstallInfo.restype = c_bool

    global ISteamUGC_GetItemDownloadInfo
    ISteamUGC_GetItemDownloadInfo = dll.SteamAPI_ISteamUGC_GetItemDownloadInfo
    ISteamUGC_GetItemDownloadInfo.argtypes = [ POINTER(ISteamUGC), c_ulonglong, POINTER(c_ulonglong), POINTER(c_ulonglong) ]
    ISteamUGC_GetItemDownloadInfo.restype = c_bool

    global ISteamUGC_DownloadItem
    ISteamUGC_DownloadItem = dll.SteamAPI_ISteamUGC_DownloadItem
    ISteamUGC_DownloadItem.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_bool ]
    ISteamUGC_DownloadItem.restype = c_bool

    global ISteamUGC_BInitWorkshopForGameServer
    ISteamUGC_BInitWorkshopForGameServer = dll.SteamAPI_ISteamUGC_BInitWorkshopForGameServer
    ISteamUGC_BInitWorkshopForGameServer.argtypes = [ POINTER(ISteamUGC), c_uint, c_char_p ]
    ISteamUGC_BInitWorkshopForGameServer.restype = c_bool

    global ISteamUGC_SuspendDownloads
    ISteamUGC_SuspendDownloads = dll.SteamAPI_ISteamUGC_SuspendDownloads
    ISteamUGC_SuspendDownloads.argtypes = [ POINTER(ISteamUGC), c_bool ]
    ISteamUGC_SuspendDownloads.restype = None

    global ISteamUGC_StartPlaytimeTracking
    ISteamUGC_StartPlaytimeTracking = dll.SteamAPI_ISteamUGC_StartPlaytimeTracking
    ISteamUGC_StartPlaytimeTracking.argtypes = [ POINTER(ISteamUGC), POINTER(c_ulonglong), c_uint ]
    ISteamUGC_StartPlaytimeTracking.restype = c_ulonglong

    global ISteamUGC_StopPlaytimeTracking
    ISteamUGC_StopPlaytimeTracking = dll.SteamAPI_ISteamUGC_StopPlaytimeTracking
    ISteamUGC_StopPlaytimeTracking.argtypes = [ POINTER(ISteamUGC), POINTER(c_ulonglong), c_uint ]
    ISteamUGC_StopPlaytimeTracking.restype = c_ulonglong

    global ISteamUGC_StopPlaytimeTrackingForAllItems
    ISteamUGC_StopPlaytimeTrackingForAllItems = dll.SteamAPI_ISteamUGC_StopPlaytimeTrackingForAllItems
    ISteamUGC_StopPlaytimeTrackingForAllItems.argtypes = [ POINTER(ISteamUGC),  ]
    ISteamUGC_StopPlaytimeTrackingForAllItems.restype = c_ulonglong

    global ISteamUGC_AddDependency
    ISteamUGC_AddDependency = dll.SteamAPI_ISteamUGC_AddDependency
    ISteamUGC_AddDependency.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_ulonglong ]
    ISteamUGC_AddDependency.restype = c_ulonglong

    global ISteamUGC_RemoveDependency
    ISteamUGC_RemoveDependency = dll.SteamAPI_ISteamUGC_RemoveDependency
    ISteamUGC_RemoveDependency.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_ulonglong ]
    ISteamUGC_RemoveDependency.restype = c_ulonglong

    global ISteamUGC_AddAppDependency
    ISteamUGC_AddAppDependency = dll.SteamAPI_ISteamUGC_AddAppDependency
    ISteamUGC_AddAppDependency.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_AddAppDependency.restype = c_ulonglong

    global ISteamUGC_RemoveAppDependency
    ISteamUGC_RemoveAppDependency = dll.SteamAPI_ISteamUGC_RemoveAppDependency
    ISteamUGC_RemoveAppDependency.argtypes = [ POINTER(ISteamUGC), c_ulonglong, c_uint ]
    ISteamUGC_RemoveAppDependency.restype = c_ulonglong

    global ISteamUGC_GetAppDependencies
    ISteamUGC_GetAppDependencies = dll.SteamAPI_ISteamUGC_GetAppDependencies
    ISteamUGC_GetAppDependencies.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_GetAppDependencies.restype = c_ulonglong

    global ISteamUGC_DeleteItem
    ISteamUGC_DeleteItem = dll.SteamAPI_ISteamUGC_DeleteItem
    ISteamUGC_DeleteItem.argtypes = [ POINTER(ISteamUGC), c_ulonglong ]
    ISteamUGC_DeleteItem.restype = c_ulonglong

    global ISteamUGC_ShowWorkshopEULA
    ISteamUGC_ShowWorkshopEULA = dll.SteamAPI_ISteamUGC_ShowWorkshopEULA
    ISteamUGC_ShowWorkshopEULA.argtypes = [ POINTER(ISteamUGC),  ]
    ISteamUGC_ShowWorkshopEULA.restype = c_bool

    global ISteamUGC_GetWorkshopEULAStatus
    ISteamUGC_GetWorkshopEULAStatus = dll.SteamAPI_ISteamUGC_GetWorkshopEULAStatus
    ISteamUGC_GetWorkshopEULAStatus.argtypes = [ POINTER(ISteamUGC),  ]
    ISteamUGC_GetWorkshopEULAStatus.restype = c_ulonglong

    global SteamUGC_v016
    SteamUGC_v016 = dll.SteamAPI_SteamUGC_v016
    SteamUGC_v016.argtypes = [ ]
    SteamUGC_v016.restype = POINTER(ISteamUGC)

    global SteamGameServerUGC_v016
    SteamGameServerUGC_v016 = dll.SteamAPI_SteamGameServerUGC_v016
    SteamGameServerUGC_v016.argtypes = [ ]
    SteamGameServerUGC_v016.restype = POINTER(ISteamUGC)

    global ISteamAppList_GetNumInstalledApps
    ISteamAppList_GetNumInstalledApps = dll.SteamAPI_ISteamAppList_GetNumInstalledApps
    ISteamAppList_GetNumInstalledApps.argtypes = [ POINTER(ISteamAppList),  ]
    ISteamAppList_GetNumInstalledApps.restype = c_uint

    global ISteamAppList_GetInstalledApps
    ISteamAppList_GetInstalledApps = dll.SteamAPI_ISteamAppList_GetInstalledApps
    ISteamAppList_GetInstalledApps.argtypes = [ POINTER(ISteamAppList), POINTER(c_uint), c_uint ]
    ISteamAppList_GetInstalledApps.restype = c_uint

    global ISteamAppList_GetAppName
    ISteamAppList_GetAppName = dll.SteamAPI_ISteamAppList_GetAppName
    ISteamAppList_GetAppName.argtypes = [ POINTER(ISteamAppList), c_uint, c_char_p, c_int ]
    ISteamAppList_GetAppName.restype = c_int

    global ISteamAppList_GetAppInstallDir
    ISteamAppList_GetAppInstallDir = dll.SteamAPI_ISteamAppList_GetAppInstallDir
    ISteamAppList_GetAppInstallDir.argtypes = [ POINTER(ISteamAppList), c_uint, c_char_p, c_int ]
    ISteamAppList_GetAppInstallDir.restype = c_int

    global ISteamAppList_GetAppBuildId
    ISteamAppList_GetAppBuildId = dll.SteamAPI_ISteamAppList_GetAppBuildId
    ISteamAppList_GetAppBuildId.argtypes = [ POINTER(ISteamAppList), c_uint ]
    ISteamAppList_GetAppBuildId.restype = c_int

    global SteamAppList_v001
    SteamAppList_v001 = dll.SteamAPI_SteamAppList_v001
    SteamAppList_v001.argtypes = [ ]
    SteamAppList_v001.restype = POINTER(ISteamAppList)

    global ISteamHTMLSurface_Init
    ISteamHTMLSurface_Init = dll.SteamAPI_ISteamHTMLSurface_Init
    ISteamHTMLSurface_Init.argtypes = [ POINTER(ISteamHTMLSurface),  ]
    ISteamHTMLSurface_Init.restype = c_bool

    global ISteamHTMLSurface_Shutdown
    ISteamHTMLSurface_Shutdown = dll.SteamAPI_ISteamHTMLSurface_Shutdown
    ISteamHTMLSurface_Shutdown.argtypes = [ POINTER(ISteamHTMLSurface),  ]
    ISteamHTMLSurface_Shutdown.restype = c_bool

    global ISteamHTMLSurface_CreateBrowser
    ISteamHTMLSurface_CreateBrowser = dll.SteamAPI_ISteamHTMLSurface_CreateBrowser
    ISteamHTMLSurface_CreateBrowser.argtypes = [ POINTER(ISteamHTMLSurface), c_char_p, c_char_p ]
    ISteamHTMLSurface_CreateBrowser.restype = c_ulonglong

    global ISteamHTMLSurface_RemoveBrowser
    ISteamHTMLSurface_RemoveBrowser = dll.SteamAPI_ISteamHTMLSurface_RemoveBrowser
    ISteamHTMLSurface_RemoveBrowser.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_RemoveBrowser.restype = None

    global ISteamHTMLSurface_LoadURL
    ISteamHTMLSurface_LoadURL = dll.SteamAPI_ISteamHTMLSurface_LoadURL
    ISteamHTMLSurface_LoadURL.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_char_p, c_char_p ]
    ISteamHTMLSurface_LoadURL.restype = None

    global ISteamHTMLSurface_SetSize
    ISteamHTMLSurface_SetSize = dll.SteamAPI_ISteamHTMLSurface_SetSize
    ISteamHTMLSurface_SetSize.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint, c_uint ]
    ISteamHTMLSurface_SetSize.restype = None

    global ISteamHTMLSurface_StopLoad
    ISteamHTMLSurface_StopLoad = dll.SteamAPI_ISteamHTMLSurface_StopLoad
    ISteamHTMLSurface_StopLoad.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_StopLoad.restype = None

    global ISteamHTMLSurface_Reload
    ISteamHTMLSurface_Reload = dll.SteamAPI_ISteamHTMLSurface_Reload
    ISteamHTMLSurface_Reload.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_Reload.restype = None

    global ISteamHTMLSurface_GoBack
    ISteamHTMLSurface_GoBack = dll.SteamAPI_ISteamHTMLSurface_GoBack
    ISteamHTMLSurface_GoBack.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_GoBack.restype = None

    global ISteamHTMLSurface_GoForward
    ISteamHTMLSurface_GoForward = dll.SteamAPI_ISteamHTMLSurface_GoForward
    ISteamHTMLSurface_GoForward.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_GoForward.restype = None

    global ISteamHTMLSurface_AddHeader
    ISteamHTMLSurface_AddHeader = dll.SteamAPI_ISteamHTMLSurface_AddHeader
    ISteamHTMLSurface_AddHeader.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_char_p, c_char_p ]
    ISteamHTMLSurface_AddHeader.restype = None

    global ISteamHTMLSurface_ExecuteJavascript
    ISteamHTMLSurface_ExecuteJavascript = dll.SteamAPI_ISteamHTMLSurface_ExecuteJavascript
    ISteamHTMLSurface_ExecuteJavascript.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_char_p ]
    ISteamHTMLSurface_ExecuteJavascript.restype = None

    global ISteamHTMLSurface_MouseUp
    ISteamHTMLSurface_MouseUp = dll.SteamAPI_ISteamHTMLSurface_MouseUp
    ISteamHTMLSurface_MouseUp.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int ]
    ISteamHTMLSurface_MouseUp.restype = None

    global ISteamHTMLSurface_MouseDown
    ISteamHTMLSurface_MouseDown = dll.SteamAPI_ISteamHTMLSurface_MouseDown
    ISteamHTMLSurface_MouseDown.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int ]
    ISteamHTMLSurface_MouseDown.restype = None

    global ISteamHTMLSurface_MouseDoubleClick
    ISteamHTMLSurface_MouseDoubleClick = dll.SteamAPI_ISteamHTMLSurface_MouseDoubleClick
    ISteamHTMLSurface_MouseDoubleClick.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int ]
    ISteamHTMLSurface_MouseDoubleClick.restype = None

    global ISteamHTMLSurface_MouseMove
    ISteamHTMLSurface_MouseMove = dll.SteamAPI_ISteamHTMLSurface_MouseMove
    ISteamHTMLSurface_MouseMove.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int, c_int ]
    ISteamHTMLSurface_MouseMove.restype = None

    global ISteamHTMLSurface_MouseWheel
    ISteamHTMLSurface_MouseWheel = dll.SteamAPI_ISteamHTMLSurface_MouseWheel
    ISteamHTMLSurface_MouseWheel.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int ]
    ISteamHTMLSurface_MouseWheel.restype = None

    global ISteamHTMLSurface_KeyDown
    ISteamHTMLSurface_KeyDown = dll.SteamAPI_ISteamHTMLSurface_KeyDown
    ISteamHTMLSurface_KeyDown.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint, c_int, c_bool ]
    ISteamHTMLSurface_KeyDown.restype = None

    global ISteamHTMLSurface_KeyUp
    ISteamHTMLSurface_KeyUp = dll.SteamAPI_ISteamHTMLSurface_KeyUp
    ISteamHTMLSurface_KeyUp.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint, c_int ]
    ISteamHTMLSurface_KeyUp.restype = None

    global ISteamHTMLSurface_KeyChar
    ISteamHTMLSurface_KeyChar = dll.SteamAPI_ISteamHTMLSurface_KeyChar
    ISteamHTMLSurface_KeyChar.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint, c_int ]
    ISteamHTMLSurface_KeyChar.restype = None

    global ISteamHTMLSurface_SetHorizontalScroll
    ISteamHTMLSurface_SetHorizontalScroll = dll.SteamAPI_ISteamHTMLSurface_SetHorizontalScroll
    ISteamHTMLSurface_SetHorizontalScroll.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint ]
    ISteamHTMLSurface_SetHorizontalScroll.restype = None

    global ISteamHTMLSurface_SetVerticalScroll
    ISteamHTMLSurface_SetVerticalScroll = dll.SteamAPI_ISteamHTMLSurface_SetVerticalScroll
    ISteamHTMLSurface_SetVerticalScroll.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_uint ]
    ISteamHTMLSurface_SetVerticalScroll.restype = None

    global ISteamHTMLSurface_SetKeyFocus
    ISteamHTMLSurface_SetKeyFocus = dll.SteamAPI_ISteamHTMLSurface_SetKeyFocus
    ISteamHTMLSurface_SetKeyFocus.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_bool ]
    ISteamHTMLSurface_SetKeyFocus.restype = None

    global ISteamHTMLSurface_ViewSource
    ISteamHTMLSurface_ViewSource = dll.SteamAPI_ISteamHTMLSurface_ViewSource
    ISteamHTMLSurface_ViewSource.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_ViewSource.restype = None

    global ISteamHTMLSurface_CopyToClipboard
    ISteamHTMLSurface_CopyToClipboard = dll.SteamAPI_ISteamHTMLSurface_CopyToClipboard
    ISteamHTMLSurface_CopyToClipboard.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_CopyToClipboard.restype = None

    global ISteamHTMLSurface_PasteFromClipboard
    ISteamHTMLSurface_PasteFromClipboard = dll.SteamAPI_ISteamHTMLSurface_PasteFromClipboard
    ISteamHTMLSurface_PasteFromClipboard.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_PasteFromClipboard.restype = None

    global ISteamHTMLSurface_Find
    ISteamHTMLSurface_Find = dll.SteamAPI_ISteamHTMLSurface_Find
    ISteamHTMLSurface_Find.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_char_p, c_bool, c_bool ]
    ISteamHTMLSurface_Find.restype = None

    global ISteamHTMLSurface_StopFind
    ISteamHTMLSurface_StopFind = dll.SteamAPI_ISteamHTMLSurface_StopFind
    ISteamHTMLSurface_StopFind.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_StopFind.restype = None

    global ISteamHTMLSurface_GetLinkAtPosition
    ISteamHTMLSurface_GetLinkAtPosition = dll.SteamAPI_ISteamHTMLSurface_GetLinkAtPosition
    ISteamHTMLSurface_GetLinkAtPosition.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_int, c_int ]
    ISteamHTMLSurface_GetLinkAtPosition.restype = None

    global ISteamHTMLSurface_SetCookie
    ISteamHTMLSurface_SetCookie = dll.SteamAPI_ISteamHTMLSurface_SetCookie
    ISteamHTMLSurface_SetCookie.argtypes = [ POINTER(ISteamHTMLSurface), c_char_p, c_char_p, c_char_p, c_char_p, c_uint, c_bool, c_bool ]
    ISteamHTMLSurface_SetCookie.restype = None

    global ISteamHTMLSurface_SetPageScaleFactor
    ISteamHTMLSurface_SetPageScaleFactor = dll.SteamAPI_ISteamHTMLSurface_SetPageScaleFactor
    ISteamHTMLSurface_SetPageScaleFactor.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_float, c_int, c_int ]
    ISteamHTMLSurface_SetPageScaleFactor.restype = None

    global ISteamHTMLSurface_SetBackgroundMode
    ISteamHTMLSurface_SetBackgroundMode = dll.SteamAPI_ISteamHTMLSurface_SetBackgroundMode
    ISteamHTMLSurface_SetBackgroundMode.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_bool ]
    ISteamHTMLSurface_SetBackgroundMode.restype = None

    global ISteamHTMLSurface_SetDPIScalingFactor
    ISteamHTMLSurface_SetDPIScalingFactor = dll.SteamAPI_ISteamHTMLSurface_SetDPIScalingFactor
    ISteamHTMLSurface_SetDPIScalingFactor.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_float ]
    ISteamHTMLSurface_SetDPIScalingFactor.restype = None

    global ISteamHTMLSurface_OpenDeveloperTools
    ISteamHTMLSurface_OpenDeveloperTools = dll.SteamAPI_ISteamHTMLSurface_OpenDeveloperTools
    ISteamHTMLSurface_OpenDeveloperTools.argtypes = [ POINTER(ISteamHTMLSurface), c_uint ]
    ISteamHTMLSurface_OpenDeveloperTools.restype = None

    global ISteamHTMLSurface_AllowStartRequest
    ISteamHTMLSurface_AllowStartRequest = dll.SteamAPI_ISteamHTMLSurface_AllowStartRequest
    ISteamHTMLSurface_AllowStartRequest.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_bool ]
    ISteamHTMLSurface_AllowStartRequest.restype = None

    global ISteamHTMLSurface_JSDialogResponse
    ISteamHTMLSurface_JSDialogResponse = dll.SteamAPI_ISteamHTMLSurface_JSDialogResponse
    ISteamHTMLSurface_JSDialogResponse.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, c_bool ]
    ISteamHTMLSurface_JSDialogResponse.restype = None

    global ISteamHTMLSurface_FileLoadDialogResponse
    ISteamHTMLSurface_FileLoadDialogResponse = dll.SteamAPI_ISteamHTMLSurface_FileLoadDialogResponse
    ISteamHTMLSurface_FileLoadDialogResponse.argtypes = [ POINTER(ISteamHTMLSurface), c_uint, POINTER(c_char_p) ]
    ISteamHTMLSurface_FileLoadDialogResponse.restype = None

    global SteamHTMLSurface_v005
    SteamHTMLSurface_v005 = dll.SteamAPI_SteamHTMLSurface_v005
    SteamHTMLSurface_v005.argtypes = [ ]
    SteamHTMLSurface_v005.restype = POINTER(ISteamHTMLSurface)

    global ISteamInventory_GetResultStatus
    ISteamInventory_GetResultStatus = dll.SteamAPI_ISteamInventory_GetResultStatus
    ISteamInventory_GetResultStatus.argtypes = [ POINTER(ISteamInventory), c_int ]
    ISteamInventory_GetResultStatus.restype = EResult

    global ISteamInventory_GetResultItems
    ISteamInventory_GetResultItems = dll.SteamAPI_ISteamInventory_GetResultItems
    ISteamInventory_GetResultItems.argtypes = [ POINTER(ISteamInventory), c_int, POINTER(SteamItemDetails_t), POINTER(c_uint) ]
    ISteamInventory_GetResultItems.restype = c_bool

    global ISteamInventory_GetResultItemProperty
    ISteamInventory_GetResultItemProperty = dll.SteamAPI_ISteamInventory_GetResultItemProperty
    ISteamInventory_GetResultItemProperty.argtypes = [ POINTER(ISteamInventory), c_int, c_uint, c_char_p, c_char_p, POINTER(c_uint) ]
    ISteamInventory_GetResultItemProperty.restype = c_bool

    global ISteamInventory_GetResultTimestamp
    ISteamInventory_GetResultTimestamp = dll.SteamAPI_ISteamInventory_GetResultTimestamp
    ISteamInventory_GetResultTimestamp.argtypes = [ POINTER(ISteamInventory), c_int ]
    ISteamInventory_GetResultTimestamp.restype = c_uint

    global ISteamInventory_CheckResultSteamID
    ISteamInventory_CheckResultSteamID = dll.SteamAPI_ISteamInventory_CheckResultSteamID
    ISteamInventory_CheckResultSteamID.argtypes = [ POINTER(ISteamInventory), c_int, c_ulonglong ]
    ISteamInventory_CheckResultSteamID.restype = c_bool

    global ISteamInventory_DestroyResult
    ISteamInventory_DestroyResult = dll.SteamAPI_ISteamInventory_DestroyResult
    ISteamInventory_DestroyResult.argtypes = [ POINTER(ISteamInventory), c_int ]
    ISteamInventory_DestroyResult.restype = None

    global ISteamInventory_GetAllItems
    ISteamInventory_GetAllItems = dll.SteamAPI_ISteamInventory_GetAllItems
    ISteamInventory_GetAllItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int) ]
    ISteamInventory_GetAllItems.restype = c_bool

    global ISteamInventory_GetItemsByID
    ISteamInventory_GetItemsByID = dll.SteamAPI_ISteamInventory_GetItemsByID
    ISteamInventory_GetItemsByID.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_ulonglong), c_uint ]
    ISteamInventory_GetItemsByID.restype = c_bool

    global ISteamInventory_SerializeResult
    ISteamInventory_SerializeResult = dll.SteamAPI_ISteamInventory_SerializeResult
    ISteamInventory_SerializeResult.argtypes = [ POINTER(ISteamInventory), c_int, c_void_p, POINTER(c_uint) ]
    ISteamInventory_SerializeResult.restype = c_bool

    global ISteamInventory_DeserializeResult
    ISteamInventory_DeserializeResult = dll.SteamAPI_ISteamInventory_DeserializeResult
    ISteamInventory_DeserializeResult.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_void_p, c_uint, c_bool ]
    ISteamInventory_DeserializeResult.restype = c_bool

    global ISteamInventory_GenerateItems
    ISteamInventory_GenerateItems = dll.SteamAPI_ISteamInventory_GenerateItems
    ISteamInventory_GenerateItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_int), POINTER(c_uint), c_uint ]
    ISteamInventory_GenerateItems.restype = c_bool

    global ISteamInventory_GrantPromoItems
    ISteamInventory_GrantPromoItems = dll.SteamAPI_ISteamInventory_GrantPromoItems
    ISteamInventory_GrantPromoItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int) ]
    ISteamInventory_GrantPromoItems.restype = c_bool

    global ISteamInventory_AddPromoItem
    ISteamInventory_AddPromoItem = dll.SteamAPI_ISteamInventory_AddPromoItem
    ISteamInventory_AddPromoItem.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_int ]
    ISteamInventory_AddPromoItem.restype = c_bool

    global ISteamInventory_AddPromoItems
    ISteamInventory_AddPromoItems = dll.SteamAPI_ISteamInventory_AddPromoItems
    ISteamInventory_AddPromoItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_int), c_uint ]
    ISteamInventory_AddPromoItems.restype = c_bool

    global ISteamInventory_ConsumeItem
    ISteamInventory_ConsumeItem = dll.SteamAPI_ISteamInventory_ConsumeItem
    ISteamInventory_ConsumeItem.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_ulonglong, c_uint ]
    ISteamInventory_ConsumeItem.restype = c_bool

    global ISteamInventory_ExchangeItems
    ISteamInventory_ExchangeItems = dll.SteamAPI_ISteamInventory_ExchangeItems
    ISteamInventory_ExchangeItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_int), POINTER(c_uint), c_uint, POINTER(c_ulonglong), POINTER(c_uint), c_uint ]
    ISteamInventory_ExchangeItems.restype = c_bool

    global ISteamInventory_TransferItemQuantity
    ISteamInventory_TransferItemQuantity = dll.SteamAPI_ISteamInventory_TransferItemQuantity
    ISteamInventory_TransferItemQuantity.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_ulonglong, c_uint, c_ulonglong ]
    ISteamInventory_TransferItemQuantity.restype = c_bool

    global ISteamInventory_SendItemDropHeartbeat
    ISteamInventory_SendItemDropHeartbeat = dll.SteamAPI_ISteamInventory_SendItemDropHeartbeat
    ISteamInventory_SendItemDropHeartbeat.argtypes = [ POINTER(ISteamInventory),  ]
    ISteamInventory_SendItemDropHeartbeat.restype = None

    global ISteamInventory_TriggerItemDrop
    ISteamInventory_TriggerItemDrop = dll.SteamAPI_ISteamInventory_TriggerItemDrop
    ISteamInventory_TriggerItemDrop.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_int ]
    ISteamInventory_TriggerItemDrop.restype = c_bool

    global ISteamInventory_TradeItems
    ISteamInventory_TradeItems = dll.SteamAPI_ISteamInventory_TradeItems
    ISteamInventory_TradeItems.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_ulonglong, POINTER(c_ulonglong), POINTER(c_uint), c_uint, POINTER(c_ulonglong), POINTER(c_uint), c_uint ]
    ISteamInventory_TradeItems.restype = c_bool

    global ISteamInventory_LoadItemDefinitions
    ISteamInventory_LoadItemDefinitions = dll.SteamAPI_ISteamInventory_LoadItemDefinitions
    ISteamInventory_LoadItemDefinitions.argtypes = [ POINTER(ISteamInventory),  ]
    ISteamInventory_LoadItemDefinitions.restype = c_bool

    global ISteamInventory_GetItemDefinitionIDs
    ISteamInventory_GetItemDefinitionIDs = dll.SteamAPI_ISteamInventory_GetItemDefinitionIDs
    ISteamInventory_GetItemDefinitionIDs.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_uint) ]
    ISteamInventory_GetItemDefinitionIDs.restype = c_bool

    global ISteamInventory_GetItemDefinitionProperty
    ISteamInventory_GetItemDefinitionProperty = dll.SteamAPI_ISteamInventory_GetItemDefinitionProperty
    ISteamInventory_GetItemDefinitionProperty.argtypes = [ POINTER(ISteamInventory), c_int, c_char_p, c_char_p, POINTER(c_uint) ]
    ISteamInventory_GetItemDefinitionProperty.restype = c_bool

    global ISteamInventory_RequestEligiblePromoItemDefinitionsIDs
    ISteamInventory_RequestEligiblePromoItemDefinitionsIDs = dll.SteamAPI_ISteamInventory_RequestEligiblePromoItemDefinitionsIDs
    ISteamInventory_RequestEligiblePromoItemDefinitionsIDs.argtypes = [ POINTER(ISteamInventory), c_ulonglong ]
    ISteamInventory_RequestEligiblePromoItemDefinitionsIDs.restype = c_ulonglong

    global ISteamInventory_GetEligiblePromoItemDefinitionIDs
    ISteamInventory_GetEligiblePromoItemDefinitionIDs = dll.SteamAPI_ISteamInventory_GetEligiblePromoItemDefinitionIDs
    ISteamInventory_GetEligiblePromoItemDefinitionIDs.argtypes = [ POINTER(ISteamInventory), c_ulonglong, POINTER(c_int), POINTER(c_uint) ]
    ISteamInventory_GetEligiblePromoItemDefinitionIDs.restype = c_bool

    global ISteamInventory_StartPurchase
    ISteamInventory_StartPurchase = dll.SteamAPI_ISteamInventory_StartPurchase
    ISteamInventory_StartPurchase.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_uint), c_uint ]
    ISteamInventory_StartPurchase.restype = c_ulonglong

    global ISteamInventory_RequestPrices
    ISteamInventory_RequestPrices = dll.SteamAPI_ISteamInventory_RequestPrices
    ISteamInventory_RequestPrices.argtypes = [ POINTER(ISteamInventory),  ]
    ISteamInventory_RequestPrices.restype = c_ulonglong

    global ISteamInventory_GetNumItemsWithPrices
    ISteamInventory_GetNumItemsWithPrices = dll.SteamAPI_ISteamInventory_GetNumItemsWithPrices
    ISteamInventory_GetNumItemsWithPrices.argtypes = [ POINTER(ISteamInventory),  ]
    ISteamInventory_GetNumItemsWithPrices.restype = c_uint

    global ISteamInventory_GetItemsWithPrices
    ISteamInventory_GetItemsWithPrices = dll.SteamAPI_ISteamInventory_GetItemsWithPrices
    ISteamInventory_GetItemsWithPrices.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), POINTER(c_ulonglong), POINTER(c_ulonglong), c_uint ]
    ISteamInventory_GetItemsWithPrices.restype = c_bool

    global ISteamInventory_GetItemPrice
    ISteamInventory_GetItemPrice = dll.SteamAPI_ISteamInventory_GetItemPrice
    ISteamInventory_GetItemPrice.argtypes = [ POINTER(ISteamInventory), c_int, POINTER(c_ulonglong), POINTER(c_ulonglong) ]
    ISteamInventory_GetItemPrice.restype = c_bool

    global ISteamInventory_StartUpdateProperties
    ISteamInventory_StartUpdateProperties = dll.SteamAPI_ISteamInventory_StartUpdateProperties
    ISteamInventory_StartUpdateProperties.argtypes = [ POINTER(ISteamInventory),  ]
    ISteamInventory_StartUpdateProperties.restype = c_ulonglong

    global ISteamInventory_RemoveProperty
    ISteamInventory_RemoveProperty = dll.SteamAPI_ISteamInventory_RemoveProperty
    ISteamInventory_RemoveProperty.argtypes = [ POINTER(ISteamInventory), c_ulonglong, c_ulonglong, c_char_p ]
    ISteamInventory_RemoveProperty.restype = c_bool

    global ISteamInventory_SetPropertyString
    ISteamInventory_SetPropertyString = dll.SteamAPI_ISteamInventory_SetPropertyString
    ISteamInventory_SetPropertyString.argtypes = [ POINTER(ISteamInventory), c_ulonglong, c_ulonglong, c_char_p, c_char_p ]
    ISteamInventory_SetPropertyString.restype = c_bool

    global ISteamInventory_SetPropertyBool
    ISteamInventory_SetPropertyBool = dll.SteamAPI_ISteamInventory_SetPropertyBool
    ISteamInventory_SetPropertyBool.argtypes = [ POINTER(ISteamInventory), c_ulonglong, c_ulonglong, c_char_p, c_bool ]
    ISteamInventory_SetPropertyBool.restype = c_bool

    global ISteamInventory_SetPropertyInt64
    ISteamInventory_SetPropertyInt64 = dll.SteamAPI_ISteamInventory_SetPropertyInt64
    ISteamInventory_SetPropertyInt64.argtypes = [ POINTER(ISteamInventory), c_ulonglong, c_ulonglong, c_char_p, c_longlong ]
    ISteamInventory_SetPropertyInt64.restype = c_bool

    global ISteamInventory_SetPropertyFloat
    ISteamInventory_SetPropertyFloat = dll.SteamAPI_ISteamInventory_SetPropertyFloat
    ISteamInventory_SetPropertyFloat.argtypes = [ POINTER(ISteamInventory), c_ulonglong, c_ulonglong, c_char_p, c_float ]
    ISteamInventory_SetPropertyFloat.restype = c_bool

    global ISteamInventory_SubmitUpdateProperties
    ISteamInventory_SubmitUpdateProperties = dll.SteamAPI_ISteamInventory_SubmitUpdateProperties
    ISteamInventory_SubmitUpdateProperties.argtypes = [ POINTER(ISteamInventory), c_ulonglong, POINTER(c_int) ]
    ISteamInventory_SubmitUpdateProperties.restype = c_bool

    global ISteamInventory_InspectItem
    ISteamInventory_InspectItem = dll.SteamAPI_ISteamInventory_InspectItem
    ISteamInventory_InspectItem.argtypes = [ POINTER(ISteamInventory), POINTER(c_int), c_char_p ]
    ISteamInventory_InspectItem.restype = c_bool

    global SteamInventory_v003
    SteamInventory_v003 = dll.SteamAPI_SteamInventory_v003
    SteamInventory_v003.argtypes = [ ]
    SteamInventory_v003.restype = POINTER(ISteamInventory)

    global SteamGameServerInventory_v003
    SteamGameServerInventory_v003 = dll.SteamAPI_SteamGameServerInventory_v003
    SteamGameServerInventory_v003.argtypes = [ ]
    SteamGameServerInventory_v003.restype = POINTER(ISteamInventory)

    global ISteamVideo_GetVideoURL
    ISteamVideo_GetVideoURL = dll.SteamAPI_ISteamVideo_GetVideoURL
    ISteamVideo_GetVideoURL.argtypes = [ POINTER(ISteamVideo), c_uint ]
    ISteamVideo_GetVideoURL.restype = None

    global ISteamVideo_IsBroadcasting
    ISteamVideo_IsBroadcasting = dll.SteamAPI_ISteamVideo_IsBroadcasting
    ISteamVideo_IsBroadcasting.argtypes = [ POINTER(ISteamVideo), POINTER(c_int) ]
    ISteamVideo_IsBroadcasting.restype = c_bool

    global ISteamVideo_GetOPFSettings
    ISteamVideo_GetOPFSettings = dll.SteamAPI_ISteamVideo_GetOPFSettings
    ISteamVideo_GetOPFSettings.argtypes = [ POINTER(ISteamVideo), c_uint ]
    ISteamVideo_GetOPFSettings.restype = None

    global ISteamVideo_GetOPFStringForApp
    ISteamVideo_GetOPFStringForApp = dll.SteamAPI_ISteamVideo_GetOPFStringForApp
    ISteamVideo_GetOPFStringForApp.argtypes = [ POINTER(ISteamVideo), c_uint, c_char_p, POINTER(c_int) ]
    ISteamVideo_GetOPFStringForApp.restype = c_bool

    global SteamVideo_v002
    SteamVideo_v002 = dll.SteamAPI_SteamVideo_v002
    SteamVideo_v002.argtypes = [ ]
    SteamVideo_v002.restype = POINTER(ISteamVideo)

    global ISteamParentalSettings_BIsParentalLockEnabled
    ISteamParentalSettings_BIsParentalLockEnabled = dll.SteamAPI_ISteamParentalSettings_BIsParentalLockEnabled
    ISteamParentalSettings_BIsParentalLockEnabled.argtypes = [ POINTER(ISteamParentalSettings),  ]
    ISteamParentalSettings_BIsParentalLockEnabled.restype = c_bool

    global ISteamParentalSettings_BIsParentalLockLocked
    ISteamParentalSettings_BIsParentalLockLocked = dll.SteamAPI_ISteamParentalSettings_BIsParentalLockLocked
    ISteamParentalSettings_BIsParentalLockLocked.argtypes = [ POINTER(ISteamParentalSettings),  ]
    ISteamParentalSettings_BIsParentalLockLocked.restype = c_bool

    global ISteamParentalSettings_BIsAppBlocked
    ISteamParentalSettings_BIsAppBlocked = dll.SteamAPI_ISteamParentalSettings_BIsAppBlocked
    ISteamParentalSettings_BIsAppBlocked.argtypes = [ POINTER(ISteamParentalSettings), c_uint ]
    ISteamParentalSettings_BIsAppBlocked.restype = c_bool

    global ISteamParentalSettings_BIsAppInBlockList
    ISteamParentalSettings_BIsAppInBlockList = dll.SteamAPI_ISteamParentalSettings_BIsAppInBlockList
    ISteamParentalSettings_BIsAppInBlockList.argtypes = [ POINTER(ISteamParentalSettings), c_uint ]
    ISteamParentalSettings_BIsAppInBlockList.restype = c_bool

    global ISteamParentalSettings_BIsFeatureBlocked
    ISteamParentalSettings_BIsFeatureBlocked = dll.SteamAPI_ISteamParentalSettings_BIsFeatureBlocked
    ISteamParentalSettings_BIsFeatureBlocked.argtypes = [ POINTER(ISteamParentalSettings), EParentalFeature ]
    ISteamParentalSettings_BIsFeatureBlocked.restype = c_bool

    global ISteamParentalSettings_BIsFeatureInBlockList
    ISteamParentalSettings_BIsFeatureInBlockList = dll.SteamAPI_ISteamParentalSettings_BIsFeatureInBlockList
    ISteamParentalSettings_BIsFeatureInBlockList.argtypes = [ POINTER(ISteamParentalSettings), EParentalFeature ]
    ISteamParentalSettings_BIsFeatureInBlockList.restype = c_bool

    global SteamParentalSettings_v001
    SteamParentalSettings_v001 = dll.SteamAPI_SteamParentalSettings_v001
    SteamParentalSettings_v001.argtypes = [ ]
    SteamParentalSettings_v001.restype = POINTER(ISteamParentalSettings)

    global ISteamRemotePlay_GetSessionCount
    ISteamRemotePlay_GetSessionCount = dll.SteamAPI_ISteamRemotePlay_GetSessionCount
    ISteamRemotePlay_GetSessionCount.argtypes = [ POINTER(ISteamRemotePlay),  ]
    ISteamRemotePlay_GetSessionCount.restype = c_uint

    global ISteamRemotePlay_GetSessionID
    ISteamRemotePlay_GetSessionID = dll.SteamAPI_ISteamRemotePlay_GetSessionID
    ISteamRemotePlay_GetSessionID.argtypes = [ POINTER(ISteamRemotePlay), c_int ]
    ISteamRemotePlay_GetSessionID.restype = c_uint

    global ISteamRemotePlay_GetSessionSteamID
    ISteamRemotePlay_GetSessionSteamID = dll.SteamAPI_ISteamRemotePlay_GetSessionSteamID
    ISteamRemotePlay_GetSessionSteamID.argtypes = [ POINTER(ISteamRemotePlay), c_uint ]
    ISteamRemotePlay_GetSessionSteamID.restype = c_ulonglong

    global ISteamRemotePlay_GetSessionClientName
    ISteamRemotePlay_GetSessionClientName = dll.SteamAPI_ISteamRemotePlay_GetSessionClientName
    ISteamRemotePlay_GetSessionClientName.argtypes = [ POINTER(ISteamRemotePlay), c_uint ]
    ISteamRemotePlay_GetSessionClientName.restype = c_char_p

    global ISteamRemotePlay_GetSessionClientFormFactor
    ISteamRemotePlay_GetSessionClientFormFactor = dll.SteamAPI_ISteamRemotePlay_GetSessionClientFormFactor
    ISteamRemotePlay_GetSessionClientFormFactor.argtypes = [ POINTER(ISteamRemotePlay), c_uint ]
    ISteamRemotePlay_GetSessionClientFormFactor.restype = ESteamDeviceFormFactor

    global ISteamRemotePlay_BGetSessionClientResolution
    ISteamRemotePlay_BGetSessionClientResolution = dll.SteamAPI_ISteamRemotePlay_BGetSessionClientResolution
    ISteamRemotePlay_BGetSessionClientResolution.argtypes = [ POINTER(ISteamRemotePlay), c_uint, POINTER(c_int), POINTER(c_int) ]
    ISteamRemotePlay_BGetSessionClientResolution.restype = c_bool

    global ISteamRemotePlay_BSendRemotePlayTogetherInvite
    ISteamRemotePlay_BSendRemotePlayTogetherInvite = dll.SteamAPI_ISteamRemotePlay_BSendRemotePlayTogetherInvite
    ISteamRemotePlay_BSendRemotePlayTogetherInvite.argtypes = [ POINTER(ISteamRemotePlay), c_ulonglong ]
    ISteamRemotePlay_BSendRemotePlayTogetherInvite.restype = c_bool

    global SteamRemotePlay_v001
    SteamRemotePlay_v001 = dll.SteamAPI_SteamRemotePlay_v001
    SteamRemotePlay_v001.argtypes = [ ]
    SteamRemotePlay_v001.restype = POINTER(ISteamRemotePlay)

    global ISteamNetworkingMessages_SendMessageToUser
    ISteamNetworkingMessages_SendMessageToUser = dll.SteamAPI_ISteamNetworkingMessages_SendMessageToUser
    ISteamNetworkingMessages_SendMessageToUser.argtypes = [ POINTER(ISteamNetworkingMessages), POINTER(SteamNetworkingIdentity), c_void_p, c_uint, c_int, c_int ]
    ISteamNetworkingMessages_SendMessageToUser.restype = EResult

    global ISteamNetworkingMessages_ReceiveMessagesOnChannel
    ISteamNetworkingMessages_ReceiveMessagesOnChannel = dll.SteamAPI_ISteamNetworkingMessages_ReceiveMessagesOnChannel
    ISteamNetworkingMessages_ReceiveMessagesOnChannel.argtypes = [ POINTER(ISteamNetworkingMessages), c_int, POINTER(POINTER(SteamNetworkingMessage_t)), c_int ]
    ISteamNetworkingMessages_ReceiveMessagesOnChannel.restype = c_int

    global ISteamNetworkingMessages_AcceptSessionWithUser
    ISteamNetworkingMessages_AcceptSessionWithUser = dll.SteamAPI_ISteamNetworkingMessages_AcceptSessionWithUser
    ISteamNetworkingMessages_AcceptSessionWithUser.argtypes = [ POINTER(ISteamNetworkingMessages), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingMessages_AcceptSessionWithUser.restype = c_bool

    global ISteamNetworkingMessages_CloseSessionWithUser
    ISteamNetworkingMessages_CloseSessionWithUser = dll.SteamAPI_ISteamNetworkingMessages_CloseSessionWithUser
    ISteamNetworkingMessages_CloseSessionWithUser.argtypes = [ POINTER(ISteamNetworkingMessages), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingMessages_CloseSessionWithUser.restype = c_bool

    global ISteamNetworkingMessages_CloseChannelWithUser
    ISteamNetworkingMessages_CloseChannelWithUser = dll.SteamAPI_ISteamNetworkingMessages_CloseChannelWithUser
    ISteamNetworkingMessages_CloseChannelWithUser.argtypes = [ POINTER(ISteamNetworkingMessages), POINTER(SteamNetworkingIdentity), c_int ]
    ISteamNetworkingMessages_CloseChannelWithUser.restype = c_bool

    global ISteamNetworkingMessages_GetSessionConnectionInfo
    ISteamNetworkingMessages_GetSessionConnectionInfo = dll.SteamAPI_ISteamNetworkingMessages_GetSessionConnectionInfo
    ISteamNetworkingMessages_GetSessionConnectionInfo.argtypes = [ POINTER(ISteamNetworkingMessages), POINTER(SteamNetworkingIdentity), POINTER(SteamNetConnectionInfo_t), POINTER(SteamNetConnectionRealTimeStatus_t) ]
    ISteamNetworkingMessages_GetSessionConnectionInfo.restype = ESteamNetworkingConnectionState

    global SteamNetworkingMessages_SteamAPI_v002
    SteamNetworkingMessages_SteamAPI_v002 = dll.SteamAPI_SteamNetworkingMessages_SteamAPI_v002
    SteamNetworkingMessages_SteamAPI_v002.argtypes = [ ]
    SteamNetworkingMessages_SteamAPI_v002.restype = POINTER(ISteamNetworkingMessages)

    global SteamGameServerNetworkingMessages_SteamAPI_v002
    SteamGameServerNetworkingMessages_SteamAPI_v002 = dll.SteamAPI_SteamGameServerNetworkingMessages_SteamAPI_v002
    SteamGameServerNetworkingMessages_SteamAPI_v002.argtypes = [ ]
    SteamGameServerNetworkingMessages_SteamAPI_v002.restype = POINTER(ISteamNetworkingMessages)

    global ISteamNetworkingSockets_CreateListenSocketIP
    ISteamNetworkingSockets_CreateListenSocketIP = dll.SteamAPI_ISteamNetworkingSockets_CreateListenSocketIP
    ISteamNetworkingSockets_CreateListenSocketIP.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIPAddr), c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_CreateListenSocketIP.restype = c_uint

    global ISteamNetworkingSockets_ConnectByIPAddress
    ISteamNetworkingSockets_ConnectByIPAddress = dll.SteamAPI_ISteamNetworkingSockets_ConnectByIPAddress
    ISteamNetworkingSockets_ConnectByIPAddress.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIPAddr), c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_ConnectByIPAddress.restype = c_uint

    global ISteamNetworkingSockets_CreateListenSocketP2P
    ISteamNetworkingSockets_CreateListenSocketP2P = dll.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2P
    ISteamNetworkingSockets_CreateListenSocketP2P.argtypes = [ POINTER(ISteamNetworkingSockets), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_CreateListenSocketP2P.restype = c_uint

    global ISteamNetworkingSockets_ConnectP2P
    ISteamNetworkingSockets_ConnectP2P = dll.SteamAPI_ISteamNetworkingSockets_ConnectP2P
    ISteamNetworkingSockets_ConnectP2P.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIdentity), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_ConnectP2P.restype = c_uint

    global ISteamNetworkingSockets_AcceptConnection
    ISteamNetworkingSockets_AcceptConnection = dll.SteamAPI_ISteamNetworkingSockets_AcceptConnection
    ISteamNetworkingSockets_AcceptConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint ]
    ISteamNetworkingSockets_AcceptConnection.restype = EResult

    global ISteamNetworkingSockets_CloseConnection
    ISteamNetworkingSockets_CloseConnection = dll.SteamAPI_ISteamNetworkingSockets_CloseConnection
    ISteamNetworkingSockets_CloseConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_int, c_char_p, c_bool ]
    ISteamNetworkingSockets_CloseConnection.restype = c_bool

    global ISteamNetworkingSockets_CloseListenSocket
    ISteamNetworkingSockets_CloseListenSocket = dll.SteamAPI_ISteamNetworkingSockets_CloseListenSocket
    ISteamNetworkingSockets_CloseListenSocket.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint ]
    ISteamNetworkingSockets_CloseListenSocket.restype = c_bool

    global ISteamNetworkingSockets_SetConnectionUserData
    ISteamNetworkingSockets_SetConnectionUserData = dll.SteamAPI_ISteamNetworkingSockets_SetConnectionUserData
    ISteamNetworkingSockets_SetConnectionUserData.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_longlong ]
    ISteamNetworkingSockets_SetConnectionUserData.restype = c_bool

    global ISteamNetworkingSockets_GetConnectionUserData
    ISteamNetworkingSockets_GetConnectionUserData = dll.SteamAPI_ISteamNetworkingSockets_GetConnectionUserData
    ISteamNetworkingSockets_GetConnectionUserData.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint ]
    ISteamNetworkingSockets_GetConnectionUserData.restype = c_longlong

    global ISteamNetworkingSockets_SetConnectionName
    ISteamNetworkingSockets_SetConnectionName = dll.SteamAPI_ISteamNetworkingSockets_SetConnectionName
    ISteamNetworkingSockets_SetConnectionName.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_char_p ]
    ISteamNetworkingSockets_SetConnectionName.restype = None

    global ISteamNetworkingSockets_GetConnectionName
    ISteamNetworkingSockets_GetConnectionName = dll.SteamAPI_ISteamNetworkingSockets_GetConnectionName
    ISteamNetworkingSockets_GetConnectionName.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_char_p, c_int ]
    ISteamNetworkingSockets_GetConnectionName.restype = c_bool

    global ISteamNetworkingSockets_SendMessageToConnection
    ISteamNetworkingSockets_SendMessageToConnection = dll.SteamAPI_ISteamNetworkingSockets_SendMessageToConnection
    ISteamNetworkingSockets_SendMessageToConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_void_p, c_uint, c_int, POINTER(c_longlong) ]
    ISteamNetworkingSockets_SendMessageToConnection.restype = EResult

    global ISteamNetworkingSockets_SendMessages
    ISteamNetworkingSockets_SendMessages = dll.SteamAPI_ISteamNetworkingSockets_SendMessages
    ISteamNetworkingSockets_SendMessages.argtypes = [ POINTER(ISteamNetworkingSockets), c_int, POINTER(POINTER(SteamNetworkingMessage_t)), POINTER(c_longlong) ]
    ISteamNetworkingSockets_SendMessages.restype = None

    global ISteamNetworkingSockets_FlushMessagesOnConnection
    ISteamNetworkingSockets_FlushMessagesOnConnection = dll.SteamAPI_ISteamNetworkingSockets_FlushMessagesOnConnection
    ISteamNetworkingSockets_FlushMessagesOnConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint ]
    ISteamNetworkingSockets_FlushMessagesOnConnection.restype = EResult

    global ISteamNetworkingSockets_ReceiveMessagesOnConnection
    ISteamNetworkingSockets_ReceiveMessagesOnConnection = dll.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnConnection
    ISteamNetworkingSockets_ReceiveMessagesOnConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(POINTER(SteamNetworkingMessage_t)), c_int ]
    ISteamNetworkingSockets_ReceiveMessagesOnConnection.restype = c_int

    global ISteamNetworkingSockets_GetConnectionInfo
    ISteamNetworkingSockets_GetConnectionInfo = dll.SteamAPI_ISteamNetworkingSockets_GetConnectionInfo
    ISteamNetworkingSockets_GetConnectionInfo.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(SteamNetConnectionInfo_t) ]
    ISteamNetworkingSockets_GetConnectionInfo.restype = c_bool

    global ISteamNetworkingSockets_GetConnectionRealTimeStatus
    ISteamNetworkingSockets_GetConnectionRealTimeStatus = dll.SteamAPI_ISteamNetworkingSockets_GetConnectionRealTimeStatus
    ISteamNetworkingSockets_GetConnectionRealTimeStatus.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(SteamNetConnectionRealTimeStatus_t), c_int, POINTER(SteamNetConnectionRealTimeLaneStatus_t) ]
    ISteamNetworkingSockets_GetConnectionRealTimeStatus.restype = EResult

    global ISteamNetworkingSockets_GetDetailedConnectionStatus
    ISteamNetworkingSockets_GetDetailedConnectionStatus = dll.SteamAPI_ISteamNetworkingSockets_GetDetailedConnectionStatus
    ISteamNetworkingSockets_GetDetailedConnectionStatus.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_char_p, c_int ]
    ISteamNetworkingSockets_GetDetailedConnectionStatus.restype = c_int

    global ISteamNetworkingSockets_GetListenSocketAddress
    ISteamNetworkingSockets_GetListenSocketAddress = dll.SteamAPI_ISteamNetworkingSockets_GetListenSocketAddress
    ISteamNetworkingSockets_GetListenSocketAddress.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(SteamNetworkingIPAddr) ]
    ISteamNetworkingSockets_GetListenSocketAddress.restype = c_bool

    global ISteamNetworkingSockets_CreateSocketPair
    ISteamNetworkingSockets_CreateSocketPair = dll.SteamAPI_ISteamNetworkingSockets_CreateSocketPair
    ISteamNetworkingSockets_CreateSocketPair.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(c_uint), POINTER(c_uint), c_bool, POINTER(SteamNetworkingIdentity), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingSockets_CreateSocketPair.restype = c_bool

    global ISteamNetworkingSockets_ConfigureConnectionLanes
    ISteamNetworkingSockets_ConfigureConnectionLanes = dll.SteamAPI_ISteamNetworkingSockets_ConfigureConnectionLanes
    ISteamNetworkingSockets_ConfigureConnectionLanes.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_int, POINTER(c_int), POINTER(c_ushort) ]
    ISteamNetworkingSockets_ConfigureConnectionLanes.restype = EResult

    global ISteamNetworkingSockets_GetIdentity
    ISteamNetworkingSockets_GetIdentity = dll.SteamAPI_ISteamNetworkingSockets_GetIdentity
    ISteamNetworkingSockets_GetIdentity.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingSockets_GetIdentity.restype = c_bool

    global ISteamNetworkingSockets_InitAuthentication
    ISteamNetworkingSockets_InitAuthentication = dll.SteamAPI_ISteamNetworkingSockets_InitAuthentication
    ISteamNetworkingSockets_InitAuthentication.argtypes = [ POINTER(ISteamNetworkingSockets),  ]
    ISteamNetworkingSockets_InitAuthentication.restype = ESteamNetworkingAvailability

    global ISteamNetworkingSockets_GetAuthenticationStatus
    ISteamNetworkingSockets_GetAuthenticationStatus = dll.SteamAPI_ISteamNetworkingSockets_GetAuthenticationStatus
    ISteamNetworkingSockets_GetAuthenticationStatus.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetAuthenticationStatus_t) ]
    ISteamNetworkingSockets_GetAuthenticationStatus.restype = ESteamNetworkingAvailability

    global ISteamNetworkingSockets_CreatePollGroup
    ISteamNetworkingSockets_CreatePollGroup = dll.SteamAPI_ISteamNetworkingSockets_CreatePollGroup
    ISteamNetworkingSockets_CreatePollGroup.argtypes = [ POINTER(ISteamNetworkingSockets),  ]
    ISteamNetworkingSockets_CreatePollGroup.restype = c_uint

    global ISteamNetworkingSockets_DestroyPollGroup
    ISteamNetworkingSockets_DestroyPollGroup = dll.SteamAPI_ISteamNetworkingSockets_DestroyPollGroup
    ISteamNetworkingSockets_DestroyPollGroup.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint ]
    ISteamNetworkingSockets_DestroyPollGroup.restype = c_bool

    global ISteamNetworkingSockets_SetConnectionPollGroup
    ISteamNetworkingSockets_SetConnectionPollGroup = dll.SteamAPI_ISteamNetworkingSockets_SetConnectionPollGroup
    ISteamNetworkingSockets_SetConnectionPollGroup.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, c_uint ]
    ISteamNetworkingSockets_SetConnectionPollGroup.restype = c_bool

    global ISteamNetworkingSockets_ReceiveMessagesOnPollGroup
    ISteamNetworkingSockets_ReceiveMessagesOnPollGroup = dll.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnPollGroup
    ISteamNetworkingSockets_ReceiveMessagesOnPollGroup.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(POINTER(SteamNetworkingMessage_t)), c_int ]
    ISteamNetworkingSockets_ReceiveMessagesOnPollGroup.restype = c_int

    global ISteamNetworkingSockets_ReceivedRelayAuthTicket
    ISteamNetworkingSockets_ReceivedRelayAuthTicket = dll.SteamAPI_ISteamNetworkingSockets_ReceivedRelayAuthTicket
    ISteamNetworkingSockets_ReceivedRelayAuthTicket.argtypes = [ POINTER(ISteamNetworkingSockets), c_void_p, c_int, c_void_p ]
    ISteamNetworkingSockets_ReceivedRelayAuthTicket.restype = c_bool

    global ISteamNetworkingSockets_FindRelayAuthTicketForServer
    ISteamNetworkingSockets_FindRelayAuthTicketForServer = dll.SteamAPI_ISteamNetworkingSockets_FindRelayAuthTicketForServer
    ISteamNetworkingSockets_FindRelayAuthTicketForServer.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIdentity), c_int, c_void_p ]
    ISteamNetworkingSockets_FindRelayAuthTicketForServer.restype = c_int

    global ISteamNetworkingSockets_ConnectToHostedDedicatedServer
    ISteamNetworkingSockets_ConnectToHostedDedicatedServer = dll.SteamAPI_ISteamNetworkingSockets_ConnectToHostedDedicatedServer
    ISteamNetworkingSockets_ConnectToHostedDedicatedServer.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIdentity), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_ConnectToHostedDedicatedServer.restype = c_uint

    global ISteamNetworkingSockets_GetHostedDedicatedServerPort
    ISteamNetworkingSockets_GetHostedDedicatedServerPort = dll.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPort
    ISteamNetworkingSockets_GetHostedDedicatedServerPort.argtypes = [ POINTER(ISteamNetworkingSockets),  ]
    ISteamNetworkingSockets_GetHostedDedicatedServerPort.restype = c_ushort

    global ISteamNetworkingSockets_GetHostedDedicatedServerPOPID
    ISteamNetworkingSockets_GetHostedDedicatedServerPOPID = dll.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPOPID
    ISteamNetworkingSockets_GetHostedDedicatedServerPOPID.argtypes = [ POINTER(ISteamNetworkingSockets),  ]
    ISteamNetworkingSockets_GetHostedDedicatedServerPOPID.restype = c_uint

    global ISteamNetworkingSockets_GetHostedDedicatedServerAddress
    ISteamNetworkingSockets_GetHostedDedicatedServerAddress = dll.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerAddress
    ISteamNetworkingSockets_GetHostedDedicatedServerAddress.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamDatagramHostedAddress) ]
    ISteamNetworkingSockets_GetHostedDedicatedServerAddress.restype = EResult

    global ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket
    ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket = dll.SteamAPI_ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket
    ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket.argtypes = [ POINTER(ISteamNetworkingSockets), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket.restype = c_uint

    global ISteamNetworkingSockets_GetGameCoordinatorServerLogin
    ISteamNetworkingSockets_GetGameCoordinatorServerLogin = dll.SteamAPI_ISteamNetworkingSockets_GetGameCoordinatorServerLogin
    ISteamNetworkingSockets_GetGameCoordinatorServerLogin.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamDatagramGameCoordinatorServerLogin), POINTER(c_int), c_void_p ]
    ISteamNetworkingSockets_GetGameCoordinatorServerLogin.restype = EResult

    global ISteamNetworkingSockets_ConnectP2PCustomSignaling
    ISteamNetworkingSockets_ConnectP2PCustomSignaling = dll.SteamAPI_ISteamNetworkingSockets_ConnectP2PCustomSignaling
    ISteamNetworkingSockets_ConnectP2PCustomSignaling.argtypes = [ POINTER(ISteamNetworkingSockets), c_void_p, POINTER(SteamNetworkingIdentity), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_ConnectP2PCustomSignaling.restype = c_uint

    global ISteamNetworkingSockets_ReceivedP2PCustomSignal
    ISteamNetworkingSockets_ReceivedP2PCustomSignal = dll.SteamAPI_ISteamNetworkingSockets_ReceivedP2PCustomSignal
    ISteamNetworkingSockets_ReceivedP2PCustomSignal.argtypes = [ POINTER(ISteamNetworkingSockets), c_void_p, c_int, c_void_p ]
    ISteamNetworkingSockets_ReceivedP2PCustomSignal.restype = c_bool

    global ISteamNetworkingSockets_GetCertificateRequest
    ISteamNetworkingSockets_GetCertificateRequest = dll.SteamAPI_ISteamNetworkingSockets_GetCertificateRequest
    ISteamNetworkingSockets_GetCertificateRequest.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(c_int), c_void_p, POINTER((c_byte * 1024)) ]
    ISteamNetworkingSockets_GetCertificateRequest.restype = c_bool

    global ISteamNetworkingSockets_SetCertificate
    ISteamNetworkingSockets_SetCertificate = dll.SteamAPI_ISteamNetworkingSockets_SetCertificate
    ISteamNetworkingSockets_SetCertificate.argtypes = [ POINTER(ISteamNetworkingSockets), c_void_p, c_int, POINTER((c_byte * 1024)) ]
    ISteamNetworkingSockets_SetCertificate.restype = c_bool

    global ISteamNetworkingSockets_ResetIdentity
    ISteamNetworkingSockets_ResetIdentity = dll.SteamAPI_ISteamNetworkingSockets_ResetIdentity
    ISteamNetworkingSockets_ResetIdentity.argtypes = [ POINTER(ISteamNetworkingSockets), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingSockets_ResetIdentity.restype = None

    global ISteamNetworkingSockets_RunCallbacks
    ISteamNetworkingSockets_RunCallbacks = dll.SteamAPI_ISteamNetworkingSockets_RunCallbacks
    ISteamNetworkingSockets_RunCallbacks.argtypes = [ POINTER(ISteamNetworkingSockets),  ]
    ISteamNetworkingSockets_RunCallbacks.restype = None

    global ISteamNetworkingSockets_BeginAsyncRequestFakeIP
    ISteamNetworkingSockets_BeginAsyncRequestFakeIP = dll.SteamAPI_ISteamNetworkingSockets_BeginAsyncRequestFakeIP
    ISteamNetworkingSockets_BeginAsyncRequestFakeIP.argtypes = [ POINTER(ISteamNetworkingSockets), c_int ]
    ISteamNetworkingSockets_BeginAsyncRequestFakeIP.restype = c_bool

    global ISteamNetworkingSockets_GetFakeIP
    ISteamNetworkingSockets_GetFakeIP = dll.SteamAPI_ISteamNetworkingSockets_GetFakeIP
    ISteamNetworkingSockets_GetFakeIP.argtypes = [ POINTER(ISteamNetworkingSockets), c_int, POINTER(SteamNetworkingFakeIPResult_t) ]
    ISteamNetworkingSockets_GetFakeIP.restype = None

    global ISteamNetworkingSockets_CreateListenSocketP2PFakeIP
    ISteamNetworkingSockets_CreateListenSocketP2PFakeIP = dll.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2PFakeIP
    ISteamNetworkingSockets_CreateListenSocketP2PFakeIP.argtypes = [ POINTER(ISteamNetworkingSockets), c_int, c_int, POINTER(SteamNetworkingConfigValue_t) ]
    ISteamNetworkingSockets_CreateListenSocketP2PFakeIP.restype = c_uint

    global ISteamNetworkingSockets_GetRemoteFakeIPForConnection
    ISteamNetworkingSockets_GetRemoteFakeIPForConnection = dll.SteamAPI_ISteamNetworkingSockets_GetRemoteFakeIPForConnection
    ISteamNetworkingSockets_GetRemoteFakeIPForConnection.argtypes = [ POINTER(ISteamNetworkingSockets), c_uint, POINTER(SteamNetworkingIPAddr) ]
    ISteamNetworkingSockets_GetRemoteFakeIPForConnection.restype = EResult

    global ISteamNetworkingSockets_CreateFakeUDPPort
    ISteamNetworkingSockets_CreateFakeUDPPort = dll.SteamAPI_ISteamNetworkingSockets_CreateFakeUDPPort
    ISteamNetworkingSockets_CreateFakeUDPPort.argtypes = [ POINTER(ISteamNetworkingSockets), c_int ]
    ISteamNetworkingSockets_CreateFakeUDPPort.restype = POINTER(ISteamNetworkingFakeUDPPort)

    global SteamNetworkingSockets_SteamAPI_v012
    SteamNetworkingSockets_SteamAPI_v012 = dll.SteamAPI_SteamNetworkingSockets_SteamAPI_v012
    SteamNetworkingSockets_SteamAPI_v012.argtypes = [ ]
    SteamNetworkingSockets_SteamAPI_v012.restype = POINTER(ISteamNetworkingSockets)

    global SteamGameServerNetworkingSockets_SteamAPI_v012
    SteamGameServerNetworkingSockets_SteamAPI_v012 = dll.SteamAPI_SteamGameServerNetworkingSockets_SteamAPI_v012
    SteamGameServerNetworkingSockets_SteamAPI_v012.argtypes = [ ]
    SteamGameServerNetworkingSockets_SteamAPI_v012.restype = POINTER(ISteamNetworkingSockets)

    global ISteamNetworkingUtils_AllocateMessage
    ISteamNetworkingUtils_AllocateMessage = dll.SteamAPI_ISteamNetworkingUtils_AllocateMessage
    ISteamNetworkingUtils_AllocateMessage.argtypes = [ POINTER(ISteamNetworkingUtils), c_int ]
    ISteamNetworkingUtils_AllocateMessage.restype = POINTER(SteamNetworkingMessage_t)

    global ISteamNetworkingUtils_InitRelayNetworkAccess
    ISteamNetworkingUtils_InitRelayNetworkAccess = dll.SteamAPI_ISteamNetworkingUtils_InitRelayNetworkAccess
    ISteamNetworkingUtils_InitRelayNetworkAccess.argtypes = [ POINTER(ISteamNetworkingUtils),  ]
    ISteamNetworkingUtils_InitRelayNetworkAccess.restype = None

    global ISteamNetworkingUtils_GetRelayNetworkStatus
    ISteamNetworkingUtils_GetRelayNetworkStatus = dll.SteamAPI_ISteamNetworkingUtils_GetRelayNetworkStatus
    ISteamNetworkingUtils_GetRelayNetworkStatus.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamRelayNetworkStatus_t) ]
    ISteamNetworkingUtils_GetRelayNetworkStatus.restype = ESteamNetworkingAvailability

    global ISteamNetworkingUtils_GetLocalPingLocation
    ISteamNetworkingUtils_GetLocalPingLocation = dll.SteamAPI_ISteamNetworkingUtils_GetLocalPingLocation
    ISteamNetworkingUtils_GetLocalPingLocation.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkPingLocation_t) ]
    ISteamNetworkingUtils_GetLocalPingLocation.restype = c_float

    global ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations
    ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations = dll.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations
    ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkPingLocation_t), POINTER(SteamNetworkPingLocation_t) ]
    ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations.restype = c_int

    global ISteamNetworkingUtils_EstimatePingTimeFromLocalHost
    ISteamNetworkingUtils_EstimatePingTimeFromLocalHost = dll.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeFromLocalHost
    ISteamNetworkingUtils_EstimatePingTimeFromLocalHost.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkPingLocation_t) ]
    ISteamNetworkingUtils_EstimatePingTimeFromLocalHost.restype = c_int

    global ISteamNetworkingUtils_ConvertPingLocationToString
    ISteamNetworkingUtils_ConvertPingLocationToString = dll.SteamAPI_ISteamNetworkingUtils_ConvertPingLocationToString
    ISteamNetworkingUtils_ConvertPingLocationToString.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkPingLocation_t), c_char_p, c_int ]
    ISteamNetworkingUtils_ConvertPingLocationToString.restype = None

    global ISteamNetworkingUtils_ParsePingLocationString
    ISteamNetworkingUtils_ParsePingLocationString = dll.SteamAPI_ISteamNetworkingUtils_ParsePingLocationString
    ISteamNetworkingUtils_ParsePingLocationString.argtypes = [ POINTER(ISteamNetworkingUtils), c_char_p, POINTER(SteamNetworkPingLocation_t) ]
    ISteamNetworkingUtils_ParsePingLocationString.restype = c_bool

    global ISteamNetworkingUtils_CheckPingDataUpToDate
    ISteamNetworkingUtils_CheckPingDataUpToDate = dll.SteamAPI_ISteamNetworkingUtils_CheckPingDataUpToDate
    ISteamNetworkingUtils_CheckPingDataUpToDate.argtypes = [ POINTER(ISteamNetworkingUtils), c_float ]
    ISteamNetworkingUtils_CheckPingDataUpToDate.restype = c_bool

    global ISteamNetworkingUtils_GetPingToDataCenter
    ISteamNetworkingUtils_GetPingToDataCenter = dll.SteamAPI_ISteamNetworkingUtils_GetPingToDataCenter
    ISteamNetworkingUtils_GetPingToDataCenter.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint, POINTER(c_uint) ]
    ISteamNetworkingUtils_GetPingToDataCenter.restype = c_int

    global ISteamNetworkingUtils_GetDirectPingToPOP
    ISteamNetworkingUtils_GetDirectPingToPOP = dll.SteamAPI_ISteamNetworkingUtils_GetDirectPingToPOP
    ISteamNetworkingUtils_GetDirectPingToPOP.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint ]
    ISteamNetworkingUtils_GetDirectPingToPOP.restype = c_int

    global ISteamNetworkingUtils_GetPOPCount
    ISteamNetworkingUtils_GetPOPCount = dll.SteamAPI_ISteamNetworkingUtils_GetPOPCount
    ISteamNetworkingUtils_GetPOPCount.argtypes = [ POINTER(ISteamNetworkingUtils),  ]
    ISteamNetworkingUtils_GetPOPCount.restype = c_int

    global ISteamNetworkingUtils_GetPOPList
    ISteamNetworkingUtils_GetPOPList = dll.SteamAPI_ISteamNetworkingUtils_GetPOPList
    ISteamNetworkingUtils_GetPOPList.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(c_uint), c_int ]
    ISteamNetworkingUtils_GetPOPList.restype = c_int

    global ISteamNetworkingUtils_GetLocalTimestamp
    ISteamNetworkingUtils_GetLocalTimestamp = dll.SteamAPI_ISteamNetworkingUtils_GetLocalTimestamp
    ISteamNetworkingUtils_GetLocalTimestamp.argtypes = [ POINTER(ISteamNetworkingUtils),  ]
    ISteamNetworkingUtils_GetLocalTimestamp.restype = c_longlong

    global ISteamNetworkingUtils_SetDebugOutputFunction
    ISteamNetworkingUtils_SetDebugOutputFunction = dll.SteamAPI_ISteamNetworkingUtils_SetDebugOutputFunction
    ISteamNetworkingUtils_SetDebugOutputFunction.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingSocketsDebugOutputType, c_void_p ]
    ISteamNetworkingUtils_SetDebugOutputFunction.restype = None

    global ISteamNetworkingUtils_IsFakeIPv4
    ISteamNetworkingUtils_IsFakeIPv4 = dll.SteamAPI_ISteamNetworkingUtils_IsFakeIPv4
    ISteamNetworkingUtils_IsFakeIPv4.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint ]
    ISteamNetworkingUtils_IsFakeIPv4.restype = c_bool

    global ISteamNetworkingUtils_GetIPv4FakeIPType
    ISteamNetworkingUtils_GetIPv4FakeIPType = dll.SteamAPI_ISteamNetworkingUtils_GetIPv4FakeIPType
    ISteamNetworkingUtils_GetIPv4FakeIPType.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint ]
    ISteamNetworkingUtils_GetIPv4FakeIPType.restype = ESteamNetworkingFakeIPType

    global ISteamNetworkingUtils_GetRealIdentityForFakeIP
    ISteamNetworkingUtils_GetRealIdentityForFakeIP = dll.SteamAPI_ISteamNetworkingUtils_GetRealIdentityForFakeIP
    ISteamNetworkingUtils_GetRealIdentityForFakeIP.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIPAddr), POINTER(SteamNetworkingIdentity) ]
    ISteamNetworkingUtils_GetRealIdentityForFakeIP.restype = EResult

    global ISteamNetworkingUtils_SetGlobalConfigValueInt32
    ISteamNetworkingUtils_SetGlobalConfigValueInt32 = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueInt32
    ISteamNetworkingUtils_SetGlobalConfigValueInt32.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, c_int ]
    ISteamNetworkingUtils_SetGlobalConfigValueInt32.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalConfigValueFloat
    ISteamNetworkingUtils_SetGlobalConfigValueFloat = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueFloat
    ISteamNetworkingUtils_SetGlobalConfigValueFloat.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, c_float ]
    ISteamNetworkingUtils_SetGlobalConfigValueFloat.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalConfigValueString
    ISteamNetworkingUtils_SetGlobalConfigValueString = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueString
    ISteamNetworkingUtils_SetGlobalConfigValueString.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, c_char_p ]
    ISteamNetworkingUtils_SetGlobalConfigValueString.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalConfigValuePtr
    ISteamNetworkingUtils_SetGlobalConfigValuePtr = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValuePtr
    ISteamNetworkingUtils_SetGlobalConfigValuePtr.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, c_void_p ]
    ISteamNetworkingUtils_SetGlobalConfigValuePtr.restype = c_bool

    global ISteamNetworkingUtils_SetConnectionConfigValueInt32
    ISteamNetworkingUtils_SetConnectionConfigValueInt32 = dll.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueInt32
    ISteamNetworkingUtils_SetConnectionConfigValueInt32.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint, ESteamNetworkingConfigValue, c_int ]
    ISteamNetworkingUtils_SetConnectionConfigValueInt32.restype = c_bool

    global ISteamNetworkingUtils_SetConnectionConfigValueFloat
    ISteamNetworkingUtils_SetConnectionConfigValueFloat = dll.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueFloat
    ISteamNetworkingUtils_SetConnectionConfigValueFloat.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint, ESteamNetworkingConfigValue, c_float ]
    ISteamNetworkingUtils_SetConnectionConfigValueFloat.restype = c_bool

    global ISteamNetworkingUtils_SetConnectionConfigValueString
    ISteamNetworkingUtils_SetConnectionConfigValueString = dll.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueString
    ISteamNetworkingUtils_SetConnectionConfigValueString.argtypes = [ POINTER(ISteamNetworkingUtils), c_uint, ESteamNetworkingConfigValue, c_char_p ]
    ISteamNetworkingUtils_SetConnectionConfigValueString.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged
    ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult
    ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult
    ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest.restype = c_bool

    global ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed = dll.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed.argtypes = [ POINTER(ISteamNetworkingUtils), c_void_p ]
    ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed.restype = c_bool

    global ISteamNetworkingUtils_SetConfigValue
    ISteamNetworkingUtils_SetConfigValue = dll.SteamAPI_ISteamNetworkingUtils_SetConfigValue
    ISteamNetworkingUtils_SetConfigValue.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, ESteamNetworkingConfigScope, POINTER(c_int), ESteamNetworkingConfigDataType, c_void_p ]
    ISteamNetworkingUtils_SetConfigValue.restype = c_bool

    global ISteamNetworkingUtils_SetConfigValueStruct
    ISteamNetworkingUtils_SetConfigValueStruct = dll.SteamAPI_ISteamNetworkingUtils_SetConfigValueStruct
    ISteamNetworkingUtils_SetConfigValueStruct.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingConfigValue_t), ESteamNetworkingConfigScope, POINTER(c_int) ]
    ISteamNetworkingUtils_SetConfigValueStruct.restype = c_bool

    global ISteamNetworkingUtils_GetConfigValue
    ISteamNetworkingUtils_GetConfigValue = dll.SteamAPI_ISteamNetworkingUtils_GetConfigValue
    ISteamNetworkingUtils_GetConfigValue.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, ESteamNetworkingConfigScope, POINTER(c_int), POINTER(ESteamNetworkingConfigDataType), c_void_p, POINTER(c_size_t) ]
    ISteamNetworkingUtils_GetConfigValue.restype = ESteamNetworkingGetConfigValueResult

    global ISteamNetworkingUtils_GetConfigValueInfo
    ISteamNetworkingUtils_GetConfigValueInfo = dll.SteamAPI_ISteamNetworkingUtils_GetConfigValueInfo
    ISteamNetworkingUtils_GetConfigValueInfo.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, POINTER(ESteamNetworkingConfigDataType), POINTER(ESteamNetworkingConfigScope) ]
    ISteamNetworkingUtils_GetConfigValueInfo.restype = c_char_p

    global ISteamNetworkingUtils_IterateGenericEditableConfigValues
    ISteamNetworkingUtils_IterateGenericEditableConfigValues = dll.SteamAPI_ISteamNetworkingUtils_IterateGenericEditableConfigValues
    ISteamNetworkingUtils_IterateGenericEditableConfigValues.argtypes = [ POINTER(ISteamNetworkingUtils), ESteamNetworkingConfigValue, c_bool ]
    ISteamNetworkingUtils_IterateGenericEditableConfigValues.restype = ESteamNetworkingConfigValue

    global ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString = dll.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIPAddr), c_char_p, c_uint, c_bool ]
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString.restype = None

    global ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString = dll.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIPAddr), c_char_p ]
    ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString.restype = c_bool

    global ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType
    ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType = dll.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType
    ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIPAddr) ]
    ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType.restype = ESteamNetworkingFakeIPType

    global ISteamNetworkingUtils_SteamNetworkingIdentity_ToString
    ISteamNetworkingUtils_SteamNetworkingIdentity_ToString = dll.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ToString
    ISteamNetworkingUtils_SteamNetworkingIdentity_ToString.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIdentity), c_char_p, c_uint ]
    ISteamNetworkingUtils_SteamNetworkingIdentity_ToString.restype = None

    global ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString
    ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString = dll.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString
    ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString.argtypes = [ POINTER(ISteamNetworkingUtils), POINTER(SteamNetworkingIdentity), c_char_p ]
    ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString.restype = c_bool

    global SteamNetworkingUtils_SteamAPI_v004
    SteamNetworkingUtils_SteamAPI_v004 = dll.SteamAPI_SteamNetworkingUtils_SteamAPI_v004
    SteamNetworkingUtils_SteamAPI_v004.argtypes = [ ]
    SteamNetworkingUtils_SteamAPI_v004.restype = POINTER(ISteamNetworkingUtils)

    global ISteamGameServer_SetProduct
    ISteamGameServer_SetProduct = dll.SteamAPI_ISteamGameServer_SetProduct
    ISteamGameServer_SetProduct.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetProduct.restype = None

    global ISteamGameServer_SetGameDescription
    ISteamGameServer_SetGameDescription = dll.SteamAPI_ISteamGameServer_SetGameDescription
    ISteamGameServer_SetGameDescription.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetGameDescription.restype = None

    global ISteamGameServer_SetModDir
    ISteamGameServer_SetModDir = dll.SteamAPI_ISteamGameServer_SetModDir
    ISteamGameServer_SetModDir.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetModDir.restype = None

    global ISteamGameServer_SetDedicatedServer
    ISteamGameServer_SetDedicatedServer = dll.SteamAPI_ISteamGameServer_SetDedicatedServer
    ISteamGameServer_SetDedicatedServer.argtypes = [ POINTER(ISteamGameServer), c_bool ]
    ISteamGameServer_SetDedicatedServer.restype = None

    global ISteamGameServer_LogOn
    ISteamGameServer_LogOn = dll.SteamAPI_ISteamGameServer_LogOn
    ISteamGameServer_LogOn.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_LogOn.restype = None

    global ISteamGameServer_LogOnAnonymous
    ISteamGameServer_LogOnAnonymous = dll.SteamAPI_ISteamGameServer_LogOnAnonymous
    ISteamGameServer_LogOnAnonymous.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_LogOnAnonymous.restype = None

    global ISteamGameServer_LogOff
    ISteamGameServer_LogOff = dll.SteamAPI_ISteamGameServer_LogOff
    ISteamGameServer_LogOff.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_LogOff.restype = None

    global ISteamGameServer_BLoggedOn
    ISteamGameServer_BLoggedOn = dll.SteamAPI_ISteamGameServer_BLoggedOn
    ISteamGameServer_BLoggedOn.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_BLoggedOn.restype = c_bool

    global ISteamGameServer_BSecure
    ISteamGameServer_BSecure = dll.SteamAPI_ISteamGameServer_BSecure
    ISteamGameServer_BSecure.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_BSecure.restype = c_bool

    global ISteamGameServer_GetSteamID
    ISteamGameServer_GetSteamID = dll.SteamAPI_ISteamGameServer_GetSteamID
    ISteamGameServer_GetSteamID.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_GetSteamID.restype = c_ulonglong

    global ISteamGameServer_WasRestartRequested
    ISteamGameServer_WasRestartRequested = dll.SteamAPI_ISteamGameServer_WasRestartRequested
    ISteamGameServer_WasRestartRequested.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_WasRestartRequested.restype = c_bool

    global ISteamGameServer_SetMaxPlayerCount
    ISteamGameServer_SetMaxPlayerCount = dll.SteamAPI_ISteamGameServer_SetMaxPlayerCount
    ISteamGameServer_SetMaxPlayerCount.argtypes = [ POINTER(ISteamGameServer), c_int ]
    ISteamGameServer_SetMaxPlayerCount.restype = None

    global ISteamGameServer_SetBotPlayerCount
    ISteamGameServer_SetBotPlayerCount = dll.SteamAPI_ISteamGameServer_SetBotPlayerCount
    ISteamGameServer_SetBotPlayerCount.argtypes = [ POINTER(ISteamGameServer), c_int ]
    ISteamGameServer_SetBotPlayerCount.restype = None

    global ISteamGameServer_SetServerName
    ISteamGameServer_SetServerName = dll.SteamAPI_ISteamGameServer_SetServerName
    ISteamGameServer_SetServerName.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetServerName.restype = None

    global ISteamGameServer_SetMapName
    ISteamGameServer_SetMapName = dll.SteamAPI_ISteamGameServer_SetMapName
    ISteamGameServer_SetMapName.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetMapName.restype = None

    global ISteamGameServer_SetPasswordProtected
    ISteamGameServer_SetPasswordProtected = dll.SteamAPI_ISteamGameServer_SetPasswordProtected
    ISteamGameServer_SetPasswordProtected.argtypes = [ POINTER(ISteamGameServer), c_bool ]
    ISteamGameServer_SetPasswordProtected.restype = None

    global ISteamGameServer_SetSpectatorPort
    ISteamGameServer_SetSpectatorPort = dll.SteamAPI_ISteamGameServer_SetSpectatorPort
    ISteamGameServer_SetSpectatorPort.argtypes = [ POINTER(ISteamGameServer), c_ushort ]
    ISteamGameServer_SetSpectatorPort.restype = None

    global ISteamGameServer_SetSpectatorServerName
    ISteamGameServer_SetSpectatorServerName = dll.SteamAPI_ISteamGameServer_SetSpectatorServerName
    ISteamGameServer_SetSpectatorServerName.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetSpectatorServerName.restype = None

    global ISteamGameServer_ClearAllKeyValues
    ISteamGameServer_ClearAllKeyValues = dll.SteamAPI_ISteamGameServer_ClearAllKeyValues
    ISteamGameServer_ClearAllKeyValues.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_ClearAllKeyValues.restype = None

    global ISteamGameServer_SetKeyValue
    ISteamGameServer_SetKeyValue = dll.SteamAPI_ISteamGameServer_SetKeyValue
    ISteamGameServer_SetKeyValue.argtypes = [ POINTER(ISteamGameServer), c_char_p, c_char_p ]
    ISteamGameServer_SetKeyValue.restype = None

    global ISteamGameServer_SetGameTags
    ISteamGameServer_SetGameTags = dll.SteamAPI_ISteamGameServer_SetGameTags
    ISteamGameServer_SetGameTags.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetGameTags.restype = None

    global ISteamGameServer_SetGameData
    ISteamGameServer_SetGameData = dll.SteamAPI_ISteamGameServer_SetGameData
    ISteamGameServer_SetGameData.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetGameData.restype = None

    global ISteamGameServer_SetRegion
    ISteamGameServer_SetRegion = dll.SteamAPI_ISteamGameServer_SetRegion
    ISteamGameServer_SetRegion.argtypes = [ POINTER(ISteamGameServer), c_char_p ]
    ISteamGameServer_SetRegion.restype = None

    global ISteamGameServer_SetAdvertiseServerActive
    ISteamGameServer_SetAdvertiseServerActive = dll.SteamAPI_ISteamGameServer_SetAdvertiseServerActive
    ISteamGameServer_SetAdvertiseServerActive.argtypes = [ POINTER(ISteamGameServer), c_bool ]
    ISteamGameServer_SetAdvertiseServerActive.restype = None

    global ISteamGameServer_GetAuthSessionTicket
    ISteamGameServer_GetAuthSessionTicket = dll.SteamAPI_ISteamGameServer_GetAuthSessionTicket
    ISteamGameServer_GetAuthSessionTicket.argtypes = [ POINTER(ISteamGameServer), c_void_p, c_int, POINTER(c_uint) ]
    ISteamGameServer_GetAuthSessionTicket.restype = c_uint

    global ISteamGameServer_BeginAuthSession
    ISteamGameServer_BeginAuthSession = dll.SteamAPI_ISteamGameServer_BeginAuthSession
    ISteamGameServer_BeginAuthSession.argtypes = [ POINTER(ISteamGameServer), c_void_p, c_int, c_ulonglong ]
    ISteamGameServer_BeginAuthSession.restype = EBeginAuthSessionResult

    global ISteamGameServer_EndAuthSession
    ISteamGameServer_EndAuthSession = dll.SteamAPI_ISteamGameServer_EndAuthSession
    ISteamGameServer_EndAuthSession.argtypes = [ POINTER(ISteamGameServer), c_ulonglong ]
    ISteamGameServer_EndAuthSession.restype = None

    global ISteamGameServer_CancelAuthTicket
    ISteamGameServer_CancelAuthTicket = dll.SteamAPI_ISteamGameServer_CancelAuthTicket
    ISteamGameServer_CancelAuthTicket.argtypes = [ POINTER(ISteamGameServer), c_uint ]
    ISteamGameServer_CancelAuthTicket.restype = None

    global ISteamGameServer_UserHasLicenseForApp
    ISteamGameServer_UserHasLicenseForApp = dll.SteamAPI_ISteamGameServer_UserHasLicenseForApp
    ISteamGameServer_UserHasLicenseForApp.argtypes = [ POINTER(ISteamGameServer), c_ulonglong, c_uint ]
    ISteamGameServer_UserHasLicenseForApp.restype = EUserHasLicenseForAppResult

    global ISteamGameServer_RequestUserGroupStatus
    ISteamGameServer_RequestUserGroupStatus = dll.SteamAPI_ISteamGameServer_RequestUserGroupStatus
    ISteamGameServer_RequestUserGroupStatus.argtypes = [ POINTER(ISteamGameServer), c_ulonglong, c_ulonglong ]
    ISteamGameServer_RequestUserGroupStatus.restype = c_bool

    global ISteamGameServer_GetGameplayStats
    ISteamGameServer_GetGameplayStats = dll.SteamAPI_ISteamGameServer_GetGameplayStats
    ISteamGameServer_GetGameplayStats.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_GetGameplayStats.restype = None

    global ISteamGameServer_GetServerReputation
    ISteamGameServer_GetServerReputation = dll.SteamAPI_ISteamGameServer_GetServerReputation
    ISteamGameServer_GetServerReputation.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_GetServerReputation.restype = c_ulonglong

    global ISteamGameServer_GetPublicIP
    ISteamGameServer_GetPublicIP = dll.SteamAPI_ISteamGameServer_GetPublicIP
    ISteamGameServer_GetPublicIP.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_GetPublicIP.restype = SteamIPAddress_t

    global ISteamGameServer_HandleIncomingPacket
    ISteamGameServer_HandleIncomingPacket = dll.SteamAPI_ISteamGameServer_HandleIncomingPacket
    ISteamGameServer_HandleIncomingPacket.argtypes = [ POINTER(ISteamGameServer), c_void_p, c_int, c_uint, c_ushort ]
    ISteamGameServer_HandleIncomingPacket.restype = c_bool

    global ISteamGameServer_GetNextOutgoingPacket
    ISteamGameServer_GetNextOutgoingPacket = dll.SteamAPI_ISteamGameServer_GetNextOutgoingPacket
    ISteamGameServer_GetNextOutgoingPacket.argtypes = [ POINTER(ISteamGameServer), c_void_p, c_int, POINTER(c_uint), POINTER(c_ushort) ]
    ISteamGameServer_GetNextOutgoingPacket.restype = c_int

    global ISteamGameServer_AssociateWithClan
    ISteamGameServer_AssociateWithClan = dll.SteamAPI_ISteamGameServer_AssociateWithClan
    ISteamGameServer_AssociateWithClan.argtypes = [ POINTER(ISteamGameServer), c_ulonglong ]
    ISteamGameServer_AssociateWithClan.restype = c_ulonglong

    global ISteamGameServer_ComputeNewPlayerCompatibility
    ISteamGameServer_ComputeNewPlayerCompatibility = dll.SteamAPI_ISteamGameServer_ComputeNewPlayerCompatibility
    ISteamGameServer_ComputeNewPlayerCompatibility.argtypes = [ POINTER(ISteamGameServer), c_ulonglong ]
    ISteamGameServer_ComputeNewPlayerCompatibility.restype = c_ulonglong

    global ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED
    ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED = dll.SteamAPI_ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED
    ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED.argtypes = [ POINTER(ISteamGameServer), c_uint, c_void_p, c_uint, POINTER(c_ulonglong) ]
    ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED.restype = c_bool

    global ISteamGameServer_CreateUnauthenticatedUserConnection
    ISteamGameServer_CreateUnauthenticatedUserConnection = dll.SteamAPI_ISteamGameServer_CreateUnauthenticatedUserConnection
    ISteamGameServer_CreateUnauthenticatedUserConnection.argtypes = [ POINTER(ISteamGameServer),  ]
    ISteamGameServer_CreateUnauthenticatedUserConnection.restype = c_ulonglong

    global ISteamGameServer_SendUserDisconnect_DEPRECATED
    ISteamGameServer_SendUserDisconnect_DEPRECATED = dll.SteamAPI_ISteamGameServer_SendUserDisconnect_DEPRECATED
    ISteamGameServer_SendUserDisconnect_DEPRECATED.argtypes = [ POINTER(ISteamGameServer), c_ulonglong ]
    ISteamGameServer_SendUserDisconnect_DEPRECATED.restype = None

    global ISteamGameServer_BUpdateUserData
    ISteamGameServer_BUpdateUserData = dll.SteamAPI_ISteamGameServer_BUpdateUserData
    ISteamGameServer_BUpdateUserData.argtypes = [ POINTER(ISteamGameServer), c_ulonglong, c_char_p, c_uint ]
    ISteamGameServer_BUpdateUserData.restype = c_bool

    global SteamGameServer_v014
    SteamGameServer_v014 = dll.SteamAPI_SteamGameServer_v014
    SteamGameServer_v014.argtypes = [ ]
    SteamGameServer_v014.restype = POINTER(ISteamGameServer)

    global ISteamGameServerStats_RequestUserStats
    ISteamGameServerStats_RequestUserStats = dll.SteamAPI_ISteamGameServerStats_RequestUserStats
    ISteamGameServerStats_RequestUserStats.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong ]
    ISteamGameServerStats_RequestUserStats.restype = c_ulonglong

    global ISteamGameServerStats_GetUserStatInt32
    ISteamGameServerStats_GetUserStatInt32 = dll.SteamAPI_ISteamGameServerStats_GetUserStatInt32
    ISteamGameServerStats_GetUserStatInt32.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, POINTER(c_int) ]
    ISteamGameServerStats_GetUserStatInt32.restype = c_bool

    global ISteamGameServerStats_GetUserStatFloat
    ISteamGameServerStats_GetUserStatFloat = dll.SteamAPI_ISteamGameServerStats_GetUserStatFloat
    ISteamGameServerStats_GetUserStatFloat.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, POINTER(c_float) ]
    ISteamGameServerStats_GetUserStatFloat.restype = c_bool

    global ISteamGameServerStats_GetUserAchievement
    ISteamGameServerStats_GetUserAchievement = dll.SteamAPI_ISteamGameServerStats_GetUserAchievement
    ISteamGameServerStats_GetUserAchievement.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, POINTER(c_bool) ]
    ISteamGameServerStats_GetUserAchievement.restype = c_bool

    global ISteamGameServerStats_SetUserStatInt32
    ISteamGameServerStats_SetUserStatInt32 = dll.SteamAPI_ISteamGameServerStats_SetUserStatInt32
    ISteamGameServerStats_SetUserStatInt32.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, c_int ]
    ISteamGameServerStats_SetUserStatInt32.restype = c_bool

    global ISteamGameServerStats_SetUserStatFloat
    ISteamGameServerStats_SetUserStatFloat = dll.SteamAPI_ISteamGameServerStats_SetUserStatFloat
    ISteamGameServerStats_SetUserStatFloat.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, c_float ]
    ISteamGameServerStats_SetUserStatFloat.restype = c_bool

    global ISteamGameServerStats_UpdateUserAvgRateStat
    ISteamGameServerStats_UpdateUserAvgRateStat = dll.SteamAPI_ISteamGameServerStats_UpdateUserAvgRateStat
    ISteamGameServerStats_UpdateUserAvgRateStat.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p, c_float, c_double ]
    ISteamGameServerStats_UpdateUserAvgRateStat.restype = c_bool

    global ISteamGameServerStats_SetUserAchievement
    ISteamGameServerStats_SetUserAchievement = dll.SteamAPI_ISteamGameServerStats_SetUserAchievement
    ISteamGameServerStats_SetUserAchievement.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p ]
    ISteamGameServerStats_SetUserAchievement.restype = c_bool

    global ISteamGameServerStats_ClearUserAchievement
    ISteamGameServerStats_ClearUserAchievement = dll.SteamAPI_ISteamGameServerStats_ClearUserAchievement
    ISteamGameServerStats_ClearUserAchievement.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong, c_char_p ]
    ISteamGameServerStats_ClearUserAchievement.restype = c_bool

    global ISteamGameServerStats_StoreUserStats
    ISteamGameServerStats_StoreUserStats = dll.SteamAPI_ISteamGameServerStats_StoreUserStats
    ISteamGameServerStats_StoreUserStats.argtypes = [ POINTER(ISteamGameServerStats), c_ulonglong ]
    ISteamGameServerStats_StoreUserStats.restype = c_ulonglong

    global SteamGameServerStats_v001
    SteamGameServerStats_v001 = dll.SteamAPI_SteamGameServerStats_v001
    SteamGameServerStats_v001.argtypes = [ ]
    SteamGameServerStats_v001.restype = POINTER(ISteamGameServerStats)

    global ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort
    ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort = dll.SteamAPI_ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort
    ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort.argtypes = [ POINTER(ISteamNetworkingFakeUDPPort),  ]
    ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort.restype = None

    global ISteamNetworkingFakeUDPPort_SendMessageToFakeIP
    ISteamNetworkingFakeUDPPort_SendMessageToFakeIP = dll.SteamAPI_ISteamNetworkingFakeUDPPort_SendMessageToFakeIP
    ISteamNetworkingFakeUDPPort_SendMessageToFakeIP.argtypes = [ POINTER(ISteamNetworkingFakeUDPPort), POINTER(SteamNetworkingIPAddr), c_void_p, c_uint, c_int ]
    ISteamNetworkingFakeUDPPort_SendMessageToFakeIP.restype = EResult

    global ISteamNetworkingFakeUDPPort_ReceiveMessages
    ISteamNetworkingFakeUDPPort_ReceiveMessages = dll.SteamAPI_ISteamNetworkingFakeUDPPort_ReceiveMessages
    ISteamNetworkingFakeUDPPort_ReceiveMessages.argtypes = [ POINTER(ISteamNetworkingFakeUDPPort), POINTER(POINTER(SteamNetworkingMessage_t)), c_int ]
    ISteamNetworkingFakeUDPPort_ReceiveMessages.restype = c_int

    global ISteamNetworkingFakeUDPPort_ScheduleCleanup
    ISteamNetworkingFakeUDPPort_ScheduleCleanup = dll.SteamAPI_ISteamNetworkingFakeUDPPort_ScheduleCleanup
    ISteamNetworkingFakeUDPPort_ScheduleCleanup.argtypes = [ POINTER(ISteamNetworkingFakeUDPPort), POINTER(SteamNetworkingIPAddr) ]
    ISteamNetworkingFakeUDPPort_ScheduleCleanup.restype = None

    global Init
    Init = dll.SteamAPI_Init
    Init.argtypes = [  ]
    Init.restype = c_bool

    global Shutdown
    Shutdown = dll.SteamAPI_Shutdown
    Shutdown.argtypes = [  ]
    Shutdown.restype = None

    global RestartAppIfNecessary
    RestartAppIfNecessary = dll.SteamAPI_RestartAppIfNecessary
    RestartAppIfNecessary.argtypes = [ c_uint ]
    RestartAppIfNecessary.restype = c_bool

    global ReleaseCurrentThreadMemory
    ReleaseCurrentThreadMemory = dll.SteamAPI_ReleaseCurrentThreadMemory
    ReleaseCurrentThreadMemory.argtypes = [  ]
    ReleaseCurrentThreadMemory.restype = None

    global WriteMiniDump
    WriteMiniDump = dll.SteamAPI_WriteMiniDump
    WriteMiniDump.argtypes = [ c_uint, c_void_p, c_uint ]
    WriteMiniDump.restype = None

    global SetMiniDumpComment
    SetMiniDumpComment = dll.SteamAPI_SetMiniDumpComment
    SetMiniDumpComment.argtypes = [ c_char_p ]
    SetMiniDumpComment.restype = None

    global ManualDispatch_Init
    ManualDispatch_Init = dll.SteamAPI_ManualDispatch_Init
    ManualDispatch_Init.argtypes = [  ]
    ManualDispatch_Init.restype = None

    global ManualDispatch_RunFrame
    ManualDispatch_RunFrame = dll.SteamAPI_ManualDispatch_RunFrame
    ManualDispatch_RunFrame.argtypes = [ c_int ]
    ManualDispatch_RunFrame.restype = None

    global ManualDispatch_GetNextCallback
    ManualDispatch_GetNextCallback = dll.SteamAPI_ManualDispatch_GetNextCallback
    ManualDispatch_GetNextCallback.argtypes = [ c_int, POINTER(CallbackMsg_t) ]
    ManualDispatch_GetNextCallback.restype = c_bool

    global ManualDispatch_FreeLastCallback
    ManualDispatch_FreeLastCallback = dll.SteamAPI_ManualDispatch_FreeLastCallback
    ManualDispatch_FreeLastCallback.argtypes = [ c_int ]
    ManualDispatch_FreeLastCallback.restype = None

    global ManualDispatch_GetAPICallResult
    ManualDispatch_GetAPICallResult = dll.SteamAPI_ManualDispatch_GetAPICallResult
    ManualDispatch_GetAPICallResult.argtypes = [ c_int, c_ulonglong, c_void_p, c_int, c_int, c_bool ]
    ManualDispatch_GetAPICallResult.restype = c_bool

    global GetHSteamPipe
    GetHSteamPipe = dll.SteamAPI_GetHSteamPipe
    GetHSteamPipe.argtypes = [  ]
    GetHSteamPipe.restype = c_int

    global GetHSteamUser
    GetHSteamUser = dll.SteamAPI_GetHSteamUser
    GetHSteamUser.argtypes = [  ]
    GetHSteamUser.restype = c_uint

    global RunCallbacks
    RunCallbacks = dll.SteamAPI_RunCallbacks
    RunCallbacks.argtypes = [  ]
    RunCallbacks.restype = None

SteamIPAddress_t_IsSet = not_ready

MatchMakingKeyValuePair_t_Construct = not_ready

servernetadr_t_Construct = not_ready

servernetadr_t_Init = not_ready

servernetadr_t_GetQueryPort = not_ready

servernetadr_t_SetQueryPort = not_ready

servernetadr_t_GetConnectionPort = not_ready

servernetadr_t_SetConnectionPort = not_ready

servernetadr_t_GetIP = not_ready

servernetadr_t_SetIP = not_ready

servernetadr_t_GetConnectionAddressString = not_ready

servernetadr_t_GetQueryAddressString = not_ready

servernetadr_t_IsLessThan = not_ready

servernetadr_t_Assign = not_ready

gameserveritem_t_Construct = not_ready

gameserveritem_t_GetName = not_ready

gameserveritem_t_SetName = not_ready

SteamNetworkingIPAddr_Clear = not_ready

SteamNetworkingIPAddr_IsIPv6AllZeros = not_ready

SteamNetworkingIPAddr_SetIPv6 = not_ready

SteamNetworkingIPAddr_SetIPv4 = not_ready

SteamNetworkingIPAddr_IsIPv4 = not_ready

SteamNetworkingIPAddr_GetIPv4 = not_ready

SteamNetworkingIPAddr_SetIPv6LocalHost = not_ready

SteamNetworkingIPAddr_IsLocalHost = not_ready

SteamNetworkingIPAddr_ToString = not_ready

SteamNetworkingIPAddr_ParseString = not_ready

SteamNetworkingIPAddr_IsEqualTo = not_ready

SteamNetworkingIPAddr_GetFakeIPType = not_ready

SteamNetworkingIPAddr_IsFakeIP = not_ready

SteamNetworkingIdentity_Clear = not_ready

SteamNetworkingIdentity_IsInvalid = not_ready

SteamNetworkingIdentity_SetSteamID = not_ready

SteamNetworkingIdentity_GetSteamID = not_ready

SteamNetworkingIdentity_SetSteamID64 = not_ready

SteamNetworkingIdentity_GetSteamID64 = not_ready

SteamNetworkingIdentity_SetXboxPairwiseID = not_ready

SteamNetworkingIdentity_GetXboxPairwiseID = not_ready

SteamNetworkingIdentity_SetPSNID = not_ready

SteamNetworkingIdentity_GetPSNID = not_ready

SteamNetworkingIdentity_SetStadiaID = not_ready

SteamNetworkingIdentity_GetStadiaID = not_ready

SteamNetworkingIdentity_SetIPAddr = not_ready

SteamNetworkingIdentity_GetIPAddr = not_ready

SteamNetworkingIdentity_SetIPv4Addr = not_ready

SteamNetworkingIdentity_GetIPv4 = not_ready

SteamNetworkingIdentity_GetFakeIPType = not_ready

SteamNetworkingIdentity_IsFakeIP = not_ready

SteamNetworkingIdentity_SetLocalHost = not_ready

SteamNetworkingIdentity_IsLocalHost = not_ready

SteamNetworkingIdentity_SetGenericString = not_ready

SteamNetworkingIdentity_GetGenericString = not_ready

SteamNetworkingIdentity_SetGenericBytes = not_ready

SteamNetworkingIdentity_GetGenericBytes = not_ready

SteamNetworkingIdentity_IsEqualTo = not_ready

SteamNetworkingIdentity_ToString = not_ready

SteamNetworkingIdentity_ParseString = not_ready

SteamNetworkingMessage_t_Release = not_ready

SteamNetworkingConfigValue_t_SetInt32 = not_ready

SteamNetworkingConfigValue_t_SetInt64 = not_ready

SteamNetworkingConfigValue_t_SetFloat = not_ready

SteamNetworkingConfigValue_t_SetPtr = not_ready

SteamNetworkingConfigValue_t_SetString = not_ready

SteamDatagramHostedAddress_Clear = not_ready

SteamDatagramHostedAddress_GetPopID = not_ready

SteamDatagramHostedAddress_SetDevAddress = not_ready

ISteamClient_CreateSteamPipe = not_ready

ISteamClient_BReleaseSteamPipe = not_ready

ISteamClient_ConnectToGlobalUser = not_ready

ISteamClient_CreateLocalUser = not_ready

ISteamClient_ReleaseUser = not_ready

ISteamClient_GetISteamUser = not_ready

ISteamClient_GetISteamGameServer = not_ready

ISteamClient_SetLocalIPBinding = not_ready

ISteamClient_GetISteamFriends = not_ready

ISteamClient_GetISteamUtils = not_ready

ISteamClient_GetISteamMatchmaking = not_ready

ISteamClient_GetISteamMatchmakingServers = not_ready

ISteamClient_GetISteamGenericInterface = not_ready

ISteamClient_GetISteamUserStats = not_ready

ISteamClient_GetISteamGameServerStats = not_ready

ISteamClient_GetISteamApps = not_ready

ISteamClient_GetISteamNetworking = not_ready

ISteamClient_GetISteamRemoteStorage = not_ready

ISteamClient_GetISteamScreenshots = not_ready

ISteamClient_GetISteamGameSearch = not_ready

ISteamClient_GetIPCCallCount = not_ready

ISteamClient_SetWarningMessageHook = not_ready

ISteamClient_BShutdownIfAllPipesClosed = not_ready

ISteamClient_GetISteamHTTP = not_ready

ISteamClient_GetISteamController = not_ready

ISteamClient_GetISteamUGC = not_ready

ISteamClient_GetISteamAppList = not_ready

ISteamClient_GetISteamMusic = not_ready

ISteamClient_GetISteamMusicRemote = not_ready

ISteamClient_GetISteamHTMLSurface = not_ready

ISteamClient_GetISteamInventory = not_ready

ISteamClient_GetISteamVideo = not_ready

ISteamClient_GetISteamParentalSettings = not_ready

ISteamClient_GetISteamInput = not_ready

ISteamClient_GetISteamParties = not_ready

ISteamClient_GetISteamRemotePlay = not_ready

ISteamUser_GetHSteamUser = not_ready

ISteamUser_BLoggedOn = not_ready

ISteamUser_GetSteamID = not_ready

ISteamUser_InitiateGameConnection_DEPRECATED = not_ready

ISteamUser_TerminateGameConnection_DEPRECATED = not_ready

ISteamUser_TrackAppUsageEvent = not_ready

ISteamUser_GetUserDataFolder = not_ready

ISteamUser_StartVoiceRecording = not_ready

ISteamUser_StopVoiceRecording = not_ready

ISteamUser_GetAvailableVoice = not_ready

ISteamUser_GetVoice = not_ready

ISteamUser_DecompressVoice = not_ready

ISteamUser_GetVoiceOptimalSampleRate = not_ready

ISteamUser_GetAuthSessionTicket = not_ready

ISteamUser_BeginAuthSession = not_ready

ISteamUser_EndAuthSession = not_ready

ISteamUser_CancelAuthTicket = not_ready

ISteamUser_UserHasLicenseForApp = not_ready

ISteamUser_BIsBehindNAT = not_ready

ISteamUser_AdvertiseGame = not_ready

ISteamUser_RequestEncryptedAppTicket = not_ready

ISteamUser_GetEncryptedAppTicket = not_ready

ISteamUser_GetGameBadgeLevel = not_ready

ISteamUser_GetPlayerSteamLevel = not_ready

ISteamUser_RequestStoreAuthURL = not_ready

ISteamUser_BIsPhoneVerified = not_ready

ISteamUser_BIsTwoFactorEnabled = not_ready

ISteamUser_BIsPhoneIdentifying = not_ready

ISteamUser_BIsPhoneRequiringVerification = not_ready

ISteamUser_GetMarketEligibility = not_ready

ISteamUser_GetDurationControl = not_ready

ISteamUser_BSetDurationControlOnlineState = not_ready

SteamUser_v021 = not_ready

def SteamUser(): # type: () -> ISteamUser
    return SteamUser_v021().contents

ISteamFriends_GetPersonaName = not_ready

ISteamFriends_SetPersonaName = not_ready

ISteamFriends_GetPersonaState = not_ready

ISteamFriends_GetFriendCount = not_ready

ISteamFriends_GetFriendByIndex = not_ready

ISteamFriends_GetFriendRelationship = not_ready

ISteamFriends_GetFriendPersonaState = not_ready

ISteamFriends_GetFriendPersonaName = not_ready

ISteamFriends_GetFriendGamePlayed = not_ready

ISteamFriends_GetFriendPersonaNameHistory = not_ready

ISteamFriends_GetFriendSteamLevel = not_ready

ISteamFriends_GetPlayerNickname = not_ready

ISteamFriends_GetFriendsGroupCount = not_ready

ISteamFriends_GetFriendsGroupIDByIndex = not_ready

ISteamFriends_GetFriendsGroupName = not_ready

ISteamFriends_GetFriendsGroupMembersCount = not_ready

ISteamFriends_GetFriendsGroupMembersList = not_ready

ISteamFriends_HasFriend = not_ready

ISteamFriends_GetClanCount = not_ready

ISteamFriends_GetClanByIndex = not_ready

ISteamFriends_GetClanName = not_ready

ISteamFriends_GetClanTag = not_ready

ISteamFriends_GetClanActivityCounts = not_ready

ISteamFriends_DownloadClanActivityCounts = not_ready

ISteamFriends_GetFriendCountFromSource = not_ready

ISteamFriends_GetFriendFromSourceByIndex = not_ready

ISteamFriends_IsUserInSource = not_ready

ISteamFriends_SetInGameVoiceSpeaking = not_ready

ISteamFriends_ActivateGameOverlay = not_ready

ISteamFriends_ActivateGameOverlayToUser = not_ready

ISteamFriends_ActivateGameOverlayToWebPage = not_ready

ISteamFriends_ActivateGameOverlayToStore = not_ready

ISteamFriends_SetPlayedWith = not_ready

ISteamFriends_ActivateGameOverlayInviteDialog = not_ready

ISteamFriends_GetSmallFriendAvatar = not_ready

ISteamFriends_GetMediumFriendAvatar = not_ready

ISteamFriends_GetLargeFriendAvatar = not_ready

ISteamFriends_RequestUserInformation = not_ready

ISteamFriends_RequestClanOfficerList = not_ready

ISteamFriends_GetClanOwner = not_ready

ISteamFriends_GetClanOfficerCount = not_ready

ISteamFriends_GetClanOfficerByIndex = not_ready

ISteamFriends_GetUserRestrictions = not_ready

ISteamFriends_SetRichPresence = not_ready

ISteamFriends_ClearRichPresence = not_ready

ISteamFriends_GetFriendRichPresence = not_ready

ISteamFriends_GetFriendRichPresenceKeyCount = not_ready

ISteamFriends_GetFriendRichPresenceKeyByIndex = not_ready

ISteamFriends_RequestFriendRichPresence = not_ready

ISteamFriends_InviteUserToGame = not_ready

ISteamFriends_GetCoplayFriendCount = not_ready

ISteamFriends_GetCoplayFriend = not_ready

ISteamFriends_GetFriendCoplayTime = not_ready

ISteamFriends_GetFriendCoplayGame = not_ready

ISteamFriends_JoinClanChatRoom = not_ready

ISteamFriends_LeaveClanChatRoom = not_ready

ISteamFriends_GetClanChatMemberCount = not_ready

ISteamFriends_GetChatMemberByIndex = not_ready

ISteamFriends_SendClanChatMessage = not_ready

ISteamFriends_GetClanChatMessage = not_ready

ISteamFriends_IsClanChatAdmin = not_ready

ISteamFriends_IsClanChatWindowOpenInSteam = not_ready

ISteamFriends_OpenClanChatWindowInSteam = not_ready

ISteamFriends_CloseClanChatWindowInSteam = not_ready

ISteamFriends_SetListenForFriendsMessages = not_ready

ISteamFriends_ReplyToFriendMessage = not_ready

ISteamFriends_GetFriendMessage = not_ready

ISteamFriends_GetFollowerCount = not_ready

ISteamFriends_IsFollowing = not_ready

ISteamFriends_EnumerateFollowingList = not_ready

ISteamFriends_IsClanPublic = not_ready

ISteamFriends_IsClanOfficialGameGroup = not_ready

ISteamFriends_GetNumChatsWithUnreadPriorityMessages = not_ready

ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog = not_ready

ISteamFriends_RegisterProtocolInOverlayBrowser = not_ready

ISteamFriends_ActivateGameOverlayInviteDialogConnectString = not_ready

SteamFriends_v017 = not_ready

def SteamFriends(): # type: () -> ISteamFriends
    return SteamFriends_v017().contents

ISteamUtils_GetSecondsSinceAppActive = not_ready

ISteamUtils_GetSecondsSinceComputerActive = not_ready

ISteamUtils_GetConnectedUniverse = not_ready

ISteamUtils_GetServerRealTime = not_ready

ISteamUtils_GetIPCountry = not_ready

ISteamUtils_GetImageSize = not_ready

ISteamUtils_GetImageRGBA = not_ready

ISteamUtils_GetCurrentBatteryPower = not_ready

ISteamUtils_GetAppID = not_ready

ISteamUtils_SetOverlayNotificationPosition = not_ready

ISteamUtils_IsAPICallCompleted = not_ready

ISteamUtils_GetAPICallFailureReason = not_ready

ISteamUtils_GetAPICallResult = not_ready

ISteamUtils_GetIPCCallCount = not_ready

ISteamUtils_SetWarningMessageHook = not_ready

ISteamUtils_IsOverlayEnabled = not_ready

ISteamUtils_BOverlayNeedsPresent = not_ready

ISteamUtils_CheckFileSignature = not_ready

ISteamUtils_ShowGamepadTextInput = not_ready

ISteamUtils_GetEnteredGamepadTextLength = not_ready

ISteamUtils_GetEnteredGamepadTextInput = not_ready

ISteamUtils_GetSteamUILanguage = not_ready

ISteamUtils_IsSteamRunningInVR = not_ready

ISteamUtils_SetOverlayNotificationInset = not_ready

ISteamUtils_IsSteamInBigPictureMode = not_ready

ISteamUtils_StartVRDashboard = not_ready

ISteamUtils_IsVRHeadsetStreamingEnabled = not_ready

ISteamUtils_SetVRHeadsetStreamingEnabled = not_ready

ISteamUtils_IsSteamChinaLauncher = not_ready

ISteamUtils_InitFilterText = not_ready

ISteamUtils_FilterText = not_ready

ISteamUtils_GetIPv6ConnectivityState = not_ready

ISteamUtils_IsSteamRunningOnSteamDeck = not_ready

ISteamUtils_ShowFloatingGamepadTextInput = not_ready

ISteamUtils_SetGameLauncherMode = not_ready

ISteamUtils_DismissFloatingGamepadTextInput = not_ready

SteamUtils_v010 = not_ready

def SteamUtils(): # type: () -> ISteamUtils
    return SteamUtils_v010().contents

SteamGameServerUtils_v010 = not_ready

def SteamGameServerUtils(): # type: () -> ISteamUtils
    return SteamGameServerUtils_v010().contents

ISteamMatchmaking_GetFavoriteGameCount = not_ready

ISteamMatchmaking_GetFavoriteGame = not_ready

ISteamMatchmaking_AddFavoriteGame = not_ready

ISteamMatchmaking_RemoveFavoriteGame = not_ready

ISteamMatchmaking_RequestLobbyList = not_ready

ISteamMatchmaking_AddRequestLobbyListStringFilter = not_ready

ISteamMatchmaking_AddRequestLobbyListNumericalFilter = not_ready

ISteamMatchmaking_AddRequestLobbyListNearValueFilter = not_ready

ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable = not_ready

ISteamMatchmaking_AddRequestLobbyListDistanceFilter = not_ready

ISteamMatchmaking_AddRequestLobbyListResultCountFilter = not_ready

ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter = not_ready

ISteamMatchmaking_GetLobbyByIndex = not_ready

ISteamMatchmaking_CreateLobby = not_ready

ISteamMatchmaking_JoinLobby = not_ready

ISteamMatchmaking_LeaveLobby = not_ready

ISteamMatchmaking_InviteUserToLobby = not_ready

ISteamMatchmaking_GetNumLobbyMembers = not_ready

ISteamMatchmaking_GetLobbyMemberByIndex = not_ready

ISteamMatchmaking_GetLobbyData = not_ready

ISteamMatchmaking_SetLobbyData = not_ready

ISteamMatchmaking_GetLobbyDataCount = not_ready

ISteamMatchmaking_GetLobbyDataByIndex = not_ready

ISteamMatchmaking_DeleteLobbyData = not_ready

ISteamMatchmaking_GetLobbyMemberData = not_ready

ISteamMatchmaking_SetLobbyMemberData = not_ready

ISteamMatchmaking_SendLobbyChatMsg = not_ready

ISteamMatchmaking_GetLobbyChatEntry = not_ready

ISteamMatchmaking_RequestLobbyData = not_ready

ISteamMatchmaking_SetLobbyGameServer = not_ready

ISteamMatchmaking_GetLobbyGameServer = not_ready

ISteamMatchmaking_SetLobbyMemberLimit = not_ready

ISteamMatchmaking_GetLobbyMemberLimit = not_ready

ISteamMatchmaking_SetLobbyType = not_ready

ISteamMatchmaking_SetLobbyJoinable = not_ready

ISteamMatchmaking_GetLobbyOwner = not_ready

ISteamMatchmaking_SetLobbyOwner = not_ready

ISteamMatchmaking_SetLinkedLobby = not_ready

SteamMatchmaking_v009 = not_ready

def SteamMatchmaking(): # type: () -> ISteamMatchmaking
    return SteamMatchmaking_v009().contents

ISteamMatchmakingServerListResponse_ServerResponded = not_ready

ISteamMatchmakingServerListResponse_ServerFailedToRespond = not_ready

ISteamMatchmakingServerListResponse_RefreshComplete = not_ready

ISteamMatchmakingPingResponse_ServerResponded = not_ready

ISteamMatchmakingPingResponse_ServerFailedToRespond = not_ready

ISteamMatchmakingPlayersResponse_AddPlayerToList = not_ready

ISteamMatchmakingPlayersResponse_PlayersFailedToRespond = not_ready

ISteamMatchmakingPlayersResponse_PlayersRefreshComplete = not_ready

ISteamMatchmakingRulesResponse_RulesResponded = not_ready

ISteamMatchmakingRulesResponse_RulesFailedToRespond = not_ready

ISteamMatchmakingRulesResponse_RulesRefreshComplete = not_ready

ISteamMatchmakingServers_RequestInternetServerList = not_ready

ISteamMatchmakingServers_RequestLANServerList = not_ready

ISteamMatchmakingServers_RequestFriendsServerList = not_ready

ISteamMatchmakingServers_RequestFavoritesServerList = not_ready

ISteamMatchmakingServers_RequestHistoryServerList = not_ready

ISteamMatchmakingServers_RequestSpectatorServerList = not_ready

ISteamMatchmakingServers_ReleaseRequest = not_ready

ISteamMatchmakingServers_GetServerDetails = not_ready

ISteamMatchmakingServers_CancelQuery = not_ready

ISteamMatchmakingServers_RefreshQuery = not_ready

ISteamMatchmakingServers_IsRefreshing = not_ready

ISteamMatchmakingServers_GetServerCount = not_ready

ISteamMatchmakingServers_RefreshServer = not_ready

ISteamMatchmakingServers_PingServer = not_ready

ISteamMatchmakingServers_PlayerDetails = not_ready

ISteamMatchmakingServers_ServerRules = not_ready

ISteamMatchmakingServers_CancelServerQuery = not_ready

SteamMatchmakingServers_v002 = not_ready

def SteamMatchmakingServers(): # type: () -> ISteamMatchmakingServers
    return SteamMatchmakingServers_v002().contents

ISteamGameSearch_AddGameSearchParams = not_ready

ISteamGameSearch_SearchForGameWithLobby = not_ready

ISteamGameSearch_SearchForGameSolo = not_ready

ISteamGameSearch_AcceptGame = not_ready

ISteamGameSearch_DeclineGame = not_ready

ISteamGameSearch_RetrieveConnectionDetails = not_ready

ISteamGameSearch_EndGameSearch = not_ready

ISteamGameSearch_SetGameHostParams = not_ready

ISteamGameSearch_SetConnectionDetails = not_ready

ISteamGameSearch_RequestPlayersForGame = not_ready

ISteamGameSearch_HostConfirmGameStart = not_ready

ISteamGameSearch_CancelRequestPlayersForGame = not_ready

ISteamGameSearch_SubmitPlayerResult = not_ready

ISteamGameSearch_EndGame = not_ready

SteamGameSearch_v001 = not_ready

def SteamGameSearch(): # type: () -> ISteamGameSearch
    return SteamGameSearch_v001().contents

ISteamParties_GetNumActiveBeacons = not_ready

ISteamParties_GetBeaconByIndex = not_ready

ISteamParties_GetBeaconDetails = not_ready

ISteamParties_JoinParty = not_ready

ISteamParties_GetNumAvailableBeaconLocations = not_ready

ISteamParties_GetAvailableBeaconLocations = not_ready

ISteamParties_CreateBeacon = not_ready

ISteamParties_OnReservationCompleted = not_ready

ISteamParties_CancelReservation = not_ready

ISteamParties_ChangeNumOpenSlots = not_ready

ISteamParties_DestroyBeacon = not_ready

ISteamParties_GetBeaconLocationData = not_ready

SteamParties_v002 = not_ready

def SteamParties(): # type: () -> ISteamParties
    return SteamParties_v002().contents

ISteamRemoteStorage_FileWrite = not_ready

ISteamRemoteStorage_FileRead = not_ready

ISteamRemoteStorage_FileWriteAsync = not_ready

ISteamRemoteStorage_FileReadAsync = not_ready

ISteamRemoteStorage_FileReadAsyncComplete = not_ready

ISteamRemoteStorage_FileForget = not_ready

ISteamRemoteStorage_FileDelete = not_ready

ISteamRemoteStorage_FileShare = not_ready

ISteamRemoteStorage_SetSyncPlatforms = not_ready

ISteamRemoteStorage_FileWriteStreamOpen = not_ready

ISteamRemoteStorage_FileWriteStreamWriteChunk = not_ready

ISteamRemoteStorage_FileWriteStreamClose = not_ready

ISteamRemoteStorage_FileWriteStreamCancel = not_ready

ISteamRemoteStorage_FileExists = not_ready

ISteamRemoteStorage_FilePersisted = not_ready

ISteamRemoteStorage_GetFileSize = not_ready

ISteamRemoteStorage_GetFileTimestamp = not_ready

ISteamRemoteStorage_GetSyncPlatforms = not_ready

ISteamRemoteStorage_GetFileCount = not_ready

ISteamRemoteStorage_GetFileNameAndSize = not_ready

ISteamRemoteStorage_GetQuota = not_ready

ISteamRemoteStorage_IsCloudEnabledForAccount = not_ready

ISteamRemoteStorage_IsCloudEnabledForApp = not_ready

ISteamRemoteStorage_SetCloudEnabledForApp = not_ready

ISteamRemoteStorage_UGCDownload = not_ready

ISteamRemoteStorage_GetUGCDownloadProgress = not_ready

ISteamRemoteStorage_GetUGCDetails = not_ready

ISteamRemoteStorage_UGCRead = not_ready

ISteamRemoteStorage_GetCachedUGCCount = not_ready

ISteamRemoteStorage_GetCachedUGCHandle = not_ready

ISteamRemoteStorage_PublishWorkshopFile = not_ready

ISteamRemoteStorage_CreatePublishedFileUpdateRequest = not_ready

ISteamRemoteStorage_UpdatePublishedFileFile = not_ready

ISteamRemoteStorage_UpdatePublishedFilePreviewFile = not_ready

ISteamRemoteStorage_UpdatePublishedFileTitle = not_ready

ISteamRemoteStorage_UpdatePublishedFileDescription = not_ready

ISteamRemoteStorage_UpdatePublishedFileVisibility = not_ready

ISteamRemoteStorage_UpdatePublishedFileTags = not_ready

ISteamRemoteStorage_CommitPublishedFileUpdate = not_ready

ISteamRemoteStorage_GetPublishedFileDetails = not_ready

ISteamRemoteStorage_DeletePublishedFile = not_ready

ISteamRemoteStorage_EnumerateUserPublishedFiles = not_ready

ISteamRemoteStorage_SubscribePublishedFile = not_ready

ISteamRemoteStorage_EnumerateUserSubscribedFiles = not_ready

ISteamRemoteStorage_UnsubscribePublishedFile = not_ready

ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription = not_ready

ISteamRemoteStorage_GetPublishedItemVoteDetails = not_ready

ISteamRemoteStorage_UpdateUserPublishedItemVote = not_ready

ISteamRemoteStorage_GetUserPublishedItemVoteDetails = not_ready

ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles = not_ready

ISteamRemoteStorage_PublishVideo = not_ready

ISteamRemoteStorage_SetUserPublishedFileAction = not_ready

ISteamRemoteStorage_EnumeratePublishedFilesByUserAction = not_ready

ISteamRemoteStorage_EnumeratePublishedWorkshopFiles = not_ready

ISteamRemoteStorage_UGCDownloadToLocation = not_ready

ISteamRemoteStorage_GetLocalFileChangeCount = not_ready

ISteamRemoteStorage_GetLocalFileChange = not_ready

ISteamRemoteStorage_BeginFileWriteBatch = not_ready

ISteamRemoteStorage_EndFileWriteBatch = not_ready

SteamRemoteStorage_v016 = not_ready

def SteamRemoteStorage(): # type: () -> ISteamRemoteStorage
    return SteamRemoteStorage_v016().contents

ISteamUserStats_RequestCurrentStats = not_ready

ISteamUserStats_GetStatInt32 = not_ready

ISteamUserStats_GetStatFloat = not_ready

ISteamUserStats_SetStatInt32 = not_ready

ISteamUserStats_SetStatFloat = not_ready

ISteamUserStats_UpdateAvgRateStat = not_ready

ISteamUserStats_GetAchievement = not_ready

ISteamUserStats_SetAchievement = not_ready

ISteamUserStats_ClearAchievement = not_ready

ISteamUserStats_GetAchievementAndUnlockTime = not_ready

ISteamUserStats_StoreStats = not_ready

ISteamUserStats_GetAchievementIcon = not_ready

ISteamUserStats_GetAchievementDisplayAttribute = not_ready

ISteamUserStats_IndicateAchievementProgress = not_ready

ISteamUserStats_GetNumAchievements = not_ready

ISteamUserStats_GetAchievementName = not_ready

ISteamUserStats_RequestUserStats = not_ready

ISteamUserStats_GetUserStatInt32 = not_ready

ISteamUserStats_GetUserStatFloat = not_ready

ISteamUserStats_GetUserAchievement = not_ready

ISteamUserStats_GetUserAchievementAndUnlockTime = not_ready

ISteamUserStats_ResetAllStats = not_ready

ISteamUserStats_FindOrCreateLeaderboard = not_ready

ISteamUserStats_FindLeaderboard = not_ready

ISteamUserStats_GetLeaderboardName = not_ready

ISteamUserStats_GetLeaderboardEntryCount = not_ready

ISteamUserStats_GetLeaderboardSortMethod = not_ready

ISteamUserStats_GetLeaderboardDisplayType = not_ready

ISteamUserStats_DownloadLeaderboardEntries = not_ready

ISteamUserStats_DownloadLeaderboardEntriesForUsers = not_ready

ISteamUserStats_GetDownloadedLeaderboardEntry = not_ready

ISteamUserStats_UploadLeaderboardScore = not_ready

ISteamUserStats_AttachLeaderboardUGC = not_ready

ISteamUserStats_GetNumberOfCurrentPlayers = not_ready

ISteamUserStats_RequestGlobalAchievementPercentages = not_ready

ISteamUserStats_GetMostAchievedAchievementInfo = not_ready

ISteamUserStats_GetNextMostAchievedAchievementInfo = not_ready

ISteamUserStats_GetAchievementAchievedPercent = not_ready

ISteamUserStats_RequestGlobalStats = not_ready

ISteamUserStats_GetGlobalStatInt64 = not_ready

ISteamUserStats_GetGlobalStatDouble = not_ready

ISteamUserStats_GetGlobalStatHistoryInt64 = not_ready

ISteamUserStats_GetGlobalStatHistoryDouble = not_ready

ISteamUserStats_GetAchievementProgressLimitsInt32 = not_ready

ISteamUserStats_GetAchievementProgressLimitsFloat = not_ready

SteamUserStats_v012 = not_ready

def SteamUserStats(): # type: () -> ISteamUserStats
    return SteamUserStats_v012().contents

ISteamApps_BIsSubscribed = not_ready

ISteamApps_BIsLowViolence = not_ready

ISteamApps_BIsCybercafe = not_ready

ISteamApps_BIsVACBanned = not_ready

ISteamApps_GetCurrentGameLanguage = not_ready

ISteamApps_GetAvailableGameLanguages = not_ready

ISteamApps_BIsSubscribedApp = not_ready

ISteamApps_BIsDlcInstalled = not_ready

ISteamApps_GetEarliestPurchaseUnixTime = not_ready

ISteamApps_BIsSubscribedFromFreeWeekend = not_ready

ISteamApps_GetDLCCount = not_ready

ISteamApps_BGetDLCDataByIndex = not_ready

ISteamApps_InstallDLC = not_ready

ISteamApps_UninstallDLC = not_ready

ISteamApps_RequestAppProofOfPurchaseKey = not_ready

ISteamApps_GetCurrentBetaName = not_ready

ISteamApps_MarkContentCorrupt = not_ready

ISteamApps_GetInstalledDepots = not_ready

ISteamApps_GetAppInstallDir = not_ready

ISteamApps_BIsAppInstalled = not_ready

ISteamApps_GetAppOwner = not_ready

ISteamApps_GetLaunchQueryParam = not_ready

ISteamApps_GetDlcDownloadProgress = not_ready

ISteamApps_GetAppBuildId = not_ready

ISteamApps_RequestAllProofOfPurchaseKeys = not_ready

ISteamApps_GetFileDetails = not_ready

ISteamApps_GetLaunchCommandLine = not_ready

ISteamApps_BIsSubscribedFromFamilySharing = not_ready

ISteamApps_BIsTimedTrial = not_ready

SteamApps_v008 = not_ready

def SteamApps(): # type: () -> ISteamApps
    return SteamApps_v008().contents

ISteamNetworking_SendP2PPacket = not_ready

ISteamNetworking_IsP2PPacketAvailable = not_ready

ISteamNetworking_ReadP2PPacket = not_ready

ISteamNetworking_AcceptP2PSessionWithUser = not_ready

ISteamNetworking_CloseP2PSessionWithUser = not_ready

ISteamNetworking_CloseP2PChannelWithUser = not_ready

ISteamNetworking_GetP2PSessionState = not_ready

ISteamNetworking_AllowP2PPacketRelay = not_ready

ISteamNetworking_CreateListenSocket = not_ready

ISteamNetworking_CreateP2PConnectionSocket = not_ready

ISteamNetworking_CreateConnectionSocket = not_ready

ISteamNetworking_DestroySocket = not_ready

ISteamNetworking_DestroyListenSocket = not_ready

ISteamNetworking_SendDataOnSocket = not_ready

ISteamNetworking_IsDataAvailableOnSocket = not_ready

ISteamNetworking_RetrieveDataFromSocket = not_ready

ISteamNetworking_IsDataAvailable = not_ready

ISteamNetworking_RetrieveData = not_ready

ISteamNetworking_GetSocketInfo = not_ready

ISteamNetworking_GetListenSocketInfo = not_ready

ISteamNetworking_GetSocketConnectionType = not_ready

ISteamNetworking_GetMaxPacketSize = not_ready

SteamNetworking_v006 = not_ready

def SteamNetworking(): # type: () -> ISteamNetworking
    return SteamNetworking_v006().contents

SteamGameServerNetworking_v006 = not_ready

def SteamGameServerNetworking(): # type: () -> ISteamNetworking
    return SteamGameServerNetworking_v006().contents

ISteamScreenshots_WriteScreenshot = not_ready

ISteamScreenshots_AddScreenshotToLibrary = not_ready

ISteamScreenshots_TriggerScreenshot = not_ready

ISteamScreenshots_HookScreenshots = not_ready

ISteamScreenshots_SetLocation = not_ready

ISteamScreenshots_TagUser = not_ready

ISteamScreenshots_TagPublishedFile = not_ready

ISteamScreenshots_IsScreenshotsHooked = not_ready

ISteamScreenshots_AddVRScreenshotToLibrary = not_ready

SteamScreenshots_v003 = not_ready

def SteamScreenshots(): # type: () -> ISteamScreenshots
    return SteamScreenshots_v003().contents

ISteamMusic_BIsEnabled = not_ready

ISteamMusic_BIsPlaying = not_ready

ISteamMusic_GetPlaybackStatus = not_ready

ISteamMusic_Play = not_ready

ISteamMusic_Pause = not_ready

ISteamMusic_PlayPrevious = not_ready

ISteamMusic_PlayNext = not_ready

ISteamMusic_SetVolume = not_ready

ISteamMusic_GetVolume = not_ready

SteamMusic_v001 = not_ready

def SteamMusic(): # type: () -> ISteamMusic
    return SteamMusic_v001().contents

ISteamMusicRemote_RegisterSteamMusicRemote = not_ready

ISteamMusicRemote_DeregisterSteamMusicRemote = not_ready

ISteamMusicRemote_BIsCurrentMusicRemote = not_ready

ISteamMusicRemote_BActivationSuccess = not_ready

ISteamMusicRemote_SetDisplayName = not_ready

ISteamMusicRemote_SetPNGIcon_64x64 = not_ready

ISteamMusicRemote_EnablePlayPrevious = not_ready

ISteamMusicRemote_EnablePlayNext = not_ready

ISteamMusicRemote_EnableShuffled = not_ready

ISteamMusicRemote_EnableLooped = not_ready

ISteamMusicRemote_EnableQueue = not_ready

ISteamMusicRemote_EnablePlaylists = not_ready

ISteamMusicRemote_UpdatePlaybackStatus = not_ready

ISteamMusicRemote_UpdateShuffled = not_ready

ISteamMusicRemote_UpdateLooped = not_ready

ISteamMusicRemote_UpdateVolume = not_ready

ISteamMusicRemote_CurrentEntryWillChange = not_ready

ISteamMusicRemote_CurrentEntryIsAvailable = not_ready

ISteamMusicRemote_UpdateCurrentEntryText = not_ready

ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds = not_ready

ISteamMusicRemote_UpdateCurrentEntryCoverArt = not_ready

ISteamMusicRemote_CurrentEntryDidChange = not_ready

ISteamMusicRemote_QueueWillChange = not_ready

ISteamMusicRemote_ResetQueueEntries = not_ready

ISteamMusicRemote_SetQueueEntry = not_ready

ISteamMusicRemote_SetCurrentQueueEntry = not_ready

ISteamMusicRemote_QueueDidChange = not_ready

ISteamMusicRemote_PlaylistWillChange = not_ready

ISteamMusicRemote_ResetPlaylistEntries = not_ready

ISteamMusicRemote_SetPlaylistEntry = not_ready

ISteamMusicRemote_SetCurrentPlaylistEntry = not_ready

ISteamMusicRemote_PlaylistDidChange = not_ready

SteamMusicRemote_v001 = not_ready

def SteamMusicRemote(): # type: () -> ISteamMusicRemote
    return SteamMusicRemote_v001().contents

ISteamHTTP_CreateHTTPRequest = not_ready

ISteamHTTP_SetHTTPRequestContextValue = not_ready

ISteamHTTP_SetHTTPRequestNetworkActivityTimeout = not_ready

ISteamHTTP_SetHTTPRequestHeaderValue = not_ready

ISteamHTTP_SetHTTPRequestGetOrPostParameter = not_ready

ISteamHTTP_SendHTTPRequest = not_ready

ISteamHTTP_SendHTTPRequestAndStreamResponse = not_ready

ISteamHTTP_DeferHTTPRequest = not_ready

ISteamHTTP_PrioritizeHTTPRequest = not_ready

ISteamHTTP_GetHTTPResponseHeaderSize = not_ready

ISteamHTTP_GetHTTPResponseHeaderValue = not_ready

ISteamHTTP_GetHTTPResponseBodySize = not_ready

ISteamHTTP_GetHTTPResponseBodyData = not_ready

ISteamHTTP_GetHTTPStreamingResponseBodyData = not_ready

ISteamHTTP_ReleaseHTTPRequest = not_ready

ISteamHTTP_GetHTTPDownloadProgressPct = not_ready

ISteamHTTP_SetHTTPRequestRawPostBody = not_ready

ISteamHTTP_CreateCookieContainer = not_ready

ISteamHTTP_ReleaseCookieContainer = not_ready

ISteamHTTP_SetCookie = not_ready

ISteamHTTP_SetHTTPRequestCookieContainer = not_ready

ISteamHTTP_SetHTTPRequestUserAgentInfo = not_ready

ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate = not_ready

ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS = not_ready

ISteamHTTP_GetHTTPRequestWasTimedOut = not_ready

SteamHTTP_v003 = not_ready

def SteamHTTP(): # type: () -> ISteamHTTP
    return SteamHTTP_v003().contents

SteamGameServerHTTP_v003 = not_ready

def SteamGameServerHTTP(): # type: () -> ISteamHTTP
    return SteamGameServerHTTP_v003().contents

ISteamInput_Init = not_ready

ISteamInput_Shutdown = not_ready

ISteamInput_SetInputActionManifestFilePath = not_ready

ISteamInput_RunFrame = not_ready

ISteamInput_BWaitForData = not_ready

ISteamInput_BNewDataAvailable = not_ready

ISteamInput_GetConnectedControllers = not_ready

ISteamInput_EnableDeviceCallbacks = not_ready

ISteamInput_EnableActionEventCallbacks = not_ready

ISteamInput_GetActionSetHandle = not_ready

ISteamInput_ActivateActionSet = not_ready

ISteamInput_GetCurrentActionSet = not_ready

ISteamInput_ActivateActionSetLayer = not_ready

ISteamInput_DeactivateActionSetLayer = not_ready

ISteamInput_DeactivateAllActionSetLayers = not_ready

ISteamInput_GetActiveActionSetLayers = not_ready

ISteamInput_GetDigitalActionHandle = not_ready

ISteamInput_GetDigitalActionData = not_ready

ISteamInput_GetDigitalActionOrigins = not_ready

ISteamInput_GetStringForDigitalActionName = not_ready

ISteamInput_GetAnalogActionHandle = not_ready

ISteamInput_GetAnalogActionData = not_ready

ISteamInput_GetAnalogActionOrigins = not_ready

ISteamInput_GetGlyphPNGForActionOrigin = not_ready

ISteamInput_GetGlyphSVGForActionOrigin = not_ready

ISteamInput_GetGlyphForActionOrigin_Legacy = not_ready

ISteamInput_GetStringForActionOrigin = not_ready

ISteamInput_GetStringForAnalogActionName = not_ready

ISteamInput_StopAnalogActionMomentum = not_ready

ISteamInput_GetMotionData = not_ready

ISteamInput_TriggerVibration = not_ready

ISteamInput_TriggerVibrationExtended = not_ready

ISteamInput_TriggerSimpleHapticEvent = not_ready

ISteamInput_SetLEDColor = not_ready

ISteamInput_Legacy_TriggerHapticPulse = not_ready

ISteamInput_Legacy_TriggerRepeatedHapticPulse = not_ready

ISteamInput_ShowBindingPanel = not_ready

ISteamInput_GetInputTypeForHandle = not_ready

ISteamInput_GetControllerForGamepadIndex = not_ready

ISteamInput_GetGamepadIndexForController = not_ready

ISteamInput_GetStringForXboxOrigin = not_ready

ISteamInput_GetGlyphForXboxOrigin = not_ready

ISteamInput_GetActionOriginFromXboxOrigin = not_ready

ISteamInput_TranslateActionOrigin = not_ready

ISteamInput_GetDeviceBindingRevision = not_ready

ISteamInput_GetRemotePlaySessionID = not_ready

ISteamInput_GetSessionInputConfigurationSettings = not_ready

SteamInput_v006 = not_ready

def SteamInput(): # type: () -> ISteamInput
    return SteamInput_v006().contents

ISteamController_Init = not_ready

ISteamController_Shutdown = not_ready

ISteamController_RunFrame = not_ready

ISteamController_GetConnectedControllers = not_ready

ISteamController_GetActionSetHandle = not_ready

ISteamController_ActivateActionSet = not_ready

ISteamController_GetCurrentActionSet = not_ready

ISteamController_ActivateActionSetLayer = not_ready

ISteamController_DeactivateActionSetLayer = not_ready

ISteamController_DeactivateAllActionSetLayers = not_ready

ISteamController_GetActiveActionSetLayers = not_ready

ISteamController_GetDigitalActionHandle = not_ready

ISteamController_GetDigitalActionData = not_ready

ISteamController_GetDigitalActionOrigins = not_ready

ISteamController_GetAnalogActionHandle = not_ready

ISteamController_GetAnalogActionData = not_ready

ISteamController_GetAnalogActionOrigins = not_ready

ISteamController_GetGlyphForActionOrigin = not_ready

ISteamController_GetStringForActionOrigin = not_ready

ISteamController_StopAnalogActionMomentum = not_ready

ISteamController_GetMotionData = not_ready

ISteamController_TriggerHapticPulse = not_ready

ISteamController_TriggerRepeatedHapticPulse = not_ready

ISteamController_TriggerVibration = not_ready

ISteamController_SetLEDColor = not_ready

ISteamController_ShowBindingPanel = not_ready

ISteamController_GetInputTypeForHandle = not_ready

ISteamController_GetControllerForGamepadIndex = not_ready

ISteamController_GetGamepadIndexForController = not_ready

ISteamController_GetStringForXboxOrigin = not_ready

ISteamController_GetGlyphForXboxOrigin = not_ready

ISteamController_GetActionOriginFromXboxOrigin = not_ready

ISteamController_TranslateActionOrigin = not_ready

ISteamController_GetControllerBindingRevision = not_ready

SteamController_v008 = not_ready

def SteamController(): # type: () -> ISteamController
    return SteamController_v008().contents

ISteamUGC_CreateQueryUserUGCRequest = not_ready

ISteamUGC_CreateQueryAllUGCRequestPage = not_ready

ISteamUGC_CreateQueryAllUGCRequestCursor = not_ready

ISteamUGC_CreateQueryUGCDetailsRequest = not_ready

ISteamUGC_SendQueryUGCRequest = not_ready

ISteamUGC_GetQueryUGCResult = not_ready

ISteamUGC_GetQueryUGCNumTags = not_ready

ISteamUGC_GetQueryUGCTag = not_ready

ISteamUGC_GetQueryUGCTagDisplayName = not_ready

ISteamUGC_GetQueryUGCPreviewURL = not_ready

ISteamUGC_GetQueryUGCMetadata = not_ready

ISteamUGC_GetQueryUGCChildren = not_ready

ISteamUGC_GetQueryUGCStatistic = not_ready

ISteamUGC_GetQueryUGCNumAdditionalPreviews = not_ready

ISteamUGC_GetQueryUGCAdditionalPreview = not_ready

ISteamUGC_GetQueryUGCNumKeyValueTags = not_ready

ISteamUGC_GetQueryUGCKeyValueTag = not_ready

ISteamUGC_GetQueryFirstUGCKeyValueTag = not_ready

ISteamUGC_ReleaseQueryUGCRequest = not_ready

ISteamUGC_AddRequiredTag = not_ready

ISteamUGC_AddRequiredTagGroup = not_ready

ISteamUGC_AddExcludedTag = not_ready

ISteamUGC_SetReturnOnlyIDs = not_ready

ISteamUGC_SetReturnKeyValueTags = not_ready

ISteamUGC_SetReturnLongDescription = not_ready

ISteamUGC_SetReturnMetadata = not_ready

ISteamUGC_SetReturnChildren = not_ready

ISteamUGC_SetReturnAdditionalPreviews = not_ready

ISteamUGC_SetReturnTotalOnly = not_ready

ISteamUGC_SetReturnPlaytimeStats = not_ready

ISteamUGC_SetLanguage = not_ready

ISteamUGC_SetAllowCachedResponse = not_ready

ISteamUGC_SetCloudFileNameFilter = not_ready

ISteamUGC_SetMatchAnyTag = not_ready

ISteamUGC_SetSearchText = not_ready

ISteamUGC_SetRankedByTrendDays = not_ready

ISteamUGC_SetTimeCreatedDateRange = not_ready

ISteamUGC_SetTimeUpdatedDateRange = not_ready

ISteamUGC_AddRequiredKeyValueTag = not_ready

ISteamUGC_RequestUGCDetails = not_ready

ISteamUGC_CreateItem = not_ready

ISteamUGC_StartItemUpdate = not_ready

ISteamUGC_SetItemTitle = not_ready

ISteamUGC_SetItemDescription = not_ready

ISteamUGC_SetItemUpdateLanguage = not_ready

ISteamUGC_SetItemMetadata = not_ready

ISteamUGC_SetItemVisibility = not_ready

ISteamUGC_SetItemTags = not_ready

ISteamUGC_SetItemContent = not_ready

ISteamUGC_SetItemPreview = not_ready

ISteamUGC_SetAllowLegacyUpload = not_ready

ISteamUGC_RemoveAllItemKeyValueTags = not_ready

ISteamUGC_RemoveItemKeyValueTags = not_ready

ISteamUGC_AddItemKeyValueTag = not_ready

ISteamUGC_AddItemPreviewFile = not_ready

ISteamUGC_AddItemPreviewVideo = not_ready

ISteamUGC_UpdateItemPreviewFile = not_ready

ISteamUGC_UpdateItemPreviewVideo = not_ready

ISteamUGC_RemoveItemPreview = not_ready

ISteamUGC_SubmitItemUpdate = not_ready

ISteamUGC_GetItemUpdateProgress = not_ready

ISteamUGC_SetUserItemVote = not_ready

ISteamUGC_GetUserItemVote = not_ready

ISteamUGC_AddItemToFavorites = not_ready

ISteamUGC_RemoveItemFromFavorites = not_ready

ISteamUGC_SubscribeItem = not_ready

ISteamUGC_UnsubscribeItem = not_ready

ISteamUGC_GetNumSubscribedItems = not_ready

ISteamUGC_GetSubscribedItems = not_ready

ISteamUGC_GetItemState = not_ready

ISteamUGC_GetItemInstallInfo = not_ready

ISteamUGC_GetItemDownloadInfo = not_ready

ISteamUGC_DownloadItem = not_ready

ISteamUGC_BInitWorkshopForGameServer = not_ready

ISteamUGC_SuspendDownloads = not_ready

ISteamUGC_StartPlaytimeTracking = not_ready

ISteamUGC_StopPlaytimeTracking = not_ready

ISteamUGC_StopPlaytimeTrackingForAllItems = not_ready

ISteamUGC_AddDependency = not_ready

ISteamUGC_RemoveDependency = not_ready

ISteamUGC_AddAppDependency = not_ready

ISteamUGC_RemoveAppDependency = not_ready

ISteamUGC_GetAppDependencies = not_ready

ISteamUGC_DeleteItem = not_ready

ISteamUGC_ShowWorkshopEULA = not_ready

ISteamUGC_GetWorkshopEULAStatus = not_ready

SteamUGC_v016 = not_ready

def SteamUGC(): # type: () -> ISteamUGC
    return SteamUGC_v016().contents

SteamGameServerUGC_v016 = not_ready

def SteamGameServerUGC(): # type: () -> ISteamUGC
    return SteamGameServerUGC_v016().contents

ISteamAppList_GetNumInstalledApps = not_ready

ISteamAppList_GetInstalledApps = not_ready

ISteamAppList_GetAppName = not_ready

ISteamAppList_GetAppInstallDir = not_ready

ISteamAppList_GetAppBuildId = not_ready

SteamAppList_v001 = not_ready

def SteamAppList(): # type: () -> ISteamAppList
    return SteamAppList_v001().contents

ISteamHTMLSurface_Init = not_ready

ISteamHTMLSurface_Shutdown = not_ready

ISteamHTMLSurface_CreateBrowser = not_ready

ISteamHTMLSurface_RemoveBrowser = not_ready

ISteamHTMLSurface_LoadURL = not_ready

ISteamHTMLSurface_SetSize = not_ready

ISteamHTMLSurface_StopLoad = not_ready

ISteamHTMLSurface_Reload = not_ready

ISteamHTMLSurface_GoBack = not_ready

ISteamHTMLSurface_GoForward = not_ready

ISteamHTMLSurface_AddHeader = not_ready

ISteamHTMLSurface_ExecuteJavascript = not_ready

ISteamHTMLSurface_MouseUp = not_ready

ISteamHTMLSurface_MouseDown = not_ready

ISteamHTMLSurface_MouseDoubleClick = not_ready

ISteamHTMLSurface_MouseMove = not_ready

ISteamHTMLSurface_MouseWheel = not_ready

ISteamHTMLSurface_KeyDown = not_ready

ISteamHTMLSurface_KeyUp = not_ready

ISteamHTMLSurface_KeyChar = not_ready

ISteamHTMLSurface_SetHorizontalScroll = not_ready

ISteamHTMLSurface_SetVerticalScroll = not_ready

ISteamHTMLSurface_SetKeyFocus = not_ready

ISteamHTMLSurface_ViewSource = not_ready

ISteamHTMLSurface_CopyToClipboard = not_ready

ISteamHTMLSurface_PasteFromClipboard = not_ready

ISteamHTMLSurface_Find = not_ready

ISteamHTMLSurface_StopFind = not_ready

ISteamHTMLSurface_GetLinkAtPosition = not_ready

ISteamHTMLSurface_SetCookie = not_ready

ISteamHTMLSurface_SetPageScaleFactor = not_ready

ISteamHTMLSurface_SetBackgroundMode = not_ready

ISteamHTMLSurface_SetDPIScalingFactor = not_ready

ISteamHTMLSurface_OpenDeveloperTools = not_ready

ISteamHTMLSurface_AllowStartRequest = not_ready

ISteamHTMLSurface_JSDialogResponse = not_ready

ISteamHTMLSurface_FileLoadDialogResponse = not_ready

SteamHTMLSurface_v005 = not_ready

def SteamHTMLSurface(): # type: () -> ISteamHTMLSurface
    return SteamHTMLSurface_v005().contents

ISteamInventory_GetResultStatus = not_ready

ISteamInventory_GetResultItems = not_ready

ISteamInventory_GetResultItemProperty = not_ready

ISteamInventory_GetResultTimestamp = not_ready

ISteamInventory_CheckResultSteamID = not_ready

ISteamInventory_DestroyResult = not_ready

ISteamInventory_GetAllItems = not_ready

ISteamInventory_GetItemsByID = not_ready

ISteamInventory_SerializeResult = not_ready

ISteamInventory_DeserializeResult = not_ready

ISteamInventory_GenerateItems = not_ready

ISteamInventory_GrantPromoItems = not_ready

ISteamInventory_AddPromoItem = not_ready

ISteamInventory_AddPromoItems = not_ready

ISteamInventory_ConsumeItem = not_ready

ISteamInventory_ExchangeItems = not_ready

ISteamInventory_TransferItemQuantity = not_ready

ISteamInventory_SendItemDropHeartbeat = not_ready

ISteamInventory_TriggerItemDrop = not_ready

ISteamInventory_TradeItems = not_ready

ISteamInventory_LoadItemDefinitions = not_ready

ISteamInventory_GetItemDefinitionIDs = not_ready

ISteamInventory_GetItemDefinitionProperty = not_ready

ISteamInventory_RequestEligiblePromoItemDefinitionsIDs = not_ready

ISteamInventory_GetEligiblePromoItemDefinitionIDs = not_ready

ISteamInventory_StartPurchase = not_ready

ISteamInventory_RequestPrices = not_ready

ISteamInventory_GetNumItemsWithPrices = not_ready

ISteamInventory_GetItemsWithPrices = not_ready

ISteamInventory_GetItemPrice = not_ready

ISteamInventory_StartUpdateProperties = not_ready

ISteamInventory_RemoveProperty = not_ready

ISteamInventory_SetPropertyString = not_ready

ISteamInventory_SetPropertyBool = not_ready

ISteamInventory_SetPropertyInt64 = not_ready

ISteamInventory_SetPropertyFloat = not_ready

ISteamInventory_SubmitUpdateProperties = not_ready

ISteamInventory_InspectItem = not_ready

SteamInventory_v003 = not_ready

def SteamInventory(): # type: () -> ISteamInventory
    return SteamInventory_v003().contents

SteamGameServerInventory_v003 = not_ready

def SteamGameServerInventory(): # type: () -> ISteamInventory
    return SteamGameServerInventory_v003().contents

ISteamVideo_GetVideoURL = not_ready

ISteamVideo_IsBroadcasting = not_ready

ISteamVideo_GetOPFSettings = not_ready

ISteamVideo_GetOPFStringForApp = not_ready

SteamVideo_v002 = not_ready

def SteamVideo(): # type: () -> ISteamVideo
    return SteamVideo_v002().contents

ISteamParentalSettings_BIsParentalLockEnabled = not_ready

ISteamParentalSettings_BIsParentalLockLocked = not_ready

ISteamParentalSettings_BIsAppBlocked = not_ready

ISteamParentalSettings_BIsAppInBlockList = not_ready

ISteamParentalSettings_BIsFeatureBlocked = not_ready

ISteamParentalSettings_BIsFeatureInBlockList = not_ready

SteamParentalSettings_v001 = not_ready

def SteamParentalSettings(): # type: () -> ISteamParentalSettings
    return SteamParentalSettings_v001().contents

ISteamRemotePlay_GetSessionCount = not_ready

ISteamRemotePlay_GetSessionID = not_ready

ISteamRemotePlay_GetSessionSteamID = not_ready

ISteamRemotePlay_GetSessionClientName = not_ready

ISteamRemotePlay_GetSessionClientFormFactor = not_ready

ISteamRemotePlay_BGetSessionClientResolution = not_ready

ISteamRemotePlay_BSendRemotePlayTogetherInvite = not_ready

SteamRemotePlay_v001 = not_ready

def SteamRemotePlay(): # type: () -> ISteamRemotePlay
    return SteamRemotePlay_v001().contents

ISteamNetworkingMessages_SendMessageToUser = not_ready

ISteamNetworkingMessages_ReceiveMessagesOnChannel = not_ready

ISteamNetworkingMessages_AcceptSessionWithUser = not_ready

ISteamNetworkingMessages_CloseSessionWithUser = not_ready

ISteamNetworkingMessages_CloseChannelWithUser = not_ready

ISteamNetworkingMessages_GetSessionConnectionInfo = not_ready

SteamNetworkingMessages_SteamAPI_v002 = not_ready

def SteamNetworkingMessages_SteamAPI(): # type: () -> ISteamNetworkingMessages
    return SteamNetworkingMessages_SteamAPI_v002().contents

SteamGameServerNetworkingMessages_SteamAPI_v002 = not_ready

def SteamGameServerNetworkingMessages_SteamAPI(): # type: () -> ISteamNetworkingMessages
    return SteamGameServerNetworkingMessages_SteamAPI_v002().contents

ISteamNetworkingSockets_CreateListenSocketIP = not_ready

ISteamNetworkingSockets_ConnectByIPAddress = not_ready

ISteamNetworkingSockets_CreateListenSocketP2P = not_ready

ISteamNetworkingSockets_ConnectP2P = not_ready

ISteamNetworkingSockets_AcceptConnection = not_ready

ISteamNetworkingSockets_CloseConnection = not_ready

ISteamNetworkingSockets_CloseListenSocket = not_ready

ISteamNetworkingSockets_SetConnectionUserData = not_ready

ISteamNetworkingSockets_GetConnectionUserData = not_ready

ISteamNetworkingSockets_SetConnectionName = not_ready

ISteamNetworkingSockets_GetConnectionName = not_ready

ISteamNetworkingSockets_SendMessageToConnection = not_ready

ISteamNetworkingSockets_SendMessages = not_ready

ISteamNetworkingSockets_FlushMessagesOnConnection = not_ready

ISteamNetworkingSockets_ReceiveMessagesOnConnection = not_ready

ISteamNetworkingSockets_GetConnectionInfo = not_ready

ISteamNetworkingSockets_GetConnectionRealTimeStatus = not_ready

ISteamNetworkingSockets_GetDetailedConnectionStatus = not_ready

ISteamNetworkingSockets_GetListenSocketAddress = not_ready

ISteamNetworkingSockets_CreateSocketPair = not_ready

ISteamNetworkingSockets_ConfigureConnectionLanes = not_ready

ISteamNetworkingSockets_GetIdentity = not_ready

ISteamNetworkingSockets_InitAuthentication = not_ready

ISteamNetworkingSockets_GetAuthenticationStatus = not_ready

ISteamNetworkingSockets_CreatePollGroup = not_ready

ISteamNetworkingSockets_DestroyPollGroup = not_ready

ISteamNetworkingSockets_SetConnectionPollGroup = not_ready

ISteamNetworkingSockets_ReceiveMessagesOnPollGroup = not_ready

ISteamNetworkingSockets_ReceivedRelayAuthTicket = not_ready

ISteamNetworkingSockets_FindRelayAuthTicketForServer = not_ready

ISteamNetworkingSockets_ConnectToHostedDedicatedServer = not_ready

ISteamNetworkingSockets_GetHostedDedicatedServerPort = not_ready

ISteamNetworkingSockets_GetHostedDedicatedServerPOPID = not_ready

ISteamNetworkingSockets_GetHostedDedicatedServerAddress = not_ready

ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket = not_ready

ISteamNetworkingSockets_GetGameCoordinatorServerLogin = not_ready

ISteamNetworkingSockets_ConnectP2PCustomSignaling = not_ready

ISteamNetworkingSockets_ReceivedP2PCustomSignal = not_ready

ISteamNetworkingSockets_GetCertificateRequest = not_ready

ISteamNetworkingSockets_SetCertificate = not_ready

ISteamNetworkingSockets_ResetIdentity = not_ready

ISteamNetworkingSockets_RunCallbacks = not_ready

ISteamNetworkingSockets_BeginAsyncRequestFakeIP = not_ready

ISteamNetworkingSockets_GetFakeIP = not_ready

ISteamNetworkingSockets_CreateListenSocketP2PFakeIP = not_ready

ISteamNetworkingSockets_GetRemoteFakeIPForConnection = not_ready

ISteamNetworkingSockets_CreateFakeUDPPort = not_ready

SteamNetworkingSockets_SteamAPI_v012 = not_ready

def SteamNetworkingSockets_SteamAPI(): # type: () -> ISteamNetworkingSockets
    return SteamNetworkingSockets_SteamAPI_v012().contents

SteamGameServerNetworkingSockets_SteamAPI_v012 = not_ready

def SteamGameServerNetworkingSockets_SteamAPI(): # type: () -> ISteamNetworkingSockets
    return SteamGameServerNetworkingSockets_SteamAPI_v012().contents

ISteamNetworkingUtils_AllocateMessage = not_ready

ISteamNetworkingUtils_InitRelayNetworkAccess = not_ready

ISteamNetworkingUtils_GetRelayNetworkStatus = not_ready

ISteamNetworkingUtils_GetLocalPingLocation = not_ready

ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations = not_ready

ISteamNetworkingUtils_EstimatePingTimeFromLocalHost = not_ready

ISteamNetworkingUtils_ConvertPingLocationToString = not_ready

ISteamNetworkingUtils_ParsePingLocationString = not_ready

ISteamNetworkingUtils_CheckPingDataUpToDate = not_ready

ISteamNetworkingUtils_GetPingToDataCenter = not_ready

ISteamNetworkingUtils_GetDirectPingToPOP = not_ready

ISteamNetworkingUtils_GetPOPCount = not_ready

ISteamNetworkingUtils_GetPOPList = not_ready

ISteamNetworkingUtils_GetLocalTimestamp = not_ready

ISteamNetworkingUtils_SetDebugOutputFunction = not_ready

ISteamNetworkingUtils_IsFakeIPv4 = not_ready

ISteamNetworkingUtils_GetIPv4FakeIPType = not_ready

ISteamNetworkingUtils_GetRealIdentityForFakeIP = not_ready

ISteamNetworkingUtils_SetGlobalConfigValueInt32 = not_ready

ISteamNetworkingUtils_SetGlobalConfigValueFloat = not_ready

ISteamNetworkingUtils_SetGlobalConfigValueString = not_ready

ISteamNetworkingUtils_SetGlobalConfigValuePtr = not_ready

ISteamNetworkingUtils_SetConnectionConfigValueInt32 = not_ready

ISteamNetworkingUtils_SetConnectionConfigValueFloat = not_ready

ISteamNetworkingUtils_SetConnectionConfigValueString = not_ready

ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged = not_ready

ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged = not_ready

ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged = not_ready

ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult = not_ready

ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest = not_ready

ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed = not_ready

ISteamNetworkingUtils_SetConfigValue = not_ready

ISteamNetworkingUtils_SetConfigValueStruct = not_ready

ISteamNetworkingUtils_GetConfigValue = not_ready

ISteamNetworkingUtils_GetConfigValueInfo = not_ready

ISteamNetworkingUtils_IterateGenericEditableConfigValues = not_ready

ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString = not_ready

ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString = not_ready

ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType = not_ready

ISteamNetworkingUtils_SteamNetworkingIdentity_ToString = not_ready

ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString = not_ready

SteamNetworkingUtils_SteamAPI_v004 = not_ready

def SteamNetworkingUtils_SteamAPI(): # type: () -> ISteamNetworkingUtils
    return SteamNetworkingUtils_SteamAPI_v004().contents

ISteamGameServer_SetProduct = not_ready

ISteamGameServer_SetGameDescription = not_ready

ISteamGameServer_SetModDir = not_ready

ISteamGameServer_SetDedicatedServer = not_ready

ISteamGameServer_LogOn = not_ready

ISteamGameServer_LogOnAnonymous = not_ready

ISteamGameServer_LogOff = not_ready

ISteamGameServer_BLoggedOn = not_ready

ISteamGameServer_BSecure = not_ready

ISteamGameServer_GetSteamID = not_ready

ISteamGameServer_WasRestartRequested = not_ready

ISteamGameServer_SetMaxPlayerCount = not_ready

ISteamGameServer_SetBotPlayerCount = not_ready

ISteamGameServer_SetServerName = not_ready

ISteamGameServer_SetMapName = not_ready

ISteamGameServer_SetPasswordProtected = not_ready

ISteamGameServer_SetSpectatorPort = not_ready

ISteamGameServer_SetSpectatorServerName = not_ready

ISteamGameServer_ClearAllKeyValues = not_ready

ISteamGameServer_SetKeyValue = not_ready

ISteamGameServer_SetGameTags = not_ready

ISteamGameServer_SetGameData = not_ready

ISteamGameServer_SetRegion = not_ready

ISteamGameServer_SetAdvertiseServerActive = not_ready

ISteamGameServer_GetAuthSessionTicket = not_ready

ISteamGameServer_BeginAuthSession = not_ready

ISteamGameServer_EndAuthSession = not_ready

ISteamGameServer_CancelAuthTicket = not_ready

ISteamGameServer_UserHasLicenseForApp = not_ready

ISteamGameServer_RequestUserGroupStatus = not_ready

ISteamGameServer_GetGameplayStats = not_ready

ISteamGameServer_GetServerReputation = not_ready

ISteamGameServer_GetPublicIP = not_ready

ISteamGameServer_HandleIncomingPacket = not_ready

ISteamGameServer_GetNextOutgoingPacket = not_ready

ISteamGameServer_AssociateWithClan = not_ready

ISteamGameServer_ComputeNewPlayerCompatibility = not_ready

ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED = not_ready

ISteamGameServer_CreateUnauthenticatedUserConnection = not_ready

ISteamGameServer_SendUserDisconnect_DEPRECATED = not_ready

ISteamGameServer_BUpdateUserData = not_ready

SteamGameServer_v014 = not_ready

def SteamGameServer(): # type: () -> ISteamGameServer
    return SteamGameServer_v014().contents

ISteamGameServerStats_RequestUserStats = not_ready

ISteamGameServerStats_GetUserStatInt32 = not_ready

ISteamGameServerStats_GetUserStatFloat = not_ready

ISteamGameServerStats_GetUserAchievement = not_ready

ISteamGameServerStats_SetUserStatInt32 = not_ready

ISteamGameServerStats_SetUserStatFloat = not_ready

ISteamGameServerStats_UpdateUserAvgRateStat = not_ready

ISteamGameServerStats_SetUserAchievement = not_ready

ISteamGameServerStats_ClearUserAchievement = not_ready

ISteamGameServerStats_StoreUserStats = not_ready

SteamGameServerStats_v001 = not_ready

def SteamGameServerStats(): # type: () -> ISteamGameServerStats
    return SteamGameServerStats_v001().contents

ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort = not_ready

ISteamNetworkingFakeUDPPort_SendMessageToFakeIP = not_ready

ISteamNetworkingFakeUDPPort_ReceiveMessages = not_ready

ISteamNetworkingFakeUDPPort_ScheduleCleanup = not_ready

Init = not_ready

Shutdown = not_ready

RestartAppIfNecessary = not_ready

ReleaseCurrentThreadMemory = not_ready

WriteMiniDump = not_ready

SetMiniDumpComment = not_ready

ManualDispatch_Init = not_ready

ManualDispatch_RunFrame = not_ready

ManualDispatch_GetNextCallback = not_ready

ManualDispatch_FreeLastCallback = not_ready

ManualDispatch_GetAPICallResult = not_ready

GetHSteamPipe = not_ready

GetHSteamUser = not_ready

RunCallbacks = not_ready
class CallbackMsg_t(Structure):
    _fields_ = [
        ( "m_hSteamUser", c_int),
        ( "m_iCallback", c_int),
        ( "m_pubParam", c_void_p),
        ( "m_cubParam", c_int),
        ]

    _pack_ = PACK

hSteamPipe = None

def init_callbacks():
    """
    This initializes Steam callback handling. It should be called after
    Init but before any other call.
    """

    global hSteamPipe
    ManualDispatch_Init()
    hSteamPipe = GetHSteamPipe()

def generate_callbacks():
    """
    This generates the callback objects produced by Steam. This needs to be
    iterated over once per frame to make sure the callbacks are
    processed and the screen is updated.

    The callbacks are generated of the

    """

    if hSteamPipe is None:
        raise RuntimeError("Please call steamapi.init_callbacks() before this function.")

    ManualDispatch_RunFrame(hSteamPipe)

    message = CallbackMsg_t()

    while ManualDispatch_GetNextCallback(hSteamPipe, byref(message)):

        callback_type = callback_by_id.get(message.m_iCallback, None)

        if callback_type is not None:
            cb = cast(message.m_pubParam, POINTER(callback_type)).contents
            yield cb

        ManualDispatch_FreeLastCallback(hSteamPipe)

class APIFailure(Exception):
    pass

def get_api_call_result(call, callback_type):
    """
    Returns the result of an API call.

    `call`
        The SteamAPICall_t returned by the call.

    `callback_type`
        Either the type or an integer representing the type of the API call.

    This returns an object of callback_type if the call completed, None if
    the call hasn't finished, and raises APIFailure if the call failed. (It's
    recommended that APIFailures are caught and the API call retried.)

    One way to use this is with the SteamAPICallCompleted_t callback::

        for i in steamapi.generate_callbacks():
            if isinstance(i, steamapi.SteamAPICallCompleted_t):
                result = steamapi.get_api_call_result(i.m_hAsyncCall, i.m_iCallback)
                print("The result of", i.m_hAsyncCall, "is", result)
            else:
                # Handle other callbacks.
    """

    failure = c_bool()

    if not SteamUtils().IsAPICallCompleted(call, byref(failure)):
        return None

    if failure:
        raise APIFailure(call)

    if isinstance(callback_type, int):
        callback_type = callback_by_id[callback_type]

    result = callback_type()

    if not SteamUtils().GetAPICallResult(call, byref(result), sizeof(result), callback_type.callback_id, byref(failure)):
        raise APIFailure(call)

    if failure:
        raise APIFailure(call)

    return result

