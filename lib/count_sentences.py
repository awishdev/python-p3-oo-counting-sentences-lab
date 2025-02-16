#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
    self._value = ''
    self.value = value

  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def get_value(self):
    return self._value
  
  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')

  def count_sentences(self):
    modded_string = self._value.replace('.', '|').replace('?', '|').replace('!', '|')
    return len([sentence for sentence in modded_string.split('|') if sentence.strip()])
