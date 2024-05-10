
# Importar los módulos necesarios para la ejecución del programa.
from datetime import datetime
from genre import GENRE

class Song():
    """Constructor of the class.

        The constructor of the class Song is used to create a new song.

        Syntax
        ------
          song = Song(id, name, artist, duration, release_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the song.
          name : str
            The name of the song.
          artist : str
            The artist of the song.
          duration : int
            The duration of the song in seconds.
          release_date : date
            The release date of the song.
          genres : list
            The genres of the song.

        Returns
        -------
          The new song.

        Example
        -------
          song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])
        """
    #Realizar la implementación de la clase Song.

    # Constructor de la clase Song
    def __init__(self, id, name, artist, duration, release_date, genres = None):
        self.id = id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.release_date = release_date
        self.genres = []

    # Getters y Setters

    def get_id(self):
        if isinstance(self.id, int):
            return self.id
        else:
            raise TypeError("El id de la canción debe ser un número entero.")
        
    def get_name(self):
        if isinstance(self.name, str):
            return self.name
        else:
            raise TypeError("El nombre de la canción debe ser una cadena de caracteres.")
        
    def get_artist(self):
        if isinstance(self.artist, str):
            return self.artist
        else:
            raise TypeError("El id del artista debe ser una cadena de caracteres número.")
        
    def get_duration(self):
        if isinstance(self.duration, int):
            return self.duration
        elif self.duration <= 0:
            return ValueError("La duración no puede ser inferior a 0 segundos.")
        else:
            raise TypeError("La duración de la canción debe ser un numero entero.")
        
    def get_release_date(self):
        if isinstance(self.release_date, datetime):
            return self.release_date
        # No puede ser una fecha futura
        elif self.release_date > datetime.today():

            raise ValueError("La fecha de lanzamiento no puede ser en el futuro.")
        else:
            raise TypeError("La fecha de lanzamiento debe ser de módulo datetime.")
        
    def get_genres(self):
      if isinstance(self.genres, list):
        for genre in self.genres:
            if not isinstance(genre, GENRE):
                raise TypeError("Los elementos de la lista de géneros deben ser instancias de GENRE.")
        return self.genres
      else:
        raise TypeError("El género de la canción debe ser una lista.")

        
    

    # Métodos
    #Añade un elemeto dado "genero" de tipo Genre en el atributo lista "genres"

    def add_genre(self, genro):
        # Si no es de tipo Genere no se añade
        if not isinstance(genro, GENRE):
            raise TypeError("Genre debe ser de módulo GENRE.")
        # Si el género no esta ya en generes se añade
        if genro not in self.genres:
            self.genres.append(genro)
    # Compara dos canciones y evalua si son iguales en base al nombre de la cancion, 
    # el nombre del artista y la fecha de lanzamiento  
    def __eq__(self, other):
        return (isinstance(other, Song) and
                self.name == other.name and
                self.artist == other.artist and
                self.release_date == other.release_date)

    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."






def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, datetime.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == datetime.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, datetime.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, datetime.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()