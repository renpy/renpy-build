Text = WScript.Arguments(0)
Speaker = WScript.Arguments(1)
Volume = WScript.Arguments(2)

Set s = CreateObject("SAPI.SpVoice")

s.Volume = Volume

For Each Voice In s.GetVoices
    I = I + 1

    If InStr(Voice.GetDescription, Speaker) > 0 Then
        Set s.Voice = s.GetVoices.Item(I-1)
        Exit For
    End If
Next

s.Speak Text
