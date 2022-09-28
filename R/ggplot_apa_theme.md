# APA Theme Template for GGplot

GGplot theme is better than the default, but its still pretty visually cluttered. 
If you prefer the cleaner APA style look, here is a theme for you:

```R
apatheme=theme_bw()+
  theme(panel.grid.major=element_blank(),
        panel.grid.minor=element_blank(),
        panel.border=element_blank(),
        panel.background = element_rect(fill = "transparent"),#
        axis.line=element_line(),
        text=element_text(family='Arial'),#
        legend.background = element_rect(fill = "transparent", linetype="solid"),#
        legend.box.background = element_rect(fill = "transparent", linetype="solid"),#
        plot.background = element_rect(fill = "transparent",colour = NA))#

apatheme_keep_text=theme_bw()+
  theme(panel.grid.major=element_blank(),
        panel.grid.minor=element_blank(),
        panel.border=element_blank(),
        panel.background = element_rect(fill = "transparent"),#
        axis.line=element_line(),
        legend.background = element_rect(fill = "transparent", linetype="solid"),#
        legend.box.background = element_rect(fill = "transparent", linetype="solid"),#
        plot.background = element_rect(fill = "transparent",colour = NA))#

```

Add either one to your code (the top changes the font, otherwise they are they same).
Then, once you are ready simply add that theme to your `ggplot`, and the theme will be automatically applied.

```R
ggplot(data aes(...)) + apatheme
```
