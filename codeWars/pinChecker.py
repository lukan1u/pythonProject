def validate_pin(pin):
    # isdigit checks for int type data
      return len(pin) in (4, 6) and pin.isdigit()
