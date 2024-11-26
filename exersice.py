
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson")
print(oscar_winners)

oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.remove("Meryl Streep")
oscar_winners_copy.clear()

common_actors = titanic_actors & dark_knight_actors
print("the actors who played in both movies are: ", common_actors)

common_actors2 = iron_man_actors & avengers_actors
print("the actors who played in both movies are: ", common_actors2)

is_subset = avengers_actors.issubset(actor_list)
if is_subset:
    print("all actors is avengers in the list")
else:
    print("not all actors is avengers in the list")

removed_actor = movie_cast.pop()
print(f"the actor who gone is: {removed_actor}")
print("the remaining actors are: ", movie_cast)

removed_actor = movie_cast.remove("Matt Damon")
print(movie_cast)

actors_no_oscar = titanic_actors - oscar_winners
print("the actors that play on titanic and didn't win oscars are: ", actors_no_oscar)

actors_titanic_dark_knight = titanic_actors | dark_knight_actors
common_actors = titanic_actors & dark_knight_actors
unique_actors = actors_titanic_dark_knight - common_actors
print("the actors that show in one of the movies are: ", unique_actors)

oscar_winners.update({"Blanchett Cate", "Lewis-Day Daniel"})
print(oscar_winners)

all_actors = titanic_actors | dark_knight_actors

print("all the actors in two movies: ", all_actors)
