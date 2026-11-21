"""TV class for Lab 12."""


class Television:
    """A television that can be powered, muted, and tuned."""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Start the television's default settings."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle TV on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the TV if it's turned on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by 1, heading back to minimum if at max.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel by 1, heading back to maximum if at min.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Unmute and increase the volume by 1 up to max.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Unmute and decrease the volume by 1 down to min.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return TV's current power, channel and volume status.
        """
        if self.__muted:
            shown_volume = Television.MIN_VOLUME
        else:
            shown_volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {shown_volume}"
