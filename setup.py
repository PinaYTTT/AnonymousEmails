from cx_Freeze import setup, Executable

setup( name = "AnonymousEmails",
        version = "1.0",
        description = "Crea Emails anonimos para que nadie sepa que los mandaste",
        icon = "Logo.ico",
        executables = [Executable("Main.py")],)