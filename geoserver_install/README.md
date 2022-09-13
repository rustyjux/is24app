# GeoServer Installer

## Installation
- install Java 8 (available from https://www.java.com/en/download/manual.jsp)
- run install.bat **as administrator** (in `/geoserver_install`)

This batch script:
- downloads the latest stable build in platform independent binary form from SourceForge
- uninstalls previous installs in C:\Program Files
- extracts the archive
- sets up the necessary environment variables (user-only)

## Run GeoServer
- run cmd.exe **as admin**, enter the command `"C:\Program Files\GeoServer\bin\startup.bat"`

## Notes
- The batch file is a quick and dirty solution for installation
- An MSI installer would have been a much better solution. Such an installer could be created using Visual Studio Installer Project or WiX, but I didn't have access to VS with the extension nor the time to learn WiX.
    - Why MSI? Reliable silent running, smoother uninstall, elevated installation rights (no messy temporary admin rights), administrative installation (file extract - essential for corporate repackaging), verbose logging, rollback support, inventory (full registration of what is installed and where)
- Silent installation of the Java requirement could have been added, see:
    - https://www.java.com/en/download/help/silent_install.html
    - https://docs.oracle.com/javase/8/docs/technotes/guides/install/windows_installer_options.html