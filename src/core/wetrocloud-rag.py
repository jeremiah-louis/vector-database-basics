from wetro import Wetrocloud
from decouple import config
from data.batch_scrape_records import batch_scrape_records
import json
import tempfile

# Initialize the main client and access modules
client = Wetrocloud(api_key=config("WETRO_API_KEY"))

# Create a collection
# collection = client.collection.create_collection(
#   collection_id="records"
# )
batch_scrape_records = [
    {
        "_id": "batch_rec1",
        "chunk_text": [
            "https://docs.firecrawl.dev/features/search",
            "https://www.firecrawl.dev/pricing",
            "https://github.com/mendableai/firecrawl",
            "https://www.zapier.com/",
            "https://www.nvidia.com/",
            "https://www.carrefour.com/",
            "https://www.pwc.com/",
            "https://www.shopify.com/",
            "https://www.fanatics.com/",
            "https://www.cyberagent.co.jp/",
            "https://www.bain.com/",
            "https://www.alibaba.com/",
            "https://gamma.app/",
            "https://phmg.com/",
            "https://www.stack-ai.com/",
            "https://www.teller.io/",
            "https://www.vendr.com/",
            "https://www.open.gov.sg/",
            "https://continue.dev/",
            "https://jasper.ai/",
            "https://www.palladiumdigital.com/",
            "https://www.checkr.com/",
            "https://www.you.com/",
            "https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-firecrawl-reader/",
            "https://python.langchain.com/v0.2/docs/integrations/document_loaders/firecrawl/",
            "https://dify.ai/blog/dify-ai-blog-integrated-with-firecrawl/",
            "https://www.langflow.org/",
            "https://flowiseai.com/",
            "https://crewai.com/",
            "https://docs.camel-ai.org/cookbooks/ingest_data_from_websites_with_Firecrawl.html",
            "https://www.firecrawl.dev/signin/signup",
            "https://docs.firecrawl.dev/",
            "https://x.com/morganlinton/status/1839454165703204955",
            "https://x.com/ChrisDevApps/status/1853587120406876601",
            "https://twitter.com/thepericulum/status/1781397799487078874",
            "https://x.com/TomReppelin/status/1844382491014201613",
            "https://twitter.com/latentsauce/status/1781738253927735331",
            "https://twitter.com/AlexReibman/status/1780299595484131836",
            "https://x.com/alxfazio/status/1826731977283641615",
            "https://x.com/mbusigin/status/1836065372010656069",
            "https://www.firecrawl.dev/extract#pricing",
            "https://docs.firecrawl.dev/rate-limits",
            "https://docs.firecrawl.dev/api-reference/endpoint/scrape",
            "https://www.firecrawl.dev/pricing#credits",
            "https://www.firecrawl.dev/",
        ],
        "category": "web_content",
    },
    {
        "_id": "batch_rec2",
        "chunk_text": [
            "https://docs.mendable.ai/",
            "https://www.mendable.ai/usecases/documentation",
            "https://www.mendable.ai/usecases/cs-enablement",
            "https://www.mendable.ai/usecases/sales-enablement",
            "https://www.mendable.ai/usecases/productcopilot",
            "https://python.langchain.com/",
            "https://0x.org/docs",
            "https://docs.zenlytic.com/",
            "http://gpt-index.readthedocs.io/",
            "https://docs.spectrocloud.com/",
            "https://www.codegpt.co/",
            "https://mendable.wolfia.com/?ref=mendable-website",
            "https://twitter.com/p0larBoy",
            "https://twitter.com/p0larBoy/status/1639119029720993792",
            "https://twitter.com/LangChainAI",
            "https://twitter.com/0xProject",
            "https://twitter.com/0xProject/status/1650521944020905984",
            "https://twitter.com/mendableai",
            "http://0x.org/docs",
            "https://twitter.com/climicrosoft365",
            "https://twitter.com/climicrosoft365/status/1646814193897578499",
            "https://aka.ms/cli-m365",
            "https://twitter.com/michaelanyi",
            "https://twitter.com/michaelanyi/status/1652044901956067342",
            "https://twitter.com/gakonst",
            "https://twitter.com/ericciarla",
            "https://twitter.com/LangChainAI/status/1652012486210768896",
            "https://twitter.com/hwchase17",
            "https://twitter.com/hwchase17/status/1646922765294010368",
            "https://twitter.com/nickscamara_",
            "https://python.langchain.com/en/latest/",
            "https://twitter.com/jerryjliu0",
            "https://twitter.com/jerryjliu0/status/1646899051030548480",
            "https://twitter.com/ai_insight1",
            "https://twitter.com/ai_insight1/status/1652278370946756609",
            "http://mendable.ai/",
            "https://twitter.com/github",
            "https://twitter.com/TaigoKuriyama",
            "https://twitter.com/TaigoKuriyama/status/1651214068550877184",
            "https://www.mendable.ai/",
            "https://twitter.com/mittallakshayy",
            "https://twitter.com/mittallakshayy/status/1623201685756862464",
            "https://twitter.com/sideguide_dev",
            "https://twitter.com/jonbishop",
            "https://twitter.com/jonbishop/status/1623096172348051458",
            "http://builtwithai.co/",
            "http://makewithai.com/",
            "https://twitter.com/krishnerkar",
            "https://twitter.com/krishnerkar/status/1623168288036655104",
            "https://twitter.com/apoorv_taneja",
            "https://twitter.com/apoorv_taneja/status/1623175972714610688",
            "https://twitter.com/williamsrabia",
            "https://twitter.com/williamsrabia/status/1646997576636567552",
            "https://twitter.com/hwchase17/status/1640755705300025349",
            "https://twitter.com/CalebPeffer",
            "https://www.crowdcast.io/c/rh66hcwivly0",
            "https://twitter.com/ravithejads",
            "https://twitter.com/ravithejads/status/1646915078178889740",
            "https://twitter.com/gpt_index",
            "https://twitter.com/garrytrinder",
            "https://twitter.com/garrytrinder/status/1646847691748433920",
            "https://twitter.com/sebastian_rtj",
            "https://twitter.com/sebastian_rtj/status/1642041104127217667",
            "https://twitter.com/AlphaSignalAI",
            "https://twitter.com/satishsampath",
            "https://twitter.com/satishsampath/status/1668838538509705217",
            "https://twitter.com/deepnavy",
            "https://twitter.com/deepnavy/status/1664877028191924224",
            "mailto:hello@mendable.ai",
            "mailto:eric@mendable.ai",
            "https://mendable.ai/",
        ],
        "category": "web_content",
    },
]

# Insert the file as a resource
insert_response = client.collection.insert_resource(
    collection_id="records",
    resource="hello is this okay?",  # Pass the file path, not the JSON string
    type="text"
)

# Query the collection
query_response = client.collection.query_collection(
    collection_id="records",
    request_query="What is the context about firecrawl?"
)

# Print the response
print(query_response)