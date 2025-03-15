# System Design Basic Monitor

# Availability
# 1. 99.99999% -> 5 nines, 1 year with 5 minutes downtime


# 2. 99.99% -> 4 nines, 1 month with 4 hours downtime


# 3. 99.9% -> 3 nines, 3.7 days with 8.7 hours downtime

# 4. 99% -> 2 nines, 30.5 days with 24 hours downtime

# 5. 90% -> 1 nines, 365 days with 10 hours downtime

# Reliability (MTBF, MTBF = MTBF / (MTBF + MTTR))
# Reliability = EXP(- Total Time/MTBF)


# SLA Violation Rate
# SLA Violation Rate = (Total Time - MTTR) / Total Time

# Data Accuracy

# Accuracy = 1 - (Total Errors / Total Requests)


# API Performance
# API Performance = (Total Requests - Total Errors) / Total Requests

# API Throughput
# API Throughput = Total Requests / Total Time

# Event Processing Accuracy
# Event Processing Accuracy = 1 - (Total Errors / Total Events)

# Event Processing Throughput
# Event Processing Throughput = Total Events / Total Time


# Network Performance
# Network Performance = (Total Requests - Total Errors) / Total Requests

# Network Throughput
# Network Throughput = Total Requests / Total Time

# Security (like WAF)
