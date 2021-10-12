import json
import os

this_dir = os.path.dirname(os.path.realpath(__file__))


class Base:

    data_path = ''

    def open_file(self) -> dict:
        with open(self.data_path) as f:
            data = f.read()
            data = json.loads(data)
            f.close()
        return data

    def replace_file_data(self, new_data: dict):

        if not isinstance(new_data, dict):
            return

        with open(self.data_path, 'w') as f:
            data = json.dumps(new_data, indent=2)
            f.write(data)


class Entities(Base):

    data_path = os.path.join(this_dir, 'jsons/entities.json')

    def add_config(self, from_entity, target_entity):

        configs = self.configs
        new_config = [from_entity, target_entity]

        for config in configs:
            if config[0] == target_entity and config[1] == from_entity:
                raise ValueError('You are forwarding two entities to each other as a cycle, this will cause '
                                 'an infinity loop. please don\'t do that. :)')

        if new_config in configs:
            raise ValueError('This config already exists')

        else:
            configs.append(new_config)

        new_data = {"entities": configs}
        self.replace_file_data(new_data)

    def remove_config(self, from_entity: str):
        configs = self.configs

        counter = 0
        for config in configs[:]:
            if from_entity == config[0]:
                configs.remove(config)
                counter += 1

        if counter == 0:
            raise ValueError(f'There is no linked entity with [ `{from_entity}` ].')

        new_data = {"entities": configs}
        self.replace_file_data(new_data)
        return counter

    def get_target_entities(self, from_entity) -> list:
        configs = self.configs

        target_entities = []
        for config in configs:
            if config[0] == from_entity:
                target_entities.append(config[1])

        return target_entities

    @property
    def configs(self) -> list:
        data = self.open_file()
        return data['entities']

    @property
    def entities(self):
        configs = self.configs
        entities = list(map(lambda x: x[0], configs))
        return entities


class Filters(Base):

    data_path = filters_file = os.path.join(this_dir, 'jsons/filters.json')

    def add_filter(self, from_word: str, to_word: str):
        words = self.words
        new_config = [from_word, to_word]

        for config in words:
            if config[0] == to_word and config[1] == from_word:
                raise ValueError('You are filtering two words to each other as a cycle, this will cause '
                                 'an infinity loop. please don\'t do that. :)')

            if from_word == config[0]:
                raise ValueError(f'Word **{from_word}** is already filtered to **{config[1]}**')

        if new_config in words:
            raise ValueError('This filter already exists')

        else:
            words.append(new_config)

        new_data = {"words": words}
        self.replace_file_data(new_data)

    def remove_filter(self, from_word: str):
        words = self.words

        counter = 0
        for config in words[:]:
            if from_word == config[0]:
                words.remove(config)
                counter += 1

        if counter == 0:
            raise ValueError('This filter does not exist.')

        new_data = {"words": words}
        self.replace_file_data(new_data)
        return counter

    @property
    def words(self) -> list:
        data = self.open_file()
        return data['words']


class Messages(Base):
    data_path = filters_file = os.path.join(this_dir, 'jsons/messages.json')

    def add(self, base_entity, base_message, target_entity, target_message):
        messages = self.messages

        key = f'{base_entity}:{base_message}'
        value = [target_entity, target_message]

        if messages.get(key) is not None:
            messages[key] = messages[key].append(value)

        else:
            messages[key] = [value]

        self.replace_file_data(messages)

    def get(self, base_entity, base_message) -> list:
        messages = self.messages

        value: str = messages.get(f'{base_entity}:{base_message}', None)

        if value is None:
            raise ValueError()

        return value

    @property
    def messages(self) -> dict:
        data = self.open_file()
        return data


class Config(Base):
    data_path = filters_file = os.path.join(this_dir, 'jsons/config.json')

    @property
    def sudo(self):
        data = self.open_file()
        return data['sudo']

    @property
    def bot_enabled(self):
        data = self.open_file()
        return data['bot_enabled']

    @property
    def sign(self):
        data = self.open_file()
        return data['signature']

    def get(self, key: str):
        data = self.open_file()
        return data[key]

    def change(self, key: str, value: str):

        """
        keys:
            bot_enabled\n
            filter_words\n
            add_signature\n
            signature\n

        :param key: config key
        :param value: new config value
        :return: None
        """

        data = self.open_file()
        data[key] = value
        self.replace_file_data(data)
