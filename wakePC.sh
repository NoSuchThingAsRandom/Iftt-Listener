sam="D8:CB:8A:3C:35:CA"
pete="48:0F:CF:58:B4:DA"
if ["$1"="SAM"]; then
    echo "Booting Sam"
    etherwake $sam
elif ["$2"="PETE"]; then
    echo "Booting Pete"
    etherwake $pete
else
    echo "Unknown mac"
fi
exit
