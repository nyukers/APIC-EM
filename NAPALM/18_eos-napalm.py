#
# NAPALM Arista EOS preview
#

from napalm import get_network_driver

driver = get_network_driver('eos')
device = driver('eos-spine1', 'ntc', 'ntc123')

# device – переменная, содержащая объект устройства NAPALM. Этот объект имеет методы для работы с конфигурациями устройства, в том числе
# и для выполнения операции замены конфигурации. Операция выполняется с помощью метода load_replace_candidate().

device.open() # требуется для загрузки регистрационных данных и установления соединения с устройством на основе используемого API
device.load_replace_candidate(filename='eos-spine1.conf')

diffs = device.compare_config()
print(diffs)

if diffs:
    device.commit_config()
    
device.rollback()
