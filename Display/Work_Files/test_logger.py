import datetime
import random
import sys
import time

from influxdb import InfluxDBClient

# Set this variables, influxDB should be localhost on Pi
host = "localhost"
port = 8086
user = "admin"
password = "password123"

# The database we created
dbname = "my_db"
# Sample period (s)
interval = 1

# Allow user to set session and runno via args otherwise auto-generate
if len(sys.argv) > 1:
    if (len(sys.argv) < 3):
        print "Must define session and runNo!!"
        sys.exit()
    else:
        session = sys.argv[1]
        runNo = sys.argv[2]
else:
    session = "dev"
    now = datetime.datetime.now()
    runNo = now.strftime("%Y%m%d%H%M")

print "Session: ", session
print "runNo: ", runNo

# Create the InfluxDB object
client = InfluxDBClient(host, port, user, password, dbname)

# Run until keyboard out
try:
    while True:
        # Generate timestamp and random VSENSE value.
        vsense = random.randint(0, 100)
        iso = time.ctime()

        json_body = [
            {
                "measurement": session,
                "tags": {
                    "run": runNo,
                    "geohash": "9v6e6jy4svbe",
                },
                "time": iso,
                "fields": {
                    # "vsense1" : vsense + 1,
                    # "vsense2" : vsense + 2,
                    # "vsense3" : vsense + 3,
                    # "vsense4" : vsense + 4,
                    # "vsense5" : vsense + 5,
                    # "vsense6" : vsense + 6,
                    # "vsense7" : vsense + 7,
                    # "vsense8" : vsense + 8,
                    # "vsense9" : vsense + 9,
                    # "vsense10" : vsense + 10,
                    # "vsense11" : vsense + 11,
                    # "vsense12" : vsense + 12,
                    # "vsense13" : vsense + 13,
                    # "vsense14" : vsense + 14,
                    # "vsense15" : vsense + 15,
                    # "vsense16" : vsense + 16,
                    # "vsense17" : vsense + 17,
                    # "vsense18" : vsense + 18,
                    # "vsense19" : vsense + 19,
                    # "vsense20" : vsense + 20,
                    # "vsense21" : vsense + 21,
                    # "vsense22" : vsense + 10,
                    # "vsense23" : vsense + 11,
                    # "vsense24" : vsense + 12,
                    # "vsense25" : vsense + 13,
                    # "vsense26" : vsense + 14,
                    # "vsense27" : vsense + 15,
                    # "vsense28" : vsense + 16,
                    # "vsense29" : vsense + 17,
                    # "vsense30" : vsense + 18,
                    # "vsense31" : vsense + 19,
                    # "vsense32" : vsense + 20,
                    # "vsense33" : vsense + 21,
                    # "vsense34" : vsense + 10,
                    # "vsense35" : vsense + 11,
                    # "vsense36" : vsense + 12,
                    # "vsense37" : vsense + 13,
                    # "vsense38" : vsense + 14,
                    # "vsense39" : vsense + 15,
                    # "vsense40" : vsense + 16,
                    # "vsense41" : vsense + 17,
                    # "vsense42" : vsense + 18,
                    # "vsense43" : vsense + 19,
                    # "vsense44" : vsense + 20,
                    # "vsense45" : vsense + 21,
                    # "vsense46" : vsense + 10,
                    # "vsense47" : vsense + 11,
                    # "vsense48" : vsense + 12,
                    # "vsense49" : vsense + 13,
                    # "vsense50" : vsense + 14,
                    # "vsense51" : vsense + 15,
                    # "vsense52" : vsense + 16,
                    # "vsense53" : vsense + 17,
                    # "vsense54" : vsense + 18,
                    # "vsense55" : vsense + 19,
                    # "vsense56" : vsense + 14,
                    # "vsense57" : vsense + 15,
                    # "vsense58" : vsense + 16,
                    # "vsense59" : vsense + 17,
                    # "vsense60" : vsense + 16,
                    # "vsense61" : vsense + 17,
                    # "vsense62" : vsense + 18,
                    # "vsense63" : vsense + 19,
                    # "vsense64" : vsense + 20,
                    # "vsense65" : vsense + 21,
                    # "vsense66" : vsense + 10,
                    # "vsense67" : vsense + 11,
                    # "vsense68" : vsense + 12,
                    # "vsense69" : vsense + 13,
                    # "vsense70" : vsense + 14,
                    # "vsense71" : vsense + 15,
                    # "vsense72" : vsense + 16,
                    # "vsense73" : vsense + 17,
                    # "vsense74" : vsense + 18,
                    # "vsense75" : vsense + 19,
                    # "vsense76" : vsense + 14,
                    # "vsense77" : vsense + 15,
                    # "vsense78" : vsense + 16,
                    # "vsense79" : vsense + 17,
                    # "vsense80" : vsense + 16,
                    # "vsense81" : vsense + 17,
                    # "vsense82" : vsense + 18,
                    # "vsense83" : vsense + 19,
                    # "vsense84" : vsense + 20,
                    # "vsense85" : vsense + 21,
                    # "vsense86" : vsense + 10,
                    # "vsense87" : vsense + 11,
                    # "vsense88" : vsense + 12,
                    # "vsense89" : vsense + 13,
                    # "vsense90" : vsense + 14,
                    # "vsense91" : vsense + 15,
                    # "vsense92" : vsense + 16,
                    # "vsense93" : vsense + 17,
                    # "vsense94" : vsense + 18,
                    # "vsense95" : vsense + 19,
                    # "vsense96" : vsense + 14,
                    # "vsense97" : vsense + 15,
                    # "vsense98" : vsense + 16,
                    # "vsense99" : vsense + 17,
                    # "vsense101" : vsense + 1,
                    # "vsense102" : vsense + 2,
                    # "vsense103" : vsense + 3,
                    # "vsense104" : vsense + 4,
                    # "vsense105" : vsense + 5,
                    # "vsense106" : vsense + 6,
                    # "vsense107" : vsense + 7,
                    # "vsense108" : vsense + 8,
                    # "vsense109" : vsense + 9,
                    # "vsense110" : vsense + 10,
                    # "vsense111" : vsense + 11,
                    # "vsense112" : vsense + 12,
                    # "vsense113" : vsense + 13,
                    # "vsense114" : vsense + 14,
                    # "vsense115" : vsense + 15,
                    # "vsense116" : vsense + 16,
                    # "vsense117" : vsense + 17,
                    # "vsense118" : vsense + 18,
                    # "vsense119" : vsense + 19,
                    # "vsense120" : vsense + 20,
                    # "vsense121" : vsense + 21,
                    # "vsense122" : vsense + 10,
                    # "vsense123" : vsense + 11,
                    # "vsense124" : vsense + 12,
                    # "vsense125" : vsense + 13,
                    # "vsense126" : vsense + 14,
                    # "vsense127" : vsense + 15,
                    # "vsense128" : vsense + 16,
                    # "vsense129" : vsense + 17,
                    # "vsense130" : vsense + 18,
                    # "vsense131" : vsense + 19,
                    # "vsense132" : vsense + 20,
                    # "vsense133" : vsense + 21,
                    # "vsense134" : vsense + 10,
                    # "vsense135" : vsense + 11,
                    # "vsense136" : vsense + 12,
                    # "vsense137" : vsense + 13,
                    # "vsense138" : vsense + 14,
                    # "vsense139" : vsense + 15,
                    # "vsense140" : vsense + 16,
                    # "vsense141" : vsense + 17,
                    # "vsense142" : vsense + 18,
                    # "vsense143" : vsense + 19,
                    # "vsense144" : vsense + 20,
                    # "vsense145" : vsense + 21,
                    # "vsense146" : vsense + 10,
                    # "vsense147" : vsense + 11,
                    # "vsense148" : vsense + 12,
                    # "vsense149" : vsense + 13,
                    # "vsense150" : vsense + 14,
                    # "vsense151" : vsense + 15,
                    # "vsense152" : vsense + 16,
                    # "vsense153" : vsense + 17,
                    # "vsense154" : vsense + 18,
                    # "vsense155" : vsense + 19,
                    # "vsense156" : vsense + 14,
                    # "vsense157" : vsense + 15,
                    # "vsense158" : vsense + 16,
                    # "vsense159" : vsense + 17,
                    # "vsense160" : vsense + 16,
                    # "vsense161" : vsense + 17,
                    # "vsense162" : vsense + 18,
                    # "vsense163" : vsense + 19,
                    # "vsense164" : vsense + 20,
                    # "vsense165" : vsense + 21,
                    # "vsense166" : vsense + 10,
                    # "vsense167" : vsense + 11,
                    # "vsense168" : vsense + 12,
                    # "vsense169" : vsense + 13,
                    # "vsense170" : vsense + 14,
                    # "vsense171" : vsense + 15,
                    # "vsense172" : vsense + 16,
                    # "vsense173" : vsense + 17,
                    # "vsense174" : vsense + 18,
                    # "vsense175" : vsense + 19,
                    # "vsense176" : vsense + 14,
                    # "vsense177" : vsense + 15,
                    # "vsense178" : vsense + 16,
                    # "vsense179" : vsense + 17,
                    # "vsense180" : vsense + 16,
                    # "vsense181" : vsense + 17,
                    # "vsense182" : vsense + 18,
                    # "vsense183" : vsense + 19,
                    # "vsense184" : vsense + 20,
                    # "vsense185" : vsense + 21,
                    # "vsense186" : vsense + 10,
                    # "vsense187" : vsense + 11,
                    # "vsense188" : vsense + 12,
                    # "vsense189" : vsense + 13,
                    # "vsense190" : vsense + 14,
                    # "vsense191" : vsense + 15,
                    # "vsense192" : vsense + 16,
                    # "vsense193" : vsense + 17,
                    # "vsense194" : vsense + 18,
                    # "vsense195" : vsense + 19,
                    # "vsense196" : vsense + 14,
                    # "vsense197" : vsense + 15,
                    # "vsense198" : vsense + 16,
                    # "vsense199" : vsense + 17,
                    # "vsense201" : vsense + 1,
                    # "vsense202" : vsense + 2,
                    # "vsense203" : vsense + 3,
                    # "vsense204" : vsense + 4,
                    # "vsense205" : vsense + 5,
                    # "vsense206" : vsense + 6,
                    # "vsense207" : vsense + 7,
                    # "vsense208" : vsense + 8,
                    # "vsense209" : vsense + 9,
                    # "vsense210" : vsense + 10,
                    # "vsense211" : vsense + 11,
                    # "vsense212" : vsense + 12,
                    # "vsense213" : vsense + 13,
                    # "vsense214" : vsense + 14,
                    # "vsense215" : vsense + 15,
                    # "vsense216" : vsense + 16,
                    # "vsense217" : vsense + 17,
                    # "vsense218" : vsense + 18,
                    # "vsense219" : vsense + 19,
                    # "vsense220" : vsense + 20,
                    # "vsense221" : vsense + 21,
                    # "vsense222" : vsense + 10,
                    # "vsense223" : vsense + 11,
                    # "vsense224" : vsense + 12,
                    # "vsense225" : vsense + 13,
                    # "vsense226" : vsense + 14,
                    # "vsense227" : vsense + 15,
                    # "vsense228" : vsense + 16,
                    # "vsense229" : vsense + 17,
                    # "vsense230" : vsense + 18,
                    # "vsense231" : vsense + 19,
                    # "vsense232" : vsense + 20,
                    # "vsense233" : vsense + 21,
                    # "vsense234" : vsense + 10,
                    # "vsense235" : vsense + 11,
                    # "vsense236" : vsense + 12,
                    # "vsense237" : vsense + 13,
                    # "vsense238" : vsense + 14,
                    # "vsense239" : vsense + 15,
                    # "vsense240" : vsense + 16,
                    # "vsense241" : vsense + 17,
                    # "vsense242" : vsense + 18,
                    # "vsense243" : vsense + 19,
                    # "vsense244" : vsense + 20,
                    # "vsense245" : vsense + 21,
                    # "vsense246" : vsense + 10,
                    # "vsense247" : vsense + 11,
                    # "vsense248" : vsense + 12,
                    # "vsense249" : vsense + 13,
                    # "vsense250" : vsense + 14,
                    # "vsense251" : vsense + 15,
                    # "vsense252" : vsense + 16,
                    # "vsense253" : vsense + 17,
                    # "vsense254" : vsense + 18,
                    # "vsense255" : vsense + 19,
                    # "vsense256" : vsense + 14,
                    # "vsense257" : vsense + 15,
                    # "vsense258" : vsense + 16,
                    # "vsense259" : vsense + 17,
                    # "vsense260" : vsense + 16,
                    # "vsense261" : vsense + 17,
                    # "vsense262" : vsense + 18,
                    # "vsense263" : vsense + 19,
                    # "vsense264" : vsense + 20,
                    # "vsense265" : vsense + 21,
                    # "vsense266" : vsense + 10,
                    # "vsense267" : vsense + 11,
                    # "vsense268" : vsense + 12,
                    # "vsense269" : vsense + 13,
                    # "vsense270" : vsense + 14,
                    # "vsense271" : vsense + 15,
                    # "vsense272" : vsense + 16,
                    # "vsense273" : vsense + 17,
                    # "vsense274" : vsense + 18,
                    # "vsense275" : vsense + 19,
                    # "vsense276" : vsense + 14,
                    # "vsense277" : vsense + 15,
                    # "vsense278" : vsense + 16,
                    # "vsense279" : vsense + 17,
                    # "vsense280" : vsense + 16,
                    # "vsense281" : vsense + 17,
                    # "vsense282" : vsense + 18,
                    # "vsense283" : vsense + 19,
                    # "vsense284" : vsense + 20,
                    # "vsense285" : vsense + 21,
                    # "vsense286" : vsense + 10,
                    # "vsense287" : vsense + 11,
                    # "vsense288" : vsense + 12,
                    # "vsense289" : vsense + 13,
                    # "vsense290" : vsense + 14,
                    # "vsense291" : vsense + 15,
                    # "vsense292" : vsense + 16,
                    # "vsense293" : vsense + 17,
                    # "vsense294" : vsense + 18,
                    # "vsense295" : vsense + 19,
                    # "vsense296" : vsense + 14,
                    # "vsense297" : vsense + 15,
                    # "vsense298" : vsense + 16,
                    # "vsense299" : vsense + 17
                    "metric": 1
                }
            }
        ]

        # Write JSON to InfluxDB
        client.write_points(json_body)
        # Wait for next sample
        time.sleep(interval)

except KeyboardInterrupt:
    pass
