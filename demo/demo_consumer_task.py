import json

from easy_kafka.kafka_consumer import EasyKafkaConsumer
from easy_kafka.kafka_producer import EasyKafkaProducer

kafka_producer = EasyKafkaProducer('../conf/conf.yml')


def consumer_task(record):
    """
    consumer callback
    :param record: object
    :return:
    """
    print('consumer_task', record.value)
    print('json', json.loads(record.value))
    if record.topic is 'topic1':
        kafka_producer.produce_msg({'type': 'task result'})


def start_consumer():
    kafka_consumer = EasyKafkaConsumer('../conf/conf.yml')
    print('consumer task started')
    kafka_consumer.subscribe(fn=consumer_task)


if __name__ == "__main__":
    start_consumer()
