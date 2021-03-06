SIMDEM_VERSION = "0.8.0-dev"
SIMDEM_TEMP_DIR = "~/.simdem/tmp"

# When in demo mode we insert a small random delay between characters.
# TYPING DELAY is the upper bound of this delay.
TYPING_DELAY = 0.08

# Prompt to use in the console
console_prompt = "$ "

# Port for web server when running with '--webui true' optios
port = 8080

# ------------------------------------------------------------------ #
# Danger zone
#
# Do not change anything after this notice,
# unless you know what you are doing
# ------------------------------------------------------------------ #

# Set is_debug to True if you want to run in debug mode. This setting
# can be overriden in the command like with the `--debug true` option.
is_debug = False

# Available modes of execution
modes = [ "tutorial", "demo", "learn", "test", "script" ]


