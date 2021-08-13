package org.renpy.android;

public class Constants {
    // Used by the in-app purchasing code.
    public static String store = "{{ config.store }}";

    // The names of the asset packs to check and download.
{% if bundle %}
    public static String assetPacks[ ] = { "ff1", "ff2", "ff3", "ff4" };
{% else %}
    public static String assetPacks[ ] = { };
{% endif %}

}
