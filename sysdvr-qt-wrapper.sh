#!/bin/bash

if [ ! -e "$XDG_CONFIG_HOME/options.json" ]; then
	cat <<- EOF > "$XDG_CONFIG_HOME/options.json"
		{
		    "recordingsPath": "$(xdg-user-dir VIDEOS)/SysDVR",
		    "screenshotsPath": "$(xdg-user-dir PICTURES)/SysDVR"
		}
	EOF
fi

exec sysdvr-qt "$@"
