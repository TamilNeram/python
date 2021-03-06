
[Setup]
    AppName=PAGE - A Python GUI Generator
    AppId=PAGE - A Python GUI Generator
    CreateUninstallRegKey=1
    UsePreviousAppDir=1
    UsePreviousGroup=1
    AppVersion=6.0a
    AppVerName=PAGE - A Python GUI Generator 6.0a
    BackColor=$FF0000
    BackColor2=$000000
    BackColorDirection=lefttoright
    WizardStyle=modern
    WindowShowCaption=1
    WindowStartMaximized=1
    WindowVisible=1
    WindowResizable=1
    UninstallLogMode=Append
    DirExistsWarning=auto
    UninstallFilesDir={app}
    DisableDirPage=0
    DisableStartupPrompt=0
    CreateAppDir=1
    DisableProgramGroupPage=0
    Uninstallable=1
    DefaultDirName=c:\page
    DefaultGroupName=PAGE
    AlwaysShowDirOnReadyPage=1
    EnableDirDoesntExistWarning=1
    ShowComponentSizes=1
    SourceDir=C:\Users\rozen\Desktop\page
    OutputDir=F:\
    OutputBaseFilename=page-6.0a


[Files]
    Source: C:\Users\rozen\Desktop\page\*; DestDir: {app}; Flags: recursesubdirs
    
[Icons]
    Name: "{userdesktop}\PAGE"; Filename: "{app}\winpage.bat"; WorkingDir: "{app}"; IconFilename: "{app}\WIN_INSTALL\page.ico"; Flags: runminimized closeonexit
    Name: "{group}\PAGE"; Filename: "{app}\winpage.bat"; WorkingDir: "{app}"

[Run]
	Filename: "{app}\WRITE.BAT"; Parameters: "{app}"	


[Code]
	function NeedsAddPathHKLM(Param: string): boolean;
	var
	OrigPath: string;
	begin
	if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
	'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
	'Path', OrigPath)
	then begin
	Result := True;
	exit;
	end;
	// look for the path with leading and trailing semicolon
	// Pos() returns 0 if not found
	Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
	end;

[Registry]

Root: "HKLM"; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPathHKLM(ExpandConstant('{app}'))
