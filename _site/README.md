## Deadlines

Countdown timers to keep track of a bunch of conference deadlines.

This is a fork of the [ai-deadlines](https://github.com/paperswithcode/ai-deadlines) website.

## Build locally

To build website the [Jekyll](https://jekyllrb.com/docs/) is used. To serve the website you need to install necessary
dependencies and then run the website.

```bash
bundle install 
bundle exec jekyll serve
  ```

## Contributing

### Adding Manually

Contributions are very welcome! To contribute please create a Pull Request in this repository.
New conferences should be added into [_data/conferences.yml](_data%2Fconferences.yml) in the following format:

```yaml
- title: ICLR
  year: 2025
  id: iclr25
  link: https://iclr.cc/Conferences/2025/CallForPapers
  deadline: '2024-10-01 23:59:59'
  abstract_deadline: '2024-09-27 23:59:59'
  timezone: UTC-12
  place: Singapore
  date: Apr 24-28, 2025
  start: 2025-04-24
  end: 2025-04-28
  hindex: 304
  sub:
    - 'ML'
    - 'main_track'
  note: Mandatory abstract deadline on September 27, 2024. More info <a href='https://iclr.cc/Conferences/2025/CallForPapers'>here</a>.

```

### Adding from CSV file

You could create the `conferences.yml` file from the existing `.csv`
file using the [utils/parse_csv.py](_site%2Futils%2Fparse_csv.py) script.
Use the following command to create a config:

```bash
python parse_csv.py example.csv output.yml
```

### Changing types of conferences

The list of the available `sub` types you can found in the [_data/types.yml](_data%2Ftypes.yml) config.
Feel free to modify them too, if needed.

## License

This project is licensed under [MIT][1].

It uses:

- [IcoMoon Icons](https://icomoon.io/#icons-icomoon): [GPL](http://www.gnu.org/licenses/gpl.html) / [CC BY4.0](http://creativecommons.org/licenses/by/4.0/)

[1]: https://abhshkdz.mit-license.org
