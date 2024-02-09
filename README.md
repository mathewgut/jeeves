Hi. This project is very much a work in progress (started within a week of creating this repository and readme).

A couple things to note:

1. <b>This code may be subject to secuirty vulnerabilities</b>. Since most of this code is running through a local port provided by Twitchio and attatched through Twitch and Spotify development platforms, there may be underlying vulnerablities which I am not able to assess.
2. <b>Requirements.</b> To use this code you will need to provide authentication tokens and client id's using the respected platforms (in this case Spotify and Twitch) for setup please visit Spotipy and Twitchio documentation found here: https://spotipy.readthedocs.io/en/2.22.1/ and https://twitchio.dev/en/latest/
3. <b>I only take credit for mashing these libraries and functions together.</b> While I did create most of the seen functions, I used a lot of resources and tools to accomplish the creation of the music commands and the Twitch integration. The example code found in the Getting Started section of TwitchIO docs will allow you to get an understanding of how easy it is to actually throw stuff to the bot to say.
4. <b>The models used for my purposes are not provided in the repository.</b> I simply dont have the resources to pay for the LFS storage needed to host the models used for this project and others. So I will provide a suggested model list below as well as the pros and cons. 
5. <b>Platforms and tools for model inference and performance may very.</b> The code is currently using ctransformers as it is extremley simple to use and allows for models to be pulled from huggingface (so you dont have to manually configure and download a bajillion .bins). However, it does have its limits. I suggest leaving it as is unless youre familiar with data science/machine learning concepts. If you are going to use a model outside of llama please ensure to change the model config/model type as it may not work other wise. 
   Thanks for checking out my project :)

Models used (mainly from https://github.com/TheBloke an awesome opensource ai dev)<br>

<b>Disclaimer:</b> 

All generative ai models I use are GGML. If youre unfamiliar, it essentially means increased performance with lower hardware demand at the cost of inference. This is because I run everything locally (typically off the pc I am streaming on or a laptop) and for the purpose of twitch bots, the quicker the better. If you are planning on hosting this on a server or a platform with higher computational power, you may perfer to use models such as the llama 30b-ggml. 

<br><li>Jeeves main speech model: https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML (q2K variant) <br>
Pros <br> <br>
  Model size and weight is similar to larger size 7b versions which allow for similar (or faster) inference, with increased quality outputs <br>

  Cons <br> <br>
     While more consitant with its reponses, getting it to work at an acceptable (non janky) level within a user driven conversation while keeping it in 'character' proves to be difficult. <br>
  </li><br>

<li>Jeeves unhinged speech model: https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/ (q5_0/q5_1 variant) <br>
Pros <br> <br>
  This model allows you to ask it more outlandish questions. Fantastic for more casual communities and once that are okay with darker/more illicit outputs. <br>
 
  Cons <br> <br>
     Very unhinged. Depending on the tokens and given temperature, the model may ignore the prompt completley or be a bit extreme. It can be far from politically correct and is a lot more prone to hallucinations. <br>
  </li><br>

  <li>Trivia/translate (text-2-text): google/flan-t5-large (use pipeline to avoid manual checkpoints and configuration) this model may be subject to change<br>
Pros <br> <br>
  This model is ideal for logical problem solving or specific tasking. Making it a nice inbetween of the other variants, it is a nice balance of quality and speed.  <br>
 
  Cons <br> <br>
     Requires significant proompt engineering to configure an output that makes sense in unseen usecases. Can sometimes not produce an output (usually when translating something it doesnt know or is too tasking) <br>
  </li><br>
