' Set WshShell = CreateObject("WScript.Shell")
' WshShell.Run "wezterm start -- cmd /k python .\Desktop\code22\main.py", 0, false

Set WshShell = CreateObject("WScript.Shell")

Dim scriptPath
scriptPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

Dim command
command = "wezterm start -- cmd /k cd " & Chr(34) & scriptPath & Chr(34) & " && python main.py"

WshShell.Run command, 0, false