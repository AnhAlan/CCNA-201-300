- When to Reset / Recovery
Forgot password → cannot login console or VTY lines
Device misconfiguration → cannot function properly
Delete all configuration → reset to default settings
Upgrade / downgrade IOS

1. Reload
Router# reload
- Device restarts but keeps current configuration.

2. Remove the default settings.
Router# write erase       # or erase startup-config
Router# reload

Device boots without any configuration
VTY, VLAN, IP → reset to default

3. Password Recovery / login ROMMON
- Turn the device off and then back on (Unplug the appliance and plug it back in).
- Press repeatedly "Ctrl + Break" (or only "break") when device start boot 
(Note: On laptops using a console adapter, this might be "Ctrl + Fn + B")
- device login ROMMON mode

rommon 1 > 

rommon 2 > dir flash: // Check if startup-config still exists:
         File size           Checksum   File name
 486899872 bytes (0x1d0580a0) 0x9da5    isr4300-universalk9.16.06.04.SPA.bin
     28282 bytes (0x6e7a)     0x6e7a    sigdef-category.xml
    227537 bytes (0x378d1)    0x78d4    sigdef-default.xml
rommon 3 > 

rommon 4 > confreg 0x2142 // Skip Startup-config during boot.
rommon 5 > reset

- When iOS starts up, you are in privileged EXEC mode without a password.
Router> enable
Router# copy startup-config running-config

- Change password:
Router(config)# enable secret 1234
Router(config)# username annk secret ccna

- Restore normal boot configuration
Reset ROMMON configuration values:
Router(config)# config-register 0x2102

- Save the configuration and reload:
Router# write memory
Router# reload
Device boots with old configuration + new password

✅ Notes
0x2142 → skip startup-config
0x2102 → normal boot, read startup-config
Always backup configuration before reset/recovery

That means we enter confreg 0x2142 to skip the startup configuration → after reloading, we can access the existing configuration, change the password, and restore the normal boot configuration.
login rommon mode -> confreg 0x0142 to skip startup config -> reload -> login config without password -> change password -> enable startup config again