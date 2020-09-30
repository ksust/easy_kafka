from easy_kafka.kafka_config import EasyKafkaConfig
from easy_kafka.kafka_producer import EasyKafkaProducer


def demo_produce_msg():
    kafka_producer = EasyKafkaProducer('../conf/conf.yml')
    kafka_producer.produce_msg({'name': 'ksust'})


def demo_produce_msg_with_config():
    config = EasyKafkaConfig('../conf/conf.yml')
    print('config', config.__dict__)
    kafka_producer = EasyKafkaProducer(config)
    kafka_producer.produce_msg({'name': 'ksust'})
    kafka_producer.produce_msg_topic('topic1', {'name': 'ksust'})


if __name__ == "__main__":
    demo_produce_msg()
    demo_produce_msg_with_config()
