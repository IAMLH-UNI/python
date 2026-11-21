from television import Television


def test_init_status_channel_and_volume() -> None:
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power_turns_tv_on() -> None:
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_power_turns_tv_off() -> None:
    tv = Television()
    tv.power()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute_while_on_after_volume_increase() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_mute_while_on_then_unmute() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_mute_when_tv_is_off_and_muted() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute_when_tv_is_off_and_unmuted() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


def test_channel_up_while_off() -> None:
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_up_while_on() -> None:
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


def test_channel_up_past_maximum() -> None:
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down_while_off() -> None:
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_down_past_minimum() -> None:
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


def test_volume_up_while_off() -> None:
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_up_while_on() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_up_while_muted() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_up_past_maximum() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down_while_off() -> None:
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_down_while_on() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_down_while_muted() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_down_past_minimum() -> None:
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
