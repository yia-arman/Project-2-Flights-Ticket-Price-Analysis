from FlightTicket import FlightTicket

with FlightTicket() as bot:
    bot.get_webpage()
    bot.fly_from('New York ')
    bot.fly_to('Miami ')
    bot.flight_date()
    bot.submit()






