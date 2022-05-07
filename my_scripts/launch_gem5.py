import subprocess
import os
import sys

NUM_CPUS=64
NUM_CHIPLETS=8

GEM5_DIR="/home/grads/g/ginochacon/gem5_garnet2_CHIPS_sni"
OUT_DIR="/home/grads/g/ginochacon/gem5_garnet2_CHIPS_sni/my_outdir/"
EXE_PATH = "/home/grads/g/ginochacon/spec_test/benchspec/CPU2006/"


args_in = sys.argv[1:]
assert(len(args_in) > 0)
print(str(args_in))

def check_running(benchmark):
    running = int(subprocess.check_output("ps -al | grep " + benchmark + " | wc -l",\
    stderr = subprocess.STDOUT, shell = True))

    #print(running)
    assert(running < 2)
    if running:
        return True
    else:
        return False

bm_names = ["perlbench", "gcc", "mcf", 
             "cactusADM", "namd", "soplex", 
             "calculix", "hmmer", "sjeng",
             "libquantum", "lbm", "astar", 
             "xalancbmk"]
mixes = {1 : "sjeng namd calculix cactusADM", #COMPLETE
2 : "namd mcf soplex perlbench", #COMPLETE
3 : "cactusADM lbm mcf namd", #COMPLETE
4 : "mcf astar libquantum hmmer", #COMPLETE
5 : "hmmer astar calculix perlbench", #COMPLETE
6 : "lbm hmmer astar soplex", #exe
7 : "astar cactusADM sjeng gcc", #exe
8 : "namd xalancbmk gcc perlbench", #COMPLETE
9 : "perlbench astar xalancbmk hmmer", #COMPLETE
10 : "soplex calculix hmmer lbm", #exe
11 : "soplex xalancbmk mcf calculix", #exe
12 : "gcc libquantum cactusADM soplex", #exe
13 : "perlbench sjeng cactusADM namd", #exe
14 : "astar calculix perlbench cactusADM", #exe
15 : "calculix xalancbmk hmmer lbm", #exe
16 : "gcc cactusADM sjeng perlbench",
42 : "astar astar"}


#HANGS :  gamess, gobmk, leslie3d,
#USER INPUT: milc
#BROKEN: bzip2 (FOLDER FORMAT), wrf
#Low number of instrs:  
                        #bwaves, zeusmp, gromacs, 
                        #povray, GemsFDTD, h264ref, tonto, omnetpp, sphinx3,

#Tested invididually and functions:
#[Executed Alone][In Gem5]
# H = HANG, L = Lower Exe time than expected
# C = Crashes
#[✓][✓]  perlbench
#[✓][C]  bzip2
#[✓][✓]  gcc
#[✓][L]  bwaves
#[H][H]  gamess
#[✓][✓]  mcf
#[H][H]  milc
#[✓][L]  zeusmp
#[✓][L]  gromacs
#[✓][✓]  cactusADM
#[H][H]  leslie3d
#[✓][✓]  namd
#[H][H]  gobmk
#[ ][ ]  dealII
#[✓][✓]  soplex
#[✓][L]  povray
#[✓][✓]  calculix
#[✓][✓]  hmmer
#[✓][✓]  sjeng
#[✓][L]  GemsFDTD
#[✓][✓]  libquantum
#[✓][L]  h264ref
#[✓][L]  tonto
#[✓][✓]  lbm
#[✓][L]  omnetpp
#[✓][✓]  astar
#[✓][C]  wrf
#[✓][L]  sphinx3
#[✓][✓]  xalancbmk
#[✓][ ]  specrand_i
#[✓][ ]  specrand_f

run_subdir = "/run/run_base_ref_amd64-m64-gcc43-nn.0000/"
exe_subname = "_base.amd64-m64-gcc43-nn"

run_dir_num = { "perlbench" : "400.", "bzip2" : "401.", "gcc" : "403.",\
                                "bwaves" : "410.", "gamess" : "416.", "mcf" : "429.",\
                                "milc" : "433.", "zeusmp" : "434.", "gromacs" : "435.",\
                                "cactusADM" : "436.", "leslie3d" : "437.", "namd" : "444.",\
                                "gobmk" : "445.", "dealII" : "447.", "soplex" : "450.", "povray" : "453.",\
                                "calculix" : "454.", "hmmer" : "456.", "sjeng" : "458.",\
                                "GemsFDTD" : "459.", "libquantum" : "462.", "h264ref" : "464.",\
                                "tonto" : "465.", "lbm" : "470.", "omnetpp" : "471.", "astar" : "473.",\
                                "wrf" : "481.", "sphinx3" : "482.", "xalancbmk" : "483.",\
                                "specrand_i" : "998.", "specrand_f" : "999."}

input_vals = {                  "perlbench"     : "-I{0}/lib {0}checkspam.pl 2500 5 25 11 150 1 1 1 1",
                                "bzip2"         : "{0}input.source 280",
                                "gcc"           : "{0}166.i -o 166.s",
                                "bwaves"        : "",
                                "gamess"        : "< {0}cytosine.2.config",
                                "mcf"           : "{0}inp.in",
                                "milc"          : "{0}su3imp.in",
                                "zeusmp"        : "",
                                "gromacs"       : "-silent -deffnm gromacs -nice 0",
                                "cactusADM"     : "{0}benchADM.par",
                                "leslie3d"      : "{0}leslie3d.in",
                                "namd"          : "--input {0}namd.input --output {0}namd.out --iterations 38",
                                "gobmk"         : "--quiet --mode gtp < {0}13x13.tst",
                                "dealII"        : "23",
                                "soplex"        : "-m45000 {0}pds-50.mps",
                                "povray"        : "{0}SPEC-benchmark-ref.ini",
                                "calculix"      : "-i {0}hyperviscoplastic",
                                "hmmer"         : "{0}nph3.hmm {0}swiss41",
                                "sjeng"         : "{0}ref.txt",
                                "GemsFDTD"      : "",
                                "libquantum"    : "1397 8",
                                "h264ref"       : "-d {0}foreman_ref_encoder_baseline.cfg",
                                "tonto"         : "",
                                "lbm"           : "300 {0}reference.dat 0 0 {0}100_100_130_ldc.of",
                                "omnetpp"       : "{0}omnetpp.ini",
                                "astar"         : "{0}rivers.cfg",\
                                "wrf"           : "", 
                                "sphinx3"       : "ctlfile . {0}args.an4", 
                                "xalancbmk"     : "-v {0}t5.xml {0}xalanc.xsl",\
                                "specrand_i"    : "1255432124 234923", 
                                "specrand_f"    : "1255432124 234923"} 

#substitute names for the SPEC workloads that do not conform to directory naming scheme....
sub_bin = {"xalancbmk" : "Xalan", "sphinx3" : "sphinx_livepretend", "specrand_i" : "specrand", "specrand_f" : "specrand"}
file_inputs = ["perlbench", "bzip2", "namd", "gcc", "gamess", "mcf", "milc", "cactusADM", "calculix", "hmmer",\
              "sjeng", "h264ref", "lbm", "omnetpp", "astar", "sphinx3", "xalancbmk", "soplex", "povray"]
#launch form:
#"EXE_PATH + run_dir_num[bench] + bench + run_subdir + bench + exe_subname " + input_vals[bench]

cwd = os.getcwd()

#for each of the arguments create a cmd and the required inputs
cmds = []
inputs = []

if "mix" in args_in[0]:
    mix_split = args_in[0].split("_")
    if len(mix_split) < 2:
        print("Error: Must Specify Mix Number")
        exit()
    mix_num = int(mix_split[1])
    if mix_num not in mixes.keys():
        print("Error: Mix number " + str(mix_num) + " not defined in launch_gem5.py")
        exit()
    args_in = mixes[mix_num].split(" ")
    print("Mix " + str(mix_num) + " selected!")
    print("Executing the following workloads: " + args_in[0])

bm_number = 1
for bm in args_in:

    #create command
    if bm == "specrand_i" or bm == "specrand_f":
        cmd_t = EXE_PATH + run_dir_num[bm] + "specrand" + run_subdir + sub_bin[bm] + exe_subname
    elif bm in sub_bin.keys():
        cmd_t = EXE_PATH + run_dir_num[bm] + bm + run_subdir + sub_bin[bm] + exe_subname
    else:
        cmd_t = EXE_PATH + run_dir_num[bm] + bm + run_subdir + bm + exe_subname
    if bm_number != len(args_in):
        cmds.append(cmd_t + ";")
    else:
        cmds.append(cmd_t)

    in_t = ""
    if bm in file_inputs:
        in_t = input_vals[bm]
        fpath = EXE_PATH + run_dir_num[bm] + bm + run_subdir
        in_t = in_t.format(str(fpath))
    else:
        in_t = input_vals[bm]

    if bm_number != len(args_in):
        inputs.append(in_t + ";")
    else:
        inputs.append(in_t)

    OUT_DIR += bm
    if bm_number < len(args_in):
        OUT_DIR += "_"
    bm_number += 1

if not os.path.isdir(OUT_DIR):
    OUT_DIR += "/"
    os.system("mkdir " + OUT_DIR)
else:
    num = 1
    temp_dir = OUT_DIR + "_" + str(num)
    while os.path.isdir(temp_dir):
        num += 1
        temp_dir = OUT_DIR + "_" + str(num)
    OUT_DIR = temp_dir
    OUT_DIR += "/"
    os.system("mkdir " + OUT_DIR)

#place all commands and inputs into respective field
cmd_str = ""
input_str = ""

for cmd in cmds:
    cmd_str += cmd #+ ";"
cmd_str = "\"" + cmd_str + "\""

for in_val in inputs:
    input_str += in_val #+ ";"
input_str = "\"" + input_str + "\""

print("CMD_STR: " + cmd_str)
print("INPUT STR: " + input_str)

print(GEM5_DIR + "/build/X86_MOESI_hammer/gem5.opt --debug-flags=ProtocolTrace \
-d " + OUT_DIR + " \
" + GEM5_DIR + "/configs/example/se.py \
--maxinsts=1000000000 \
--cpu-type TimingSimpleCPU \
--num-cpus="+ str(NUM_CPUS) + " \
--l1d_size=64kB --l1i_size=32kB --l1d_assoc=4 \
--num-l2caches="+ str(NUM_CPUS) + " \
--l2_size=2MB --l2_assoc=8 \
--num-dirs=4 \
--ruby \
--mem-type=DDR4_2400_8x8 \
--mem-size=4096MB \
--num-chiplets=" + str(NUM_CHIPLETS) + " \
--sni=1 \
--network=garnet2.0 \
--link-width-bits=1024 \
--vcs-per-vnet=4 \
--topology=CHIPS_GTRocket_Mesh_hammer -c " + str(cmd_str) + " -o " + str(input_str))

#1000000000
os.system(GEM5_DIR + "/build/X86_MOESI_hammer/gem5.opt --debug-flags=ProtocolTrace,RubySlicc \
-debug-file=debug.out -d " + OUT_DIR + " \
" + GEM5_DIR + "/configs/example/se.py \
--maxinsts=100000 \
--cpu-type TimingSimpleCPU \
--num-cpus="+ str(NUM_CPUS) + " \
--l1d_size=64kB --l1i_size=32kB --l1d_assoc=4 \
--num-l2caches="+ str(NUM_CPUS) + " \
--l2_size=2MB --l2_assoc=8 \
--num-dirs=4 \
--ruby \
--mem-type=DDR4_2400_8x8 \
--mem-size=4096MB \
--num-chiplets=" + str(NUM_CHIPLETS) + " \
--sni=1 \
--network=garnet2.0 \
--link-width-bits=1024 \
--vcs-per-vnet=4 \
--topology=CHIPS_GTRocket_Mesh_hammer -c " + str(cmd_str) + " -o " + str(input_str))# + "\"")

print(OUT_DIR)
print("CHIPS Demo: Stats:")
os.system("grep \"sim_ticks\" " + OUT_DIR + "stats.txt")
os.system("grep \"average_packet_latency\" " + OUT_DIR + "stats.txt")
print("TEST: $BENCHMARK Finished")
print("=====================================================================")

