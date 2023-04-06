import time
import random
import constants as Cons
import config
from adafruit_helper import *
from mask_detection import *
from yolobit import *
#************************************************************************************************************************
def publish(count, max_count=5):
    
    _feed_id = Cons.Feeds.Feed1.value
    _count = (0 if count >= max_count else count + 1)

    if _count > 0:
        _feed_id = Cons.Feeds.Feed2.value
    
    mqtt_client.publish(_feed_id, _value:=random.randint(0, 100), config.ADAFRUIT_IO_USERNAME)

    return _count, _feed_id, _value

def sample1_publishing():    
    _count = 0
    while True:
        _count, _feed_id, _value = publish(_count)
        print('Publishing value: [{0}] to [{1}].'.format(_value, _feed_id))    
        time.sleep(1)


#************************************************************************************************************************
def subscribe(client: mqtt_client, feed_id):
    def on_message(client, feed_id, payload):
        print(f"Received `{payload}` from `{feed_id}` topic")        

    client.subscribe(feed_id)
    client.on_message = on_message

def sample2_subscribing():    
    subscribe(mqtt_client, Cons.Feeds.Feed1.value)
    while True: 
        # TODO: Add implementation
        pass
        

#************************************************************************************************************************
def run():
    
    #sample1_publishing()
    #sample2_subscribing()
    #image_detector()
    #run_camera(mqtt_client)
    yolobit_run(mqtt_client)

