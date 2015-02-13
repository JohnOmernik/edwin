#!/bin/bash

echo "Usage is: ./install_edwin.sh %PATHTOEDWIN% %PROFILENAME%"
echo "Example: ./install_edwin.sh /home/user1/notebooks/edwin default"


EDWIN_DIR=$1
PROFILE=$2

echo "The Edwin Directory is $EDWIN_DIR"
echo "Profile: $PROFILE"


PROFILE_DIR=~/.ipython/profile_"$PROFILE"

echo "The Profile Directory is $PROFILE_DIR"


if [ -d "$PROFILE_DIR" ]; then
    PROFILE_STARTUP="$PROFILE_DIR/startup"
    if [ -d $PROFILE_STARTUP ]; then
        rm $PROFILE_STARTUP/*-edwin*
        echo "ln -s $EDWIN_DIR/edwin_imports.py $PROFILE_STARTUP/00-edwin_imports.py"
        ln -s $EDWIN_DIR/edwin_imports.py $PROFILE_STARTUP/00-edwin_imports.py
        echo "ln -s $EDWIN_DIR/edwin_imports_custom.py $PROFILE_STARTUP/01-edwin_imports_custom.py"
        ln -s $EDWIN_DIR/edwin_imports_custom.py $PROFILE_STARTUP/01-edwin_imports_custom.py
        echo "ln -s $EDWIN_DIR/edwin_vars.py $PROFILE_STARTUP/02-edwin_vars.py"
        ln -s $EDWIN_DIR/edwin_vars.py $PROFILE_STARTUP/02-edwin_vars.py
        echo "ln -s $EDWIN_DIR/edwin_vars_custom.py $PROFILE_STARTUP/03-edwin_vars_custom.py"
        ln -s $EDWIN_DIR/edwin_vars_custom.py $PROFILE_STARTUP/03-edwin_vars_custom.py
        echo "ln -s $EDWIN_DIR/edwin_funcs.py $PROFILE_STARTUP/04-edwin_funcs.py"
        ln -s $EDWIN_DIR/edwin_funcs.py $PROFILE_STARTUP/04-edwin_funcs.py
        echo "ln -s $EDWIN_DIR/edwin_funcs_custom.py $PROFILE_STARTUP/05-edwin_funcs_custom.py"
        ln -s $EDWIN_DIR/edwin_funcs_custom.py $PROFILE_STARTUP/05-edwin_funcs_custom.py
        echo "ln -s $EDWIN_DIR/edwin_magics.py $PROFILE_STARTUP/06-edwin_magics.py"
        ln -s $EDWIN_DIR/edwin_magics.py $PROFILE_STARTUP/06-edwin_magics.py
        echo "ln -s $EDWIN_DIR/edwin_magics_custom.py $PROFILE_STARTUP/07-edwin_magics_custom.py"
        ln -s $EDWIN_DIR/edwin_magics_custom.py $PROFILE_STARTUP/07-edwin_magics_custom.py
        echo "ln -s $EDWIN_DIR/edwin_vis.py $PROFILE_STARTUP/08-edwin_vis.py"
        ln -s $EDWIN_DIR/edwin_vis.py $PROFILE_STARTUP/08-edwin_vis.py
        echo "ln -s $EDWIN_DIR/edwin_vis_custom.py $PROFILE_STARTUP/09-edwin_vis_custom.py"
        ln -s $EDWIN_DIR/edwin_vis_custom.py $PROFILE_STARTUP/09-edwin_vis_custom.py
        echo "ln -s $EDWIN_DIR/edwin.py $PROFILE_STARTUP/10-edwin.py"
        ln -s $EDWIN_DIR/edwin.py $PROFILE_STARTUP/10-edwin.py
    else
        echo "Sorry, while the profile seems to exist, the startup dir does not, please check into that"
    fi
else
    echo "That profile doesn't exist, please check your profile name and run ./install_edwin.sh %PROFILENAME%"
fi
