/*
 * Copyright (c) 1999-2008 Mark D. Hill and David A. Wood
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef __MEM_RUBY_SLICC_INTERFACE_RUBYSLICC_COMPONENTMAPPINGS_HH__
#define __MEM_RUBY_SLICC_INTERFACE_RUBYSLICC_COMPONENTMAPPINGS_HH__

#include <cmath>

#include "debug/ProtocolTrace.hh"
#include "debug/RubyNetwork.hh"
#include "mem/ruby/common/Address.hh"
#include "mem/ruby/common/MachineID.hh"
#include "mem/ruby/common/NetDest.hh"
#include "mem/ruby/protocol/MachineType.hh"
#include "mem/ruby/structures/DirectoryMemory.hh"
#include "mem/ruby/common/DataBlock.hh"

inline NetDest
broadcast(MachineType type)
{
    NetDest dest;
    for (NodeID i = 0; i < MachineType_base_count(type); i++) {
        MachineID mach = {type, i};
        dest.add(mach);
    }
    return dest;
}

inline MachineID
mapAddressToRange(Addr addr, MachineType type, int low_bit,
                  int num_bits, int cluster_id = 0)
{

    MachineID mach = {type, 0};
    if (num_bits == 0)
        mach.num = cluster_id;
    else
        //num_bits defintion can be found in
        //configs/ruby/MESI_Two_Level.py
        //cluster_id here refers to the machineID of the L1Cache
        //If L1Cache ID is 3 and number of L2 Caches is 2;
        //Then the mach.num=1
        mach.num = cluster_id/pow(2 , num_bits);

        //mach.num = bitSelect(addr, low_bit, low_bit + num_bits - 1)
        //    + (1 << num_bits) * cluster_id;

    //DPRINTF(ProtocolTrace, "Cache_Map: Addr:%x; Type:%s;"
    //"low_bit:%d; num_bits:%d; cluster_id:%d; L2Cache-num:%d\n",
    //printAddress(addr), MachineType_to_string(type),
    //low_bit, num_bits, cluster_id, mach.num);

    return mach;
}

/////////////// TROJAN ////////////////////
inline Addr
intToAddr(uint64_t addr){
  Addr temp;
  temp = addr;
  return temp;
}

inline NodeID
intToNodeID(int num)
{
  return NodeID(num);
}

inline bool
test(int n)
{
    return false;
}

inline MachineID
createMachineIDint(MachineType type, int id)
{
    MachineID mach = {type, NodeID(id)};
    return mach;
}


/////////////// TROJAN ////////////////////

inline bool
printDataBlock(DataBlock db){
  db.print(std::cout);
  return true;
}

inline DataBlock
createTrojanData(){
  DataBlock datablk;
  uint8_t *db;
  db = new uint8_t[64];
  int a = 0;
  for(a = 0; a < 3; a+=4){//63; a+=2){
    if(a > 60){
      db[a] = 0xbe;
      db[a+1] = 0xef;
    }
  }
  datablk.assign(db);
  return datablk;
}

inline NodeID
machineIDToNodeID(MachineID machID)
{
    return machID.num;
}

inline MachineType
machineIDToMachineType(MachineID machID)
{
    return machID.type;
}

inline int
machineCount(MachineType machType)
{
    return MachineType_base_count(machType);
}

inline MachineID
createMachineID(MachineType type, NodeID id)
{
    MachineID mach = {type, id};
    return mach;
}

inline MachineID
MachineTypeAndNodeIDToMachineID(MachineType type, NodeID node)
{
    MachineID mach = {type, node};
    return mach;
}

#endif  // __MEM_RUBY_SLICC_INTERFACE_COMPONENTMAPPINGS_HH__
