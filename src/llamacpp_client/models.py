from typing import Any
from pydantic import BaseModel, Field, model_validator


class Image(BaseModel):
    data: str  #Base64-encoded image data
    id: int  #Image ID


class Lora(BaseModel):
    id: int  #LoRA adapter ID
    scale: float  #Scale of the LoRA adapter


class ImageData(BaseModel):
    id: int # image id
    data: str  # base64 string with image


class Message(BaseModel):
    role: str
    content: str


class File(BaseModel):
    filename: str
    text: str


class Completions(BaseModel):
    prompt: str | list[int] | list[int | str] | list[str] | list[str | list[int]]  #Prompt for completion
    temperature: float | None = None               #Randomness of generated text, default: 0.8
    dynatemp_range: float  | None = None           #Dynamic temperature range, default: 0.0
    dynatemp_exponent: float | None = None         #Dynamic temperature exponent, default: 1.0
    top_k: int | None = None                       #Limit next token selection to K most probable, default: 40
    top_p: float | None = None                     #Limit next token selection to cumulative probability P, default: 0.95
    min_p: float | None = None                     #Minimum probability for a token, relative to most likely, default: 0.05
    n_predict: int | None = None                   #Max tokens to predict (-1 for infinity), default: -1
    n_indent: int | None = None                    #Minimum line indentation, default: 0
    n_keep: int | None = None                      #Number of tokens from prompt to retain (0 for none, -1 for all) default: 0
    stream: bool = False                           #Enable streaming output, default: False
    stop: list[str] | None = None                  #JSON array of stopping strings
    typical_p: float | None = None                 #Enable locally typical sampling (1.0 to disable), default: 1.0
    repeat_penalty: float | None = None            #Control repetition of token sequences, default: 1.1
    repeat_last_n: int | None = None               #Last N tokens to consider for penalizing repetition (0 to disable, -1 for ctx-size), default: 64
    presence_penalty: float | None = None          #Repeat alpha presence penalty (0.0 to disable), default: 0.0
    frequency_penalty: float | None = None         #Repeat alpha frequency penalty (0.0 to disable), default: 0.0
    dry_multiplier: float | None = None            #DRY repetition penalty multiplier (0.0 to disable), default: 0.0
    dry_base: float | None = None                  #DRY repetition penalty base value, default: 1.75
    dry_allowed_length: int | None = None          #Tokens that extend repetition receive penalty, default: 2
    dry_penalty_last_n: int | None = None          #How many tokens to scan for repetitions (0 disable, -1 = ctx-size), default: -1
    dry_sequence_breakers: list[str] | None = None #Array of sequence breakers for DRY sampling
    xtc_probability: float | None = None           #Chance for token removal via XTC sampler (0.0 to disable), default: 0.0
    xtc_threshold: float | None = None             #Minimum probability threshold for XTC removal (> 0.5 disables XTC), default: 0.1
    mirostat: int | None = None                    #Enable Mirostat sampling (0: disabled, 1: Mirostat, 2: Mirostat 2.0), default: 0
    mirostat_tau: float | None = None              #Mirostat target entropy, parameter tau, default: 5.0
    mirostat_eta: float | None = None              #Mirostat learning rate, parameter eta, default: 0.1
    grammar: str | None | None = None              #Set grammar for grammar-based sampling, default: None
    json_schema: dict[str, Any] | None  = None     #Set a JSON schema for grammar-based sampling, default: None
    seed: int  | None = None                       #RNG seed (-1 for random seed), default: -1
    ignore_eos: bool | None = None                 #Ignore end of stream token, default: False
    logit_bias: list[list[int | str | bool | float]] | None = None #Modify token likelihood [[token, bias]] #Complicated
    n_probs: int | None = None                     #If > 0, return top N token probabilities, default: 0
    min_keep: int | None = None                    #Force samplers to return N possible tokens minimum, default: 0
    t_max_predict_ms: int | None = None            #Time limit in ms for the prediction phase, default: 0
    image_data: list[Image] | None = None          #Array of objects holding base64 image data and IDs
    id_slot: int | None = None                     #Assign the completion task to a specific slot, default: -1
    cache_prompt: bool | None = None               #Re-use KV cache from previous request if possible, default: True
    return_tokens: bool | None = None              #Return raw generated token IDs in the tokens field, default: False
    samplers: list[str] | None = None              #Order samplers should be applied
    timings_per_token: bool | None = None          #Include prompt processing and text generation speed info in each response, default: False
    post_sampling_probs: bool | None = None        #Returns the probabilities of top n_probs tokens after applying sampling chain., default: False
    response_fields: list[str] | None = None       #List of response fields to include, default: None
    lora: list[Lora]  | None = None                #List of LoRA adapters to be applied to this request


class Tokenize(BaseModel):
    content: str
    add_special: bool = False
    with_pieces: bool = False


class Detokenize(BaseModel):
    tokens: list[int]


class ApplyTemplate(BaseModel):
    messages: list[Message]


class Embedding(BaseModel):
    content: str
    image_data: list[ImageData] | None = None


class Infill(Completions):
    prompt: str | None = None
    input_prefix: str | None = None
    input_suffix: str | None = None
    input_extra: list[File] | None = None