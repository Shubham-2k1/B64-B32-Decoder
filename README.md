# Base64/Base32 Decoder

## Description
This Python script is designed to decode strings encoded in either Base64 or Base32 format. It provides a command-line interface to decode encoded strings and output the decoded text.

## Usage
python3 base64_base32_decoder.py --b64 [cipher] | --b32 [cipher] [-v]

## Arguments
- `--b64 [cipher]`: Decode Base64-encoded text. Multiple encoded strings can be provided.
- `--b32 [cipher]`: Decode Base32-encoded text. Multiple encoded strings can be provided.
- `-v`: Print the version of the script.

## Examples
- Decode a Base64-encoded string:
python3 base64_base32_decoder.py --b64 aGk=

Output:
hi

- Decode a Base32-encoded string:
python3 base64_base32_decoder.py --b32 NBSWY3DP

## Note
- Run the script with either `--b64` or `--b32` along with the encoded string to decode it.
- The script can handle decoding of both Base64 and Base32 encoded strings.
- For more information, use the `-h` or `--help` option.
