import json

from easy_kafka.kafka_consumer import EasyKafkaConsumer


def start_consumer():
    kafka_consumer = EasyKafkaConsumer('../conf/conf.yml')
    print('consumer iterator started')
    for record in kafka_consumer:
        print('record', record.value)
        print('json', json.loads(record.value))


if __name__ == "__main__":
    start_consumer()
