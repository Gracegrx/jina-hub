# BleuEvaluator

Bilingual Evaluation Understudy Score. Evaluates the generated sentence against a desired sentence. 
A perfect match will score 1.0 and a complete mismatch will score 0.0

BLEU works well with n-grams of at least 4, if less than that, it's neccessary to use a smoothing function.