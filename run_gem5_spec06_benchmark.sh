#!/bin/bash
#
# run_gem5_alpha_spec06_benchmark.sh
# Author: Mark Gottscho Email: mgottscho@ucla.edu
# Copyright (C) 2014 Mark Gottscho
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 
############ DIRECTORY VARIABLES: MODIFY ACCORDINGLY #############
GEM5_DIR=/home/grads/g/ginochacon/gem5_garnet2_CHIPS                          # Install location of gem5
SPEC_DIR=/home/grads/g/ginochacon/spec-SE                  # Install location of your SPEC2006 benchmarks
##################################################################
 
ARGC=$# # Get number of arguments excluding arg0 (the script itself). Check for help message condition.
if [[ "$ARGC" != 2 ]]; then # Bad number of arguments.
    echo "run_gem5_alpha_spec06_benchmark.sh  Copyright (C) 2014 Mark Gottscho"
   echo "This program comes with ABSOLUTELY NO WARRANTY; for details see <http://www.gnu.org/licenses/>."
   echo "This is free software, and you are welcome to redistribute it under certain conditions; see <http://www.gnu.org/licenses/> for details."
   echo ""
    echo "Author: Mark Gottscho"
    echo "mgottscho@ucla.edu"
    echo ""
    echo "This script runs a single gem5 simulation of a single SPEC CPU2006 benchmark for Alpha ISA."
    echo ""
    echo "USAGE: run_gem5_alpha_spec06_benchmark.sh <BENCHMARK> <OUTPUT_DIR>"
    echo "EXAMPLE: ./run_gem5_alpha_spec06_benchmark.sh bzip2 /FULL/PATH/TO/output_dir"
    echo ""
    echo "A single --help help or -h argument will bring this message back."
    exit
fi
 
# Get command line input. We will need to check these.
BENCHMARK=$1                    # Benchmark name, e.g. bzip2
OUTPUT_DIR=$2                   # Directory to place run output. Make sure this exists!
 
######################### BENCHMARK CODENAMES ####################
PERLBENCH_CODE=400.perlbench
BZIP2_CODE=401.bzip2
GCC_CODE=403.gcc
BWAVES_CODE=410.bwaves
GAMESS_CODE=416.gamess
MCF_CODE=429.mcf
MILC_CODE=433.milc
ZEUSMP_CODE=434.zeusmp
GROMACS_CODE=435.gromacs
CACTUSADM_CODE=436.cactusADM
LESLIE3D_CODE=437.leslie3d
NAMD_CODE=444.namd
GOBMK_CODE=445.gobmk
DEALII_CODE=447.dealII
SOPLEX_CODE=450.soplex
POVRAY_CODE=453.povray
CALCULIX_CODE=454.calculix
HMMER_CODE=456.hmmer
SJENG_CODE=458.sjeng
GEMSFDTD_CODE=459.GemsFDTD
LIBQUANTUM_CODE=462.libquantum
H264REF_CODE=464.h264ref
TONTO_CODE=465.tonto
LBM_CODE=470.lbm
OMNETPP_CODE=471.omnetpp
ASTAR_CODE=astar
WRF_CODE=481.wrf
SPHINX3_CODE=482.sphinx3
XALANCBMK_CODE=483.xalancbmk
SPECRAND_INT_CODE=998.specrand
SPECRAND_FLOAT_CODE=999.specrand
##################################################################
 
# Check BENCHMARK input
#################### BENCHMARK CODE MAPPING ######################
BENCHMARK_CODE="none"
CMD_CODE="none"
 
if [[ "$BENCHMARK" == "perlbench" ]]; then
    BENCHMARK_CODE=$PERLBENCH_CODE
fi
if [[ "$BENCHMARK" == "bzip2" ]]; then
    BENCHMARK_CODE=$BZIP2_CODE
fi
if [[ "$BENCHMARK" == "gcc" ]]; then
    BENCHMARK_CODE=$GCC_CODE
fi
if [[ "$BENCHMARK" == "bwaves" ]]; then
    BENCHMARK_CODE=$BWAVES_CODE
fi
if [[ "$BENCHMARK" == "gamess" ]]; then
    BENCHMARK_CODE=$GAMESS_CODE
fi
if [[ "$BENCHMARK" == "mcf" ]]; then
    BENCHMARK_CODE=$MCF_CODE
fi
if [[ "$BENCHMARK" == "milc" ]]; then
    BENCHMARK_CODE=$MILC_CODE
fi
if [[ "$BENCHMARK" == "zeusmp" ]]; then
    BENCHMARK_CODE=$ZEUSMP_CODE
fi
if [[ "$BENCHMARK" == "gromacs" ]]; then
    BENCHMARK_CODE=$GROMACS_CODE
fi
if [[ "$BENCHMARK" == "cactusADM" ]]; then
    BENCHMARK_CODE=$CACTUSADM_CODE
fi
if [[ "$BENCHMARK" == "leslie3d" ]]; then
    BENCHMARK_CODE=$LESLIE3D_CODE
fi
if [[ "$BENCHMARK" == "namd" ]]; then
    BENCHMARK_CODE=$NAMD_CODE
fi
if [[ "$BENCHMARK" == "gobmk" ]]; then
    BENCHMARK_CODE=$GOBMK_CODE
fi
if [[ "$BENCHMARK" == "dealII" ]]; then # DOES NOT WORK
    BENCHMARK_CODE=$DEALII_CODE
fi
if [[ "$BENCHMARK" == "soplex" ]]; then
    BENCHMARK_CODE=$SOPLEX_CODE
fi
if [[ "$BENCHMARK" == "povray" ]]; then
    BENCHMARK_CODE=$POVRAY_CODE
fi
if [[ "$BENCHMARK" == "calculix" ]]; then
    BENCHMARK_CODE=$CALCULIX_CODE
fi
if [[ "$BENCHMARK" == "hmmer" ]]; then
    BENCHMARK_CODE=$HMMER_CODE
fi
if [[ "$BENCHMARK" == "sjeng" ]]; then
    BENCHMARK_CODE=$SJENG_CODE
fi
if [[ "$BENCHMARK" == "GemsFDTD" ]]; then
    BENCHMARK_CODE=$GEMSFDTD_CODE
fi
if [[ "$BENCHMARK" == "libquantum" ]]; then
    BENCHMARK_CODE=$LIBQUANTUM_CODE
fi
if [[ "$BENCHMARK" == "h264ref" ]]; then
    BENCHMARK_CODE=$H264REF_CODE
fi
if [[ "$BENCHMARK" == "tonto" ]]; then
    BENCHMARK_CODE=$TONTO_CODE
fi
if [[ "$BENCHMARK" == "lbm" ]]; then
    BENCHMARK_CODE=$LBM_CODE
fi
if [[ "$BENCHMARK" == "omnetpp" ]]; then
    BENCHMARK_CODE=$OMNETPP_CODE
fi
if [[ "$BENCHMARK" == "astar" ]]; then
    BENCHMARK_CODE=$ASTAR_CODE
    CMD_CODE=$ASTAR_CMD
fi
if [[ "$BENCHMARK" == "wrf" ]]; then
    BENCHMARK_CODE=$WRF_CODE
fi
if [[ "$BENCHMARK" == "sphinx3" ]]; then
    BENCHMARK_CODE=$SPHINX3_CODE
fi
if [[ "$BENCHMARK" == "xalancbmk" ]]; then # DOES NOT WORK
    BENCHMARK_CODE=$XALANCBMK_CODE
fi
if [[ "$BENCHMARK" == "specrand_i" ]]; then
    BENCHMARK_CODE=$SPECRAND_INT_CODE
fi
if [[ "$BENCHMARK" == "specrand_f" ]]; then
    BENCHMARK_CODE=$SPECRAND_FLOAT_CODE
fi
 
# Sanity check
if [[ "$BENCHMARK_CODE" == "none" ]]; then
    echo "Input benchmark selection $BENCHMARK did not match any known SPEC CPU2006 benchmarks! Exiting."
    exit 1
fi
##################################################################
 
# Check OUTPUT_DIR existence
if [[ !(-d "$OUTPUT_DIR") ]]; then
    echo "Output directory $OUTPUT_DIR does not exist! Exiting."
    exit 1
fi
#/scratch/user/ginochacon/spec_2006_binaries/running_folder 
RUN_DIR=$SPEC_DIR/running_folder/$BENCHMARK_CODE #run/run_base_ref\_my-alpha.0000     # Run directory for the selected SPEC benchmark
#RUN_DIR=$SPEC_DIR/benchspec/CPU2006/$BENCHMARK_CODE/run/run_base_ref\_my-alpha.0000     # Run directory for the selected SPEC benchmark
SCRIPT_OUT=$OUTPUT_DIR/runscript.log                                                                    # File log for this script's stdout henceforth

CMD_CODE="astar $RUN_DIR/BigLakes2048.cfg"
 
################## REPORT SCRIPT CONFIGURATION ###################
 
echo "Command line:"                                | tee $SCRIPT_OUT
echo "$0 $*"                                        | tee -a $SCRIPT_OUT
echo "================= Hardcoded directories ==================" | tee -a $SCRIPT_OUT
echo "GEM5_DIR:                                     $GEM5_DIR" | tee -a $SCRIPT_OUT
echo "SPEC_DIR:                                     $SPEC_DIR" | tee -a $SCRIPT_OUT
echo "==================== Script inputs =======================" | tee -a $SCRIPT_OUT
echo "BENCHMARK:                                    $BENCHMARK" | tee -a $SCRIPT_OUT
echo "OUTPUT_DIR:                                   $OUTPUT_DIR" | tee -a $SCRIPT_OUT
echo "==========================================================" | tee -a $SCRIPT_OUT
##################################################################
 
 
#################### LAUNCH GEM5 SIMULATION ######################
echo ""
echo "Changing to SPEC benchmark runtime directory: $RUN_DIR" | tee -a $SCRIPT_OUT
cd $RUN_DIR
 
echo "" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT
echo "--------- Here goes nothing! Starting gem5! ------------" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT

#--benchmark_stderr=$OUTPUT_DIR/$BENCHMARK.err  
# Actually launch gem5!
#$GEM5_DIR/configs/example/se.py --cpu-type TimingSimpleCPU \
$GEM5_DIR/build/X86_MOESI_hammer/gem5.opt --outdir=$OUTPUT_DIR --benchmark=$BENCHMARK --benchmark_stdout=$OUTPUT_DIR/$BENCHMARK.out\
$GEM5_DIR/configs/example/spec06_config.py --cpu-type TimingSimpleCPU \
--num-cpus=64 \
--l1d_size=64kB --l1i_size=32kB --l1d_assoc=4 \
--num-l2caches=64 \
--l2_size=2MB --l2_assoc=8 \
--num-dirs=4 \
--ruby \
--mem-type=DDR3_1600_8x8 \
--mem-size=1024MB \
--num-chiplets=8 \
--sni=0 \
--network=garnet2.0 \
--link-width-bits=1024 \
--vcs-per-vnet=4 \
--topology=CHIPS_GTRocket_Mesh_hammer \
| tee -a $SCRIPT_OUT
#--cmd="astar $RUN_DIR/BigLakes2048.cfg " \
#$GEM5_DIR/build/X86_MOESI_hammer/gem5.opt --outdir=$OUTPUT_DIR $GEM5_DIR/configs/example/spec06_config.py --benchmark=$BENCHMARK --benchmark_stdout=$OUTPUT_DIR/$BENCHMARK.out --benchmark_stderr=$OUTPUT_DIR/$BENCHMARK.err <YOUR_SIMULATOR_OPTIONS_HERE> | tee -a $SCRIPT_OUT
