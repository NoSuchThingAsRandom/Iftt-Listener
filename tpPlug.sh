#!/bin/bash
ip="$1"
status="$2"
port=9999

payload_on="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="

payload_off="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="

if [ "$status" = "on" ]; then
	echo "on"
	echo -n $payload_on | base64 -d | nc $ip $port
elif [ "$status" = "off" ]; then
	echo "off"
	echo -n $payload_off | base64 -d | nc $ip $port

else
	echo "Unknown option"
fi
exit
