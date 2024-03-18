from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import json

class QandABot():
    def __init__(self):
        self.model_name = "deepset/bert-base-cased-squad2"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
    def QandA(self, question, context):
        inputs = self.tokenizer(question, context, return_tensors="pt")
        outputs = self.model(**inputs)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        answer_start = torch.argmax(start_scores)
        answer_end = torch.argmax(end_scores)
        answer = self.tokenizer.convert_tokens_to_string(self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end+1]))
        print(answer)


if __name__ == "__main__":
    Scotty = QandABot()
    # Question = "You are a helpful topic model. Every prompt will be an abstract, your job is to analyze the abstract and extract a list of possible topics for it. The topics start at a high level and get more detailed as you go. The topics for example should be like Computer Science or Business etc..., output should be JSON with the root being the abstract"
    # Abstract = "Mesophotic reef corals remain largely unexplored in terms of the genetic adaptations and physiological mechanisms to acquire, allocate, and use energy for survival and reproduction. In the Hawaiian Archipelago, the Leptoseris species complex form the most spatially extensive mesophotic coral ecosystem known and provide habitat for a unique community. To study how the ecophysiology of Leptoseris species relates to symbiont-host specialization and understand the mechanisms responsible for coral energy acquisition in extreme low light environments, we examined Symbiodinium (endosymbiotic dinoflagellate) photobiological characteristics and the lipids and isotopic signatures from Symbiodinium and coral hosts over a depth-dependent light gradient (55-7 mu mol photons m(-2) s(-1), 60-132 m). Clear performance differences demonstrate different photoadaptation and photoacclimatization across this genus. Our results also show that flexibility in photoacclimatization depends primarily on Symbiodinium type. Colonies harboring Symbiodinium sp. COI-2 showed significant increases in photosynthetic pigment content with increasing depth, whereas colonies harboring Symbiodinium spp. COI-1 and COI-3 showed variability in pigment composition, yield measurements for photosystem II, as well as size and density of Symbiodinium cells. Despite remarkable differences in photosynthetic adaptive strategies, there were no significant differences among lipids of Leptoseris species with depth. Finally, isotopic signatures of both host and Symbiodinium changed with depth, indicating that coral colonies acquired energy from different sources depending on depth. This study highlights the complexity in physiological adaptations within this symbiosis and the different strategies used by closely related mesophotic species to diversify energy acquisition and to successfully establish and compete in extreme light-limited environments."
    # Scotty.QandA(Question, Abstract)
    # Abstract = "This paper examines the disparate impact of US federal regulations on small businesses. Using a two-sector dynamic general equilibrium model, we obtained two implications of higher regulation on small firms that have yet to be empirically tested in the published literature. First, as regulations increase, small firms' share of employment shrinks. Second, as regulations rise, small firms' share of total output falls. Using a panel of industry-specific US regulatory restrictions, we found that a 10% increase in federal regulations was associated with an approximate 0.8% reduction in small firms' share of industry employment and a nearly 1.5% decline in small firms' share of industry output."
    # Scotty.QandA(Question, Abstract)
    Scotty.QandA("What is the best way to code a sort algorithm?", "")