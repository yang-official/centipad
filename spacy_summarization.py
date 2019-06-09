# NLP Pkgs
import spacy
nlp = spacy.load('en_core_web_sm')
# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Import Heapq for Finding the Top N Sentences
from heapq import nlargest

def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary

def data_select(id):
    data = {
        1: 'Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in realtime will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line. Podcasting operational change management inside of workflows to establish a framework. Taking seamless key performance indicators offline to maximise the long tail. Keeping your eye on the ball while performing a deep dive on the start-up mentality to derive convergence on cross-platform integration. Collaboratively administrate empowered markets via plug-and-play networks. Dynamically procrastinate B2C users after installed base benefits. Dramatically visualize customer directed convergence without revolutionary ROI.',
        2: 'Environmental Liability. The Company, the Bank and the Subsidiaries have, and at the Closing Date will have complied in all material respects with all laws, regulations, ordinances and orders relating to public health, safety or the environment (including without limitation all laws, regulations, ordinances and orders relating to releases, discharges, emissions or disposals to air, water, land or groundwater, to the withdrawal or use of groundwater, to the use, handling or disposal of polychlorinated biphenyls, asbestos or urea formaldehyde, to the treatment, storage, disposal or management of hazardous substances, pollutants or contaminants, or to exposure to toxic, hazardous or other controlled, prohibited or regulated substances), the violation of which would or might have a material impact on the Company, the Bank or any Subsidiary or the consummation of the transactions contemplated by this Agreement. There is no legal, administrative, arbitral or other proceeding, claim, action or notice of any nature seeking to impose, or that could result in the imposition of, on the Company, the Bank or any Subsidiary, any liability or obligation of the Company, the Bank or any Subsidiary with respect to any environmental health or safety matter or any private or governmental, environmental health or safety investigation or remediation activity of any nature arising under common law or under any local, state or federal environmental, health or safety statute, regulation or ordinance, including the Comprehensive Environmental Response, Compensation and Liability Act of 1980, as amended (“CERCLA”), pending or, to the Company’s knowledge, threatened against the Company, the Bank or any Subsidiary or any property in which the Company, the Bank or any Subsidiary has taken a security interest the result of which has had or would reasonably be expected to have a Material Adverse Effect; to the Company’s knowledge, there is no reasonable basis for, or circumstances that could reasonably be expected to give rise to, any such proceeding, claim, action, investigation or remediation; and to the Company’s knowledge, none of the Company, the Bank or any Subsidiary is subject to any agreement, order, judgment, decree, letter or memorandum by or with any Governmental Entity or third party that could impose any such environmental obligation or liability. ',
        3: 'Buyer is in compliance with all applicable environmental laws. To the knowledge of Buyer, there are no liabilities of Buyer of any kind, whether accrued, contingent, absolute, determined, determinable or otherwise arising under or relating to any environmental law and, to the knowledge of Buyer, there are no facts, conditions, situations or set of circumstances that could reasonably be expected to result in or be the basis for any such liability. '
    }
    return data[id]

def text_modeler(id):
    data = {
    1: 'Corporate',
    2: 'Banking',
    3: 'Business'
    }
    return data[id]

def flagger(id):
    data = {
    1: 'Jargon, Corporate',
    2: 'Environmental, Chemical',
    3: 'None'
    }
    return data[id]
