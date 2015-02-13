#!/bin/bash


# This is the location of the edwin main package.py
EDWIN_DIR="/home/darkness/notebooks/edwin/python2"

# This is the location of your orgs custom files.  This should be outside of the git repository to keep things clean. 
# Note if this location does not exist, it will create it and put the blank edwin custom files in it. 
EDWIN_CUSTOM="/home/darkness/notebooks/edwin_custom/python2"

# This is for user development and other per user settings. If this file doesn't exist, it will create it
EDWIN_USER=~/edwin.py

# The profile you want edwin installed to. 

PROFILE="default"
PROFILE_DIR=~/.ipython/profile_"$PROFILE"

####################################
echo "The Edwin Directory is $EDWIN_DIR"
echo "The Edwin Custom Directory is $EDWIN_CUSTOM"
echo "The User Edwin File is $EDWIN_USER"
echo "Profile: $PROFILE"
echo "The Profile Directory is $PROFILE_DIR"


###################################
# Check directores and files for edwin custom
echo "Checking for $EDWIN_CUSTOM"
if [ -d "$EDWIN_CUSTOM" ]; then
    echo "$EDWIN_CUSTOM exists checking for files"
    if [ -f "$EDWIN_CUSTOM/edwin_imports_custom.py" ]; then
        echo "Custom files found, no actions taken"
    else
        echo "$EDWIN_CUSTOM Exists, but no files: adding"
        cp "$EDWIN_DIR/edwin_*_custom.py" "$EDWIN_CUSTOM/"
    fi
else
    echo "$EDWIN_CUSTOM Does not Exist: Creating"
    mkdir -p $EDWIN_CUSTOM
    if [ ! -d "$EDWIN_CUSTOM" ]; then
        echo "Creation of $EDWIN_CUSTOM did not work. Are you sure you have permissions?"
        exit 1
    else
       cp $EDWIN_DIR/edwin_*_custom.py $EDWIN_CUSTOM/
    fi
fi

###################################
# Check to see if the user edwin exists. If not, just copy the blank one from the git
if [ ! -f "$EDWIN_USER" ]; then
    cp $EDWIN_DIR/edwin.py $EDWIN_USER 
fi


####################################
if [ -d "$PROFILE_DIR" ]; then
    PROFILE_STARTUP="$PROFILE_DIR/startup"
    if [ -d $PROFILE_STARTUP ]; then
        rm $PROFILE_STARTUP/*-edwin*

        echo "ln -s $EDWIN_DIR/edwin_imports.py $PROFILE_STARTUP/00-edwin_imports.py"
        ln -s $EDWIN_DIR/edwin_imports.py $PROFILE_STARTUP/00-edwin_imports.py

        echo "ln -s $EDWIN_CUSTOM/edwin_imports_custom.py $PROFILE_STARTUP/01-edwin_imports_custom.py"
        ln -s $EDWIN_CUSTOM/edwin_imports_custom.py $PROFILE_STARTUP/01-edwin_imports_custom.py

        echo "ln -s $EDWIN_DIR/edwin_vars.py $PROFILE_STARTUP/02-edwin_vars.py"
        ln -s $EDWIN_DIR/edwin_vars.py $PROFILE_STARTUP/02-edwin_vars.py

        echo "ln -s $EDWIN_CUSTOM/edwin_vars_custom.py $PROFILE_STARTUP/03-edwin_vars_custom.py"
        ln -s $EDWIN_CUSTOM/edwin_vars_custom.py $PROFILE_STARTUP/03-edwin_vars_custom.py

        echo "ln -s $EDWIN_DIR/edwin_funcs.py $PROFILE_STARTUP/04-edwin_funcs.py"
        ln -s $EDWIN_DIR/edwin_funcs.py $PROFILE_STARTUP/04-edwin_funcs.py
 
        echo "ln -s $EDWIN_CUSTOM/edwin_funcs_custom.py $PROFILE_STARTUP/05-edwin_funcs_custom.py"
        ln -s $EDWIN_CUSTOM/edwin_funcs_custom.py $PROFILE_STARTUP/05-edwin_funcs_custom.py

        echo "ln -s $EDWIN_DIR/edwin_magics.py $PROFILE_STARTUP/06-edwin_magics.py"
        ln -s $EDWIN_DIR/edwin_magics.py $PROFILE_STARTUP/06-edwin_magics.py

        echo "ln -s $EDWIN_CUSTOM/edwin_magics_custom.py $PROFILE_STARTUP/07-edwin_magics_custom.py"
        ln -s $EDWIN_CUSTOM/edwin_magics_custom.py $PROFILE_STARTUP/07-edwin_magics_custom.py

        echo "ln -s $EDWIN_DIR/edwin_vis.py $PROFILE_STARTUP/08-edwin_vis.py"
        ln -s $EDWIN_DIR/edwin_vis.py $PROFILE_STARTUP/08-edwin_vis.py

        echo "ln -s $EDWIN_CUSTOM/edwin_vis_custom.py $PROFILE_STARTUP/09-edwin_vis_custom.py"
        ln -s $EDWIN_CUSTOM/edwin_vis_custom.py $PROFILE_STARTUP/09-edwin_vis_custom.py

        echo "Adding User Local Edwins"
        echo "ln -s $EDWIN_USER $PROFILE_STARTUP/10-edwin.py"
        ln -s $EDWIN_USER $PROFILE_STARTUP/10-edwin_user.py
    else
        echo "Sorry, while the profile seems to exist, the startup dir does not, please check into that"
    fi
else
    echo "That profile doesn't exist, please check your profile name and run ./install_edwin.sh %PROFILENAME%"
fi
