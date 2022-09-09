# Reload Shell

If you update your `~/.aliases` file or you `~/.\*rc` it may be a pain to quit your terminal and load all the set up you had. Instead you can reload your shell with the [`exec`][exec] command:

```bash
exec $SHELL
```

where `SHELL` should be replace with your current shell. Typically one of the following:
- `bash`
- `zsh`
- `fish`
**UPDATE** to makde `SHELL` and env variable to automatically reload the shell without you typing which one you are using


[exec]: https://www.shell-tips.com/linux/how-to-reload-shell/#gsc.tab=0 "Reloading Shell"
