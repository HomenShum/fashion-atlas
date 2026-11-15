import copy,json,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate import validate_match
class Invariants(unittest.TestCase):
 def setUp(self): self.x=json.loads((ROOT/'examples/catalog_matches.jsonl').read_text().splitlines()[0])
 def test_owned_can_be_liked(self): self.assertTrue(validate_match(self.x));self.assertEqual(self.x['taste'],'liked')
 def test_owned_reason_requires_owned(self):
  self.x['ownership']='needed'
  with self.assertRaises(AssertionError):validate_match(self.x)
 def test_online_stock_not_pickup(self):
  self.x['stock']['online']='in_stock';self.x['pickup_confirmed']=True
  with self.assertRaises(AssertionError):validate_match(self.x)
 def test_pickup_requires_source(self):
  self.x['stock']['branch']='in_stock';self.x['pickup_confirmed']=True
  with self.assertRaises(AssertionError):validate_match(self.x)
 def test_branch_with_source(self):
  self.x['stock']['branch']='in_stock';self.x['pickup_confirmed']=True;self.x['branch_confirmation_source']='synthetic branch confirmation'
  self.assertTrue(validate_match(self.x))
 def test_ai_no_fit_claim(self):
  self.x['image_kind']='ai';self.x['approximation_label']=True;self.x['fit_proven']=True
  with self.assertRaises(AssertionError):validate_match(self.x)
 def test_ai_label_required(self):
  self.x['image_kind']='ai'
  with self.assertRaises(AssertionError):validate_match(self.x)
 def test_unknown_taste_preserved(self):
  self.x['taste']='unknown';self.assertTrue(validate_match(self.x))
if __name__=='__main__':unittest.main()
