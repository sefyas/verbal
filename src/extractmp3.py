import sys
from ros import rosbag

def extract_audio(bag_path, topic_name, mp3_path):
   print 'Opening bag'
   bag = rosbag.Bag(bag_path)
   mp3_file = open(mp3_path, 'w')
   print 'Reading audio messages and saving to mp3 file'
   msg_count = 0
   for topic, msg, stamp in bag.read_messages(topics=[topic_name]):
      if msg._type == 'audio_common_msgs/AudioData':
         msg_count += 1
         mp3_file.write(''.join(msg.data))
   bag.close()
   mp3_file.close()
   print 'Done. %d audio messages written to %s'%(msg_count, mp3_path)

if __name__ == '__main__':
   # assumes the name of bag files under the bag_folder_path that should be processed are listed in bagFiles.txt
   # example call python src/extractmp3.py /home/yasaman/Data/VPbD /audio /home/yasaman/Data/VPbD
   # note that folder pathes do NOT end in '/'
   print 'bag_folder_path: ', sys.argv[1], ' topic_name: ', sys.argv[2], 'mp3_folder_path: ', sys.argv[3]
   bag_file_names = open("/home/yasaman/ROSprojects/verbal_pbd_ws/src/verbal/src/bagFiles.txt", "r");
   names = bag_file_names.readlines()
   names = [x.strip() for x in names] 
   for name in names:
      print 'processing bag: ', sys.argv[1]+'/'+name, ' into mp3: ', sys.argv[3]+'/'+name.strip('.bag')+'.mp3'
      #extract_audio(sys.argv[1]+'/'+name, sys.argv[2], sys.argv[3]+'/'+name.strip('.bag')+'.mp3')
