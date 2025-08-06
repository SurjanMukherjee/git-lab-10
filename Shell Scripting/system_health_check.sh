#!/bin/bash
# =========================================
# Shell Script Task 1: system_health_check.sh
# =========================================

# Get current date for log file naming
DATE=$(date +"%Y-%m-%d")

# 1️⃣ Log Running Processes
PROCESS_LOG="process_log_${DATE}.log"

echo "📋 Currently running processes:"
ps aux   # Show all processes on screen
ps aux > "$PROCESS_LOG"   # Save to log file
echo "✅ Running processes saved to $PROCESS_LOG"
echo "------------------------------------------"

# 2️⃣ Check for High Memory Usage (>30%)
HIGH_MEM_LOG="high_mem_processes.log"

# Get processes with memory usage >30%
ps aux | awk '$4>30 {print}' > temp_high_mem.txt

if [[ -s temp_high_mem.txt ]]; then
    echo "⚠️ WARNING: Processes using more than 30% memory found!"
    cat temp_high_mem.txt   # Print on screen
    cat temp_high_mem.txt >> "$HIGH_MEM_LOG"   # Append to log
else
    echo "✅ No processes found using more than 30% memory."
fi
rm -f temp_high_mem.txt
echo "------------------------------------------"

# 3️⃣ Check Disk Space on Root Partition (>80%)
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if (( DISK_USAGE > 80 )); then
    echo "⚠️ WARNING: Disk usage on / is ${DISK_USAGE}%!"
else
    echo "✅ Disk usage on / is ${DISK_USAGE}%."
fi
echo "------------------------------------------"

# 4️⃣ Display Summary
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(ps aux | awk '$4>30 {print}' | wc -l)

echo "============== Summary =============="
echo "Total running processes: $TOTAL_PROCESSES"
echo "Processes using >30% memory: $HIGH_MEM_COUNT"
echo "Disk usage on /: ${DISK_USAGE}%"
echo "======================================"