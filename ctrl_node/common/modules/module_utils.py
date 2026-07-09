def show_port_open_or_close(result: int, port: int, silence: bool = False):
    """
    Depending on the response parsed to the function prints if the
    port is open or closed, the closed ones can be silenced with the
    True flag.

    Arguments:
        result {int}: The result of the socket function
        port {int}: The scanned port
        silence {bool}: The flag to make close ports not to show
    """
    if result == 0:
        print(f"Port {port}: 	 Open")
    else:
        if not silence:
            print(f"Port {port}: 	 Close")


def rate_ttfb(ttfb: float) -> str:
    """
    Rates a time to first byte measurement using the Core Web Vitals
    TTFB thresholds: good is at or under 0.8s, poor is over 1.8s.

    Arguments:
        ttfb {float}: Time to first byte, in seconds.

    Returns:
        str: "Good", "Needs Improvement", or "Poor".
    """
    if ttfb <= 0.8:
        return "Good"
    if ttfb <= 1.8:
        return "Needs Improvement"
    return "Poor"
