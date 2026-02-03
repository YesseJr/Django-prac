from django.core.management.base import BaseCommand
from artists.models import Artist, Song


class Command(BaseCommand):
    help = 'Populate database with initial artist and song data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Song.objects.all().delete()
        Artist.objects.all().delete()

        artists_data = [
            {
                "name": "Michael Jackson",
                "genre": "Pop, R&B, Rock",
                "bio": "The King of Pop, Michael Jackson revolutionized music with his iconic dance moves, groundbreaking music videos, and timeless hits. His influence on pop culture is immeasurable.",
                "image_color": "linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%)",
                "image": "Michael.jpg",
                "songs": [
                    {"title": "Thriller", "year": "1982"},
                    {"title": "Billie Jean", "year": "1983"},
                    {"title": "Beat It", "year": "1983"},
                    {"title": "Smooth Criminal", "year": "1988"},
                    {"title": "Black or White", "year": "1991"},
                    {"title": "Man in the Mirror", "year": "1988"}
                ]
            },
            {
                "name": "Monique Seka",
                "genre": "Afro-Pop, Zouk",
                "bio": "Ivorian music icon Monique Seka is known for her powerful voice and energetic performances. She has been a pioneering force in African pop music since the 1980s.",
                "image_color": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
                "image": "Seka.jpg",
                "songs": [
                    {"title": "Missounwa", "year": "1986"},
                    {"title": "Okaman", "year": "1987"},
                    {"title": "Mawa Née", "year": "1988"},
                    {"title": "Tantie Affoué", "year": "1990"},
                    {"title": "Paradis", "year": "1991"}
                ]
            },
            {
                "name": "Post Malone",
                "genre": "Hip-Hop, Pop, R&B",
                "bio": "Post Malone blends hip-hop, pop, and rock to create his unique sound. Known for his melodic style and heartfelt lyrics, he's become one of the biggest artists of his generation.",
                "image_color": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
                "image": "Malone.jpg",
                "songs": [
                    {"title": "Psycho", "year": "2018"},
                    {"title": "Sunflower", "year": "2018"},
                    {"title": "Rockstar", "year": "2017"},
                    {"title": "Congratulations", "year": "2016"},
                    {"title": "Better Now", "year": "2018"},
                    {"title": "Die For Me", "year": "2018"}
                ]
            },
            {
                "name": "Sia",
                "genre": "Pop, Indie Pop",
                "bio": "Australian singer-songwriter Sia is known for her powerful vocals, emotional songwriting, and unique artistic vision. She's also a successful songwriter for other major artists.",
                "image_color": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
                "image": "Sia.jpg",
                "songs": [
                    {"title": "I'm Still Here", "year": "2018"},
                    {"title": "Bird Set Me Free", "year": "2015"},
                    {"title": "Never Give Up", "year": "2016"},
                    {"title": "Titanium", "year": "2011"},
                    {"title": "Unstoppable", "year": "2016"},
                    {"title": "The Greatest", "year": "2016"}
                ]
            },
            {
                "name": "The Weeknd",
                "genre": "R&B, Pop, Alternative R&B",
                "bio": "The Weeknd has redefined contemporary R&B with his distinctive voice and dark, atmospheric productions. His artistic vision and chart-topping hits have made him a global superstar.",
                "image_color": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "image": "Weeknd.jpg",
                "songs": [
                    {"title": "Blinding Lights", "year": "2019"},
                    {"title": "Starboy", "year": "2016"},
                    {"title": "Call Out My Name", "year": "2018"},
                    {"title": "Can't Feel My Face", "year": "2015"},
                    {"title": "Save Your Tears", "year": "2020"},
                    {"title": "I Feel It Coming", "year": "2016"}
                ]
            },
            {
                "name": "Taylor Swift",
                "genre": "Pop, Country, Indie Folk",
                "bio": "Taylor Swift is one of the best-selling music artists of all time. Known for her narrative songwriting and ability to reinvent her sound, she's won numerous awards and broken countless records.",
                "image_color": "linear-gradient(135deg, #fccb90 0%, #d57eeb 100%)",
                "image": "Swift.jpg",
                "songs": [
                    {"title": "Shake It Off", "year": "2014"},
                    {"title": "Blank Space", "year": "2014"},
                    {"title": "Love Story", "year": "2008"},
                    {"title": "Anti-Hero", "year": "2022"},
                    {"title": "Cruel Summer", "year": "2019"},
                    {"title": "Wildest Dreams", "year": "2015"}
                ]
            },
            {
                "name": "Ina Wroldsen",
                "genre": "Pop, Electropop",
                "bio": "Norwegian singer-songwriter Ina Wroldsen has written hits for numerous artists and achieved success as a solo artist. Her powerful voice and songwriting skills have made her a respected figure in pop music.",
                "image_color": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
                "image": "Ina.jpg",
                "songs": [
                    {"title": "Strongest", "year": "2017"},
                    {"title": "Forgiveness", "year": "2019"},
                    {"title": "Aliens", "year": "2018"},
                    {"title": "Sea", "year": "2020"},
                    {"title": "Mama's Boy", "year": "2019"}
                ]
            },
            {
                "name": "Halsey",
                "genre": "Alternative Pop, Electropop",
                "bio": "Halsey is known for her distinctive voice, honest lyrics, and genre-blending music. She's become a voice for her generation, addressing important social issues through her art.",
                "image_color": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
                "image": "Halsey.jpg",
                "songs": [
                    {"title": "Without Me", "year": "2018"},
                    {"title": "Closer", "year": "2016"},
                    {"title": "Bad at Love", "year": "2017"},
                    {"title": "Eastside", "year": "2018"},
                    {"title": "Graveyard", "year": "2019"},
                    {"title": "Colors", "year": "2016"}
                ]
            },
            {
                "name": "Faouzia",
                "genre": "Pop, R&B",
                "bio": "Moroccan-Canadian singer Faouzia has captivated audiences with her powerful vocals and emotional performances. Her multilingual abilities and songwriting talent have earned her international recognition.",
                "image_color": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
                "image": "Faouzia.jpg",
                "songs": [
                    {"title": "Tears of Gold", "year": "2020"},
                    {"title": "Born Without a Heart", "year": "2018"},
                    {"title": "Battle", "year": "2019"},
                    {"title": "Minefields", "year": "2020"},
                    {"title": "Hero", "year": "2021"},
                    {"title": "Don't Tell Me I'm Pretty", "year": "2021"}
                ]
            },
            {
                "name": "Dua Lipa",
                "genre": "Pop, Dance-Pop",
                "bio": "British-Albanian pop star Dua Lipa has dominated the charts with her disco-influenced pop sound and empowering anthems. Her distinctive voice and style have made her one of pop's biggest stars.",
                "image_color": "linear-gradient(135deg, #fad0c4 0%, #ffd1ff 100%)",
                "image": "Dua.jpg",
                "songs": [
                    {"title": "Levitating", "year": "2020"},
                    {"title": "Don't Start Now", "year": "2019"},
                    {"title": "New Rules", "year": "2017"},
                    {"title": "Physical", "year": "2020"},
                    {"title": "One Kiss", "year": "2018"},
                    {"title": "IDGAF", "year": "2018"}
                ]
            },
            {
                "name": "Nicki Minaj",
                "genre": "Hip-Hop, Pop Rap",
                "bio": "Nicki Minaj is one of the most influential female rappers of all time. Known for her versatile flow, animated persona, and chart-topping hits, she's broken numerous records and barriers in hip-hop.",
                "image_color": "linear-gradient(135deg, #ff0844 0%, #ffb199 100%)",
                "image": "Minaj.jpg",
                "songs": [
                    {"title": "Super Bass", "year": "2011"},
                    {"title": "Anaconda", "year": "2014"},
                    {"title": "Starships", "year": "2012"},
                    {"title": "Moment 4 Life", "year": "2010"},
                    {"title": "Bang Bang", "year": "2014"},
                    {"title": "Chun-Li", "year": "2018"}
                ]
            },
            {
                "name": "Oliver N'Goma",
                "genre": "Afro-Zouk, Soukous",
                "bio": "Gabonese music legend Oliver Ngoma was known for his smooth voice and romantic songs. He was The King of Afro-Zouk music and left an indelible mark on African music before his passing in 2010.",
                "image_color": "linear-gradient(135deg, #ff6e7f 0%, #bfe9ff 100%)",
                "image": "Oliver.png",
                "songs": [
                    {"title": "Bane", "year": "1990"},
                    {"title": "Adia", "year": "1995"},
                    {"title": "Mawonami", "year": "1993"},
                    {"title": "Nge Nge", "year": "1998"},
                    {"title": "Icole", "year": "2000"}
                ]
            }
        ]

        for artist_data in artists_data:
            songs_data = artist_data.pop('songs')
            image_file = artist_data.pop('image')
            
            artist = Artist.objects.create(**artist_data)
            
            for song_data in songs_data:
                Song.objects.create(artist=artist, **song_data)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created artist: {artist.name}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {Artist.objects.count()} artists and {Song.objects.count()} songs')
        )
