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

bm_names = ["perlbench", "gcc", "bwaves", "gamess", "mcf", "milc", "zeusmp", 
                        "gromacs", "cactusADM", "leslie3d", "namd", "gobmk", "soplex", 
                        "povray", "calculix", "hmmer", "sjeng",
                        "libquantum", "h264ref", "tonto", "lbm", "omnetpp", "astar", 
                        "wrf", "sphinx3", "xalancbmk", "specrand_i", "specrand_f"]
#"bzip2","GemsFDTD" 

run_subdir = "/run/run_base_ref_amd64-m64-gcc43-nn.0000/"
exe_subname = "_base.amd64-m64-gcc43-nn"

run_dir_num = { "perlbench" : "400.", "bzip2" : "401.", "gcc" : "403.",\
                                "bwaves" : "410.", "gamess" : "416.", "mcf" : "429.",\
                                "milc" : "433.", "zeusmp" : "434.", "gromacs" : "435.",\
                                "cactusADM" : "436.", "leslie3d" : "437.", "namd" : "444.",\
                                "gobmk" : "445.", "soplex" : "450.", "povray" : "453.",\
                                "calculix" : "454.", "hmmer" : "456.", "sjeng" : "458.",\
                                "GemsFDTD" : "459.", "libquantum" : "462.", "h264ref" : "464.",\
                                "tonto" : "465.", "lbm" : "470.", "omnetpp" : "471.", "astar" : "473.",\
                                "wrf" : "481.", "sphinx3" : "482.", "xalancbmk" : "483.",\
                                "specrand_i" : "998.", "specrand_f" : "999."}

input_vals = {  "perlbench"     : "-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1", 
                                "bzip2"             : "input.source 280", 
                                "gcc"               : "166.i -o 166.s",
                                "bwaves"            : "", 
                                "gamess"            : "cytosine.2.config", 
                                "mcf"               : "inp.in",
                                "milc"              : "su3imp.in", 
                                "zeusmp"            : "", 
                                "gromacs"       : "-silent -deffnm gromacs -nice 0",\
                                "cactusADM"     : "benchADM.par", 
                                "leslie3d"      : "", 
                                "namd"              : "--input namd.input --output namd.out --iterations 38",\
                                "gobmk"             : "--quiet --mode gtp", 
                                "soplex"            : "-m45000 pds-50.mps", 
                                "povray"            : "SPEC-benchmark-ref.ini",\
                                "calculix"      : "-i hyperviscoplastic", 
                                "hmmer"             : "nph3.hmm swiss41", 
                                "sjeng"             : "ref.txt",\
                                "GemsFDTD"      : "",
                                "libquantum"    : "1397 7", 
                                "h264ref"       : "-d foreman_ref_encoder_baseline.cfg",\
                                "tonto"             : "", 
                                "lbm"               : "300 reference.dat 0 0 100_100_130_ldc.of", 
                                "omnetpp"       : "omnetpp.ini", 
                                "astar"             : "rivers.cfg",\
                                "wrf"               : "", 
                                "sphinx3"       : "ctlfile . args.an4", 
                                "xalancbmk"     : "-v t5.xml xalanc.xsl",\
                                "specrand_i"    : "1255432124 234923", 
                                "specrand_f"    : "1255432124 234923"} 

#substitute names for the SPEC workloads that do not conform to directory naming scheme....
sub_bin = {"xalancbmk" : "Xalan"} 
#launch form:
#"EXE_PATH + run_dir_num[bench] + bench + run_subdir + bench + exe_subname " + input_vals[bench]

cwd = os.getcwd()

#for each of the arguments create a cmd and the required inputs
cmds = []
inputs = []

bm_number = 1
for bm in args_in:

    #create command
    if bm in sub_bin.keys():
        cmd_t = EXE_PATH + run_dir_num[bm] + bm + run_subdir + sub_bin[bm] + exe_subname
    else:
        cmd_t = EXE_PATH + run_dir_num[bm] + bm + run_subdir + bm + exe_subname
    if bm_number != len(args_in):
        cmds.append(cmd_t + ";")
    else:
        cmds.append(cmd_t)

    in_t = EXE_PATH + run_dir_num[bm] + bm + run_subdir + input_vals[bm]
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
print(input_str)

os.system(GEM5_DIR + "/build/X86_MOESI_hammer/gem5.opt \
-d " + OUT_DIR + " \
" + GEM5_DIR + "/configs/example/se.py \
--maxinsts=5000000000 \
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

