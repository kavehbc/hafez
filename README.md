# Divan Hafez Poems & Omen

This library gives you access to the Hafez Poems.
To get more information about this poet, you can check [https://en.wikipedia.org/wiki/Hafez](https://en.wikipedia.org/wiki/Hafez).

Poems can be accessed as following:

- By the number of poem,
- By searching a query,
- Random poem (known as Omen or `Fal` in Persian)

## Installation

This package can be installed:

- using `pip`:

```bash
pip install hafez
```

- using `Makefile` on a cloned/forked repo:

```bash
make install
```

- using `pip` on a cloned/forked repo:

```bash
pip install -e . --upgrade --upgrade-strategy only-if-needed
```

## Methods

- `hafez.total_poems()` -> `int`
<br />
It returns `int`, the total number of poems available in the package.


- `hafez.get_poem(poem_id: int)` -> `dict`
<br />
It returns the poem in a dictionary format (see Poem Data Structure)
  
  - `poem_id: int`: It is a number between `1` and `hafez.total_poems()`.


- `hafez.omen()` or `hafez.fal()` -> `dict`
<br />
It returns a random poem in a dictionary format (see Poem Data Structure)


- `hafez.search(qeury: str)` -> `list`
<br />
It returns a list of poems in a dictionary format (see Poem Data Structure)
  
  - `query: str`: It is a string to search within the verses of the Divan Hafez


- `hafez.download_all_audio(force: boolean = False)` -> `int`
<br />
It downloads all the audio files.
  
  - `force: boolean = False`: If it is set to `False`, it only downloads the file if not previously downloaded.
  If set to `True`, it will force to re-download and replace the existing file.


- `hafez.download_audio(poem: int)` -> `int`
<br />
It downloads the audio file of the given `poem`. It returns `1`, once the downloaded is completed.


- `hafez.get_audio(poem: int=1, download: boolean = True)` -> `str`
<br />
It returns the absolute path of the audio file related to the given  `poem`.
  
  - `poem: int=1`: It is the poem number.
  - `download: boolean = True`: If `download=True`, it downloads the audio file if not existing.


## Poem's Data Structure

```json
{"id": 1,
"poem": [],
"interpretation": "",
"alt_interpretation": "",
"mp3": "https://..."}
```

## Example

```python
# it returns the total number of poems
# returns: int
total_number_of_poems = hafez.total_poems()

# get a poem by ID
# returns: dict
poem_5 = hafez.get_poem(5)

# get a random poem - omen (fal)
# returns: dict
omen = hafez.omen()  # same as: hafez.fal()

# search within the verses of poems
# returns: list[dict]
search_result = hafez.search("حافظ")
```

## Database
The poems of Divan Hafez are extracted from an open-source database as below:

Source: [https://github.com/mahmoud-eskandari/HafezFaalDatabase](https://github.com/mahmoud-eskandari/HafezFaalDatabase)

## Vocal Audios
The vocal audio files are done by Ms. Modares Zadeh, and it is available below:  

Source: [https://avayemastan.deklame.net/hafez/](https://avayemastan.deklame.net/hafez/)

## Demo
You can access the demo version deployed on Streamlit server at:

[https://divan-hafez.streamlit.app/](https://divan-hafez.streamlit.app/)


## Developer(s)
Kaveh Bakhtiyari - [Website](http://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

## Contribution
Feel free to join the open-source community and contribute to this repository.
