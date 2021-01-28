from unittest import mock
from UFV import UFV

# ufv_ins = UFV('')
# ufv_ins.run()

def r2(self):
    self.status = 'mock r2 status'
    self.reason = 'mock r2 reason'
    self.r2 = 'mock r2'
    print('self.r2: ', self.r2)
def r1(self):
    self.status = 'mock r1 status'
    self.reason = 'mock r1 reason'
    self.r1 = 'mock r1'
    print('self.r1: ', self.r1)
@mock.patch.object(UFV,'r2', autospec = True, return_value='')
@mock.patch.object(UFV,'r1', autospec = True)
def test_mock_ufv(mock_r1, mock_r2, capsys):
    ufv_ins = UFV("")
    mock_r1.side_effect = r1
    mock_r2.side_effect = r2
    ufv_ins.run()
    # print(ufv_ins.status)
    out, err = capsys.readouterr()
    print("test:", out)
    assert ufv_ins.status == 'mock r2 status'
    # assert 0


@mock.patch('UFV.UFV',  autospec = UFV)
def test_mock_ufv(self, mock_ufv, capsys):
    def r2(self):
        self.status = 'mock r2 status'
        self.reason = 'mock r2 reason'
        self.r2 = 'mock r2'
        print('self.r2: ', self.r2)
    def r1(self):
        self.status = 'mock r1 status'
        self.reason = 'mock r1 reason'
        self.r1 = 'mock r1'
        print('self.r1: ', self.r1)
    mock_ufv_ins = mock_ufv.return_value
    mock_ufv_ins.status = ''
    mock_ufv_ins.reason = ''
    mock_ufv_ins.r1 = ''
    mock_ufv_ins.r2 = ''
    mock_ufv_ins.r1.side_effect = r1(mock_ufv_ins)
    mock_ufv_ins.r2.side_effect = r2(mock_ufv_ins)
    mock_ufv_ins.run()
    # print(ufv_ins.status)
    out, err = capsys.readouterr()
    print("test:", out)
    assert mock_ufv_ins.status == 'mock r2 status'
