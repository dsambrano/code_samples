# Apply `Sed` Replacement inside a full directory

Applying `sed` commands is super useful.
But sometimes you need a little more power!
Specifically, you need to apply the `sed` find and replace to all the files in a directory.
For that, you can check out these commands (sources: [1][source1] and [2][source2]):

```bash

# Method 1
grep -l "@nyu.edu" ./ |xargs sed -i "s/@nyu.edu/@harvard.edu/g"

# Method 2
find ./ -type f -exec sed -i -e 's/apple/orange/g' {} \;
```

[source1]: https://stackoverflow.com/a/35607711
[source2]: https://stackoverflow.com/a/6759339


