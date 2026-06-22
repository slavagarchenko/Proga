from functools import reduce
import json


class Playlist:
    def __init__(self, name, tracks=None):
        self._name = name
        self._tracks = tracks if tracks is not None else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError
        self._name = value

    @staticmethod
    def is_valid_track(track):
        if not isinstance(track, dict):
            return False
        if not "title" in track or not isinstance(track["title"], str) or not track["title"].strip():
            return False
        if not "artist" in track or not isinstance(track["artist"], str) or not track["artist"].strip():
            return False
        if not "duration" in track or not isinstance(track["duration"], int) or track["duration"] <= 0:
            return False
        if not "genre" in track or not isinstance(track["genre"], str) or not track["genre"].strip():
            return False
        if not "rating" in track or not isinstance(track["rating"], (int, float)) or not 1 <= track["rating"] <= 5:
            return False
        return True

    @property
    def tracks(self):
        return self._tracks

    @tracks.setter
    def tracks(self, new_tracks):
        if not isinstance(new_tracks, list):
            raise TypeError
        for track in new_tracks:
            if not self.is_valid_track(track):
                raise TypeError
        self._tracks = new_tracks

    @property
    def total_duration(self):
        return sum(d["duration"] for d in self._tracks)

    @property
    def average_rating(self):
        all_rating = sum(r["rating"] for r in self._tracks)
        return all_rating/len(self._tracks)

    @property
    def genres(self):
        un_genres = set()
        for track in self._tracks:
            un_genres.add(track["genre"])
        return un_genres

    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(data["name"], data["tracks"])

    def recursive_search_by_genre(self, genre, index=0, result=None):
        if result is None:
            result = []
        if index >= len(self._tracks):
            return result
        if genre == self._tracks[index]["genre"]:
            result.append(self._tracks[index])
        return self.recursive_search_by_genre(genre, index+1, result)

    def recursive_total_duration(self, index=0):
        if index >= len(self._tracks):
            return 0
        return self._tracks[index]["duration"] + self.recursive_total_duration(index+1)

    def recursive_find_longest(self, index=0, current_longest=None):
        if current_longest is None:
            current_longest = self._tracks[0] if self._tracks else None
        if index >= len(self._tracks):
            return current_longest
        if current_longest["duration"] < self._tracks[index]["duration"] or current_longest is None:
            current_longest = self._tracks[index]
        return self.recursive_find_longest(index+1, current_longest)

    def filter_by_rating(self, min_rating):
        return list(filter(lambda r: r["rating"] >= min_rating, self._tracks))

    def map_titles(self):
        return list(map(lambda t: t["title"], self._tracks))

    def reduce_total_duration(self):
        return reduce(lambda total, d: total + d["duration"], self._tracks, 0)

    def group_by_genre(self):
        """Группирует треки по жанрам через reduce"""
        def add_to_group(acc, track):
            genre = track['genre']
            if genre not in acc:
                acc[genre] = []
            acc[genre].append(track)
            return acc

        return reduce(add_to_group, self._tracks, {})

    def sort_by_duration(self, reverse=False):
        return sorted(self._tracks, key=lambda d: d["duration"], reverse=reverse)

    def add_track(self, title, artist, duration, genre, rating):
        """Добавляет новый трек"""
        track = {
            'title': title,
            'artist': artist,
            'duration': duration,
            'genre': genre,
            'rating': rating
        }
        if not self.is_valid_track(track):
            raise ValueError("Некорректные данные трека")
        self._tracks.append(track)

    def format_duration(self, seconds):
        """Форматирует длительность в минуты:секунды"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"

    def __str__(self):
        result = f"🎵 {self._name} (треков: {len(self._tracks)}, длительность: {self.format_duration(self.total_duration)}, ср. рейтинг: {self.average_rating:.2f})\n"
        result += f"   Жанры: {', '.join(self.genres)}\n"
        for i, t in enumerate(self._tracks, 1):
            result += f"  {i}. {t['title']} - {t['artist']} ({self.format_duration(t['duration'])}) [{t['genre']}] ⭐{t['rating']}\n"
        return result


print("=" * 70)
print("ПРОВЕРКА КОМПЛЕКСНОГО ЗАДАНИЯ 35")
print("=" * 70)

# 1. Создание плейлиста
playlist = Playlist("Мой любимый плейлист")
playlist.add_track("Bohemian Rhapsody", "Queen", 354, "rock", 5)
playlist.add_track("Stairway to Heaven", "Led Zeppelin", 482, "rock", 5)
playlist.add_track("Imagine", "John Lennon", 183, "pop", 4)
playlist.add_track("Hotel California", "Eagles", 391, "rock", 4)
playlist.add_track("Yesterday", "The Beatles", 125, "pop", 5)
playlist.add_track("Smells Like Teen Spirit", "Nirvana", 302, "grunge", 4)

print("\n1. Исходный плейлист:")
print(playlist)

# 2. Геттеры
print(f"\n2. Геттеры:")
print(
    f"   Общая длительность: {playlist.format_duration(playlist.total_duration)}")
print(f"   Средний рейтинг: {playlist.average_rating:.2f}")
print(f"   Уникальные жанры: {playlist.genres}")

# 3. Рекурсивные методы
print("\n3. Рекурсивные методы:")
rock_tracks = playlist.recursive_search_by_genre("rock")
print(f"   Треки в жанре 'rock': {[t['title'] for t in rock_tracks]}")
print(
    f"   Общая длительность (рекурсивно): {playlist.format_duration(playlist.recursive_total_duration())}")
longest = playlist.recursive_find_longest()
print(
    f"   Самый длинный трек: {longest['title']} ({playlist.format_duration(longest['duration'])})")

# 4. Функциональное программирование
print("\n4. Функциональное программирование:")
high_rated = playlist.filter_by_rating(4)
print(f"   Треки с рейтингом >= 4: {[t['title'] for t in high_rated]}")
print(f"   Названия всех треков: {playlist.map_titles()}")
print(
    f"   Общая длительность (через reduce): {playlist.format_duration(playlist.reduce_total_duration())}")

grouped = playlist.group_by_genre()
print("   Группировка по жанрам:")
for genre, tracks in grouped.items():
    print(f"     {genre}: {[t['title'] for t in tracks]}")

sorted_tracks = playlist.sort_by_duration(reverse=True)
print(f"   Самые длинные треки: {[t['title'] for t in sorted_tracks[:3]]}")

# 5. Создание из JSON
print("\n5. Создание из JSON:")
json_str = json.dumps({
    'name': 'Чилл-плейлист',
    'tracks': [
        {'title': 'Weightless', 'artist': 'Marconi Union',
            'duration': 480, 'genre': 'ambient', 'rating': 4},
        {'title': 'Clair de Lune', 'artist': 'Debussy',
            'duration': 300, 'genre': 'classical', 'rating': 5}
    ]
})
playlist2 = Playlist.from_json(json_str)
print(playlist2)
