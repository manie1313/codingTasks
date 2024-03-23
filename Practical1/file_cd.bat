"For some reason, the script didn't want to change directory to the
"1st directory, resulting in 4 folders ( avada..., YYD, whoiswho and dumbledor)
"To bypass this, install the Debugger for Mainframe v1.9.0
"(didn't add manually the extension .bat, instead added batch as file type directly)
"Actually, I don't know why the interpreter runs the old version of the code and don't reload 
"the new version of the actual code 


mkdir avada_kedavra
mkdir YYD
mkdir whoiswho

cd avada_kedavra
mkdir voldemort
mkdir agrid
mkdir dumbledor
rmdir voldemort
rmdir agrid