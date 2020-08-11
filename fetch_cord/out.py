from .bash import exec_bash, BashError
import sys
import os
baseinfo = exec_bash("neofetch --stdout --config none")
#make lists
cpu = "CPU:"
cpuline = []
nvidiagpu = "GPU: NVIDIA"
nvidiagpuline = []
amdgpu = "GPU: AMD"
amdgpuline = []
intelgpu = "GPU: Intel"
intelgpuline = []
term = "Terminal:"
termline = []
termfont = "Terminal Font:"
termfontline = []
wm = "WM:"
wmline = []
de = "DE:"
deline = []
shell = "Shell:"
shell_line = []
kernel = "Kernel:"
kernelline = []
sysos = "OS:"
sysosline = []
packages = "Packages:"
packagesline = []
filepath="/tmp/out.txt"
with open(filepath, 'w') as f:
    print(baseinfo, file=f)
with open(filepath, "rt") as f:
    for line in f:
        if line.find(cpu) != -1:
            cpuline.append(line.rstrip('\n'))
        if line.find(nvidiagpu) != -1:
            nvidiagpuline.append(line.rstrip('\n'))
        if line.find(amdgpu) != -1:
            amdgpuline.append(line.rstrip('\n'))
        if line.find(intelgpu) != -1:
            intelgpuline.append(line.rstrip('\n'))
        if line.find(term) != -1:
            termline.append(line.rstrip('\n'))
        if line.find(termfont) != -1:
            termfontline.append(line.rstrip('\n'))
        if line.find(de) != -1:
            deline.append(line.rstrip('\n'))
        if line.find(wm) != -1:
            wmline.append(line.rstrip('\n'))
        if line.find(shell) != -1:
            shell_line.append(line.rstrip('\n'))
        if line.find(packages) != -1:
            packagesline.append(line.rstrip('\n'))
        if line.find(kernel) != -1:
            kernelline.append(line.rstrip('\n'))
        if line.find(sysos) != -1:
            sysosline.append(line.rstrip('\n'))
try:
    if os.path.isfile(filepath):
        os.remove(filepath)
except FileNotFoundError:
    pass
gpuvendor = "none"
sysosid = sysosline[0].split()[1]
if sysosid.lower() != "macos":
    try:
        check_provider = exec_bash("xrandr --listproviders | grep -o \"NVIDIA.*\"")
    except BashError:
        pass
        check_provider = ""
        print(check_provider)
    if check_provider == "" and not intelgpuline:
        try:
            if amdgpuline:
            # amd GPUs
                gpuline = "GPU: " + exec_bash("glxinfo | grep \"OpenGL renderer string:\" | sed 's/^.*: //;s/(.*//;s/Mesa //'")
                gpuvendor = gpuline.split()[1]
                gpuinfo = gpuline
                gpuid = gpuline
                print(gpuid)
                print(gpuline)
        except BashError as e:
            print("ERROR: Could not run glxinfo [%s]" % str(e))
            sys.exit(1)
    else:
        if nvidiagpuline:
            gpuvendor = nvidiagpuline[0].split()[1]
            gpuinfo = nvidiagpuline[0]
            print(gpuinfo)
            print(gpuvendor)
            print(nvidiagpuline)
        if intelgpuline and not nvidiagpuline:
            gpuvendor = intelgpuline[0].split()[1]
            gpuinfo = intelgpuline[0]
            print(gpuinfo)
            print(gpuvendor)
            print(intelgpuline)
cpuvendor = cpuline[0].split()[1]
if cpuvendor == "Intel":
    cpumodel = cpuline[0].replace('-', ' ').split()[1] + ' ' + cpuline[0].replace('-', ' ').split()[2]
elif cpuvendor == "AMD":
    cpumodel = cpuline[0].split()[2] + ' ' + cpuline[0].split()[3]
cpuinfo = cpuline[0].join(cpuline)[5:]
wmid = wmline[0].split()[1]
termid = termline[0].split()[1]
shellid = shell_line[0].split()[1]
kernelid = kernelline[0].split()[1]
if not termfontline:
    termfontline = []
    termfontline.append("Terminal font: N/A")
    print(termfontline[0])
if deline:
    deid = deline[0].split()[1]
    print(deid)
else:
    deid = "none"
print(wmid)
print(termid)
print(cpuvendor)
print(cpumodel)
print(cpuinfo)
print(packagesline[0])
print(cpuline[0])
print(termline[0])
print(sysosid)
print(sysosline[0])
print(wmline[0])
